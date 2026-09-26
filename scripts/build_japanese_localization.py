#!/usr/bin/env python3
"""Build a complete Japanese Localizable.strings catalog at minimal model cost.

The script augments the English catalog with referenced UI keys that currently
fall back to hard-coded source strings, then translates every entry in bounded
structured batches using the lowest-cost available model. It validates that all
keys and protected format tokens survive before writing the Japanese catalog.
"""
from __future__ import annotations

import concurrent.futures
import json
import os
import re
import sys
import time
from collections import OrderedDict
from pathlib import Path
from typing import Iterable

from openai import OpenAI

ROOT = Path(__file__).resolve().parents[1]
EN_PATH = ROOT / "Natives/resources/en.lproj/Localizable.strings"
JA_PATH = ROOT / "Natives/resources/ja.lproj/Localizable.strings"
MODEL = os.environ.get("LOCALIZATION_MODEL", "gpt-5-nano")
BATCH_SIZE = 75
MAX_WORKERS = 4

PAIR_RE = re.compile(r'^\s*"((?:[^"\\]|\\.)*)"\s*=\s*"((?:[^"\\]|\\.)*)"\s*;', re.M)
LITERAL_RE = r'@"((?:[^"\\]|\\.)*)"'
CALL_RE = re.compile(
    r'\b(?:localize|MPLocalized|NSLocalizedString)\s*\(\s*'
    + LITERAL_RE + r'\s*,\s*' + LITERAL_RE,
    re.S,
)
PLACEHOLDER_RE = re.compile(r"%(?:\d+\$)?[-+#0 \\']*\d*(?:\.\d+)?(?:@|[diuoxXfFeEgGcCsSp])")
URL_RE = re.compile(r'https?://[^\s\\"<>]+')
ANGLE_TOKEN_RE = re.compile(r'<[^<>\n]+>')

MANUAL_EN = {
    "Cancel": "Cancel",
    "Delete": "Delete",
    "Done": "Done",
    "Edit profile": "Edit profile",
    "Error": "Error",
    "None": "None",
    "OK": "OK",
    "Release": "Release",
    "Rename": "Rename",
    "Share": "Share",
    "Sign in": "Sign in",
    "Warning": "Warning",
    "login.cancelled": "Sign-in cancelled",
    "download.progress.file_count_short": "%1$ld/%2$ld · %3$@",
    "download.history.result.success": "Completed",
    "download.history.result.failed": "Failed",
    "download.history.title": "Download History",
    "download.history.clear": "Clear",
    "download.history.empty": "No download history yet",
    "download.history.clear_confirm": "Clear all download history? This action cannot be undone.",
    "download.history.cancel": "Cancel",
    "download.history.entry": "History",
    "mc_news.read_more": "Read more",
    "mc_news.title": "Minecraft News",
    "mc_news.retry": "Retry",
    "mc_news.load_failed": "Failed to load",
    "preference.title.language": "Language",
    "preference.detail.language": "Choose the launcher display language. The interface refreshes immediately.",
    "preference.title.language-ja": "Japanese",
    "preference.title.language-default": "Default (English)",
}


def unescape_string(value: str) -> str:
    """Decode the limited escape syntax used by .strings source values."""
    return re.sub(r'\\([\\"nrt])', lambda m: {
        "\\": "\\", '"': '"', "n": "\n", "r": "\r", "t": "\t"
    }[m.group(1)], value)


def escape_string(value: str) -> str:
    return (value.replace("\\", "\\\\")
                 .replace('"', '\\"')
                 .replace("\n", "\\n")
                 .replace("\r", "\\r")
                 .replace("\t", "\\t"))


def parse_catalog(path: Path) -> OrderedDict[str, str]:
    pairs = OrderedDict()
    for key, value in PAIR_RE.findall(path.read_text(encoding="utf-8")):
        pairs[unescape_string(key)] = unescape_string(value)
    return pairs


def source_fallback_entries() -> dict[str, str]:
    discovered: dict[str, str] = {}
    for path in ROOT.joinpath("Natives").rglob("*"):
        if not path.is_file() or path.suffix not in {".m", ".mm", ".h", ".c"}:
            continue
        if "external" in path.parts:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for key, fallback in CALL_RE.findall(text):
            key, fallback = unescape_string(key), unescape_string(fallback)
            # NSLocalizedString's second argument is a developer comment, not fallback.
            # The current code only uses its second arg as a Chinese fallback in a few
            # locations; catalog values supplied below replace those code paths.
            if key.startswith(("mp.", "common.")) or key in {
                "login.title", "login.cancelled", "download.progress.file_count_short",
                "download.history.result.success", "download.history.result.failed",
                "download.history.title", "download.history.clear", "download.history.empty",
                "download.history.clear_confirm", "download.history.cancel", "download.history.entry",
                "mc_news.read_more", "mc_news.title", "mc_news.retry", "mc_news.load_failed",
            }:
                discovered[key] = fallback
    return discovered


def protect(value: str) -> tuple[str, list[str]]:
    """Replace fragile format tokens with unambiguous markers before translation."""
    tokens: list[str] = []
    combined = re.compile("|".join((PLACEHOLDER_RE.pattern, URL_RE.pattern, ANGLE_TOKEN_RE.pattern)))

    def repl(match: re.Match[str]) -> str:
        tokens.append(match.group(0))
        return f"[[AMETHYST_TOKEN_{len(tokens) - 1}]]"

    return combined.sub(repl, value), tokens


def restore(value: str, tokens: list[str]) -> str:
    for index, token in enumerate(tokens):
        marker = f"[[AMETHYST_TOKEN_{index}]]"
        if value.count(marker) != 1:
            raise ValueError(f"protected token {marker} was not preserved exactly once")
        value = value.replace(marker, token)
    return value


def chunks(items: list[tuple[str, str]], size: int) -> Iterable[list[tuple[str, str]]]:
    for index in range(0, len(items), size):
        yield items[index:index + size]


def request_translations(client: OpenAI, entries: list[dict[str, str]], instruction: str) -> tuple[dict[str, str], dict[str, int]]:
    prompt = instruction + "\n\nEntries:\n" + json.dumps(entries, ensure_ascii=False)
    schema = {
        "type": "json_schema",
        "json_schema": {
            "name": "japanese_localization_batch",
            "strict": True,
            "schema": {
                "type": "object",
                "properties": {
                    "translations": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "key": {"type": "string"},
                                "text": {"type": "string"},
                            },
                            "required": ["key", "text"],
                            "additionalProperties": False,
                        },
                    }
                },
                "required": ["translations"],
                "additionalProperties": False,
            },
        },
    }
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a precise professional Japanese software localizer."},
            {"role": "user", "content": prompt},
        ],
        response_format=schema,
        max_completion_tokens=14000,
    )
    payload = json.loads(response.choices[0].message.content)
    usage = response.usage
    return ({item["key"]: item["text"] for item in payload["translations"]}, {
        "prompt_tokens": getattr(usage, "prompt_tokens", 0) or 0,
        "completion_tokens": getattr(usage, "completion_tokens", 0) or 0,
    })


def translate_batch(batch_index: int, batch: list[tuple[str, str]]) -> tuple[int, dict[str, str], dict[str, int]]:
    protected: list[dict[str, str]] = []
    token_map: dict[str, list[str]] = {}
    for key, english in batch:
        safe_value, tokens = protect(english)
        protected.append({"key": key, "text": safe_value})
        token_map[key] = tokens

    instruction = """Translate the supplied iOS Minecraft launcher localization strings from English into natural Japanese.

Rules:
- Return exactly one Japanese translation for every supplied key, retaining every key unchanged.
- Translate only `text`; never translate keys, token markers such as [[AMETHYST_TOKEN_0]], code, product names, version numbers, or filenames.
- Preserve all token markers exactly and exactly once. Do not add or remove placeholders.
- Use concise, natural Japanese for an iOS app. Use standard Japanese terminology: Mod=Mod, shader pack=シェーダーパック, resource pack=リソースパック, modpack=Modパック, launcher=ランチャー.
- Keep UI labels short where possible. Preserve Markdown syntax and any punctuation encoded in token markers.
-- Do not explain the translations."""

    client = OpenAI()

    last_error: Exception | None = None
    for attempt in range(4):
        try:
            translated, usage = request_translations(client, protected, instruction)
            expected_keys = {key for key, _ in batch}
            unexpected = set(translated) - expected_keys
            if unexpected:
                raise ValueError(f"batch returned unexpected keys: {sorted(unexpected)[:3]}")
            missing = expected_keys - set(translated)
            if missing:
                recovery_entries = [entry for entry in protected if entry["key"] in missing]
                recovery_instruction = instruction + "\n\nReturn every entry below. A previous response omitted these keys, so no key may be skipped."
                recovered, recovery_usage = request_translations(client, recovery_entries, recovery_instruction)
                if set(recovered) != missing:
                    raise ValueError(f"recovery key mismatch; missing={sorted(missing - set(recovered))[:3]}")
                translated.update(recovered)
                usage["prompt_tokens"] += recovery_usage["prompt_tokens"]
                usage["completion_tokens"] += recovery_usage["completion_tokens"]
            for key in expected_keys:
                translated[key] = restore(translated[key], token_map[key])
            return batch_index, translated, {
                "prompt_tokens": usage["prompt_tokens"],
                "completion_tokens": usage["completion_tokens"],
            }
        except Exception as exc:  # bounded retry; failures are never silently accepted
            last_error = exc
            time.sleep(2 ** attempt)
    raise RuntimeError(f"Batch {batch_index} failed after retries: {last_error}")


def append_missing_english_entries(catalog: OrderedDict[str, str]) -> int:
    fallback_entries = source_fallback_entries()
    fallback_entries.update(MANUAL_EN)
    added = 0
    for key in sorted(fallback_entries):
        if key not in catalog:
            catalog[key] = fallback_entries[key]
            added += 1
    return added


def write_catalog(path: Path, catalog: OrderedDict[str, str]) -> None:
    header = "/*\n  Localizable.strings\n  Japanese localization for Air\n*/\n\n"
    lines = [header]
    for key, value in catalog.items():
        lines.append(f'"{escape_string(key)}" = "{escape_string(value)}";\n')
    path.write_text("".join(lines), encoding="utf-8")


def main() -> int:
    if not os.environ.get("OPENAI_API_KEY"):
        print("OPENAI_API_KEY is required", file=sys.stderr)
        return 2

    english = parse_catalog(EN_PATH)
    before = len(english)
    added = append_missing_english_entries(english)
    if added:
        write_catalog(EN_PATH, english)
        print(f"Added {added} referenced UI entries to English catalog ({before} -> {len(english)}).")

    items = list(english.items())
    batches = list(chunks(items, BATCH_SIZE))
    translated: dict[str, str] = {}
    usage = {"prompt_tokens": 0, "completion_tokens": 0}
    print(f"Translating {len(items)} strings in {len(batches)} batches with {MODEL}.")
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = [executor.submit(translate_batch, index, batch) for index, batch in enumerate(batches)]
        for future in concurrent.futures.as_completed(futures):
            index, result, batch_usage = future.result()
            translated.update(result)
            usage["prompt_tokens"] += batch_usage["prompt_tokens"]
            usage["completion_tokens"] += batch_usage["completion_tokens"]
            print(f"Completed batch {index + 1}/{len(batches)} ({len(result)} strings).", flush=True)

    if set(translated) != set(english):
        raise RuntimeError("Translation output does not cover the full English catalog")
    japanese = OrderedDict((key, translated[key]) for key in english)
    write_catalog(JA_PATH, japanese)
    print(f"Wrote {len(japanese)} Japanese strings to {JA_PATH}.")
    print(json.dumps(usage))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
