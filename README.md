<div align="center">
  <img src="Natives/Assets.xcassets/AppIcon-Light.appiconset/1024x1024.png" alt="Air アイコン" width="120" style="border-radius: 24px;">
</div>

<h1 align="center">Air</h1>
<p align="center"><sub>Amethyst iOS Remastered</sub></p>

<div align="center">
  <img alt="ビルド状態" src="https://github.com/386612/Amethyst-JP/actions/workflows/development.yml/badge.svg?branch=main">
  <img alt="ダウンロード数" src="https://img.shields.io/github/downloads/386612/Amethyst-JP/total?label=Downloads&style=flat">
  <img alt="リリース" src="https://img.shields.io/github/v/release/386612/Amethyst-JP?style=flat">
  <img alt="ライセンス" src="https://img.shields.io/github/license/386612/Amethyst-JP?style=flat">
  <a title="Crowdin" target="_blank" href="https://crowdin.com/project/amethyst-ios-remastered"><img alt="Crowdin" src="https://badges.crowdin.net/amethyst-ios-remastered/localized.svg"></a>
</div>

<p align="center">
  <a href="./README.md">日本語</a> | <a href="./README_EN.md">English</a> | <a href="./README_CN.md">简体中文</a>
</p>

---

**Air** は、公式 Amethyst プロジェクトを基に一から再構築した、iOS・iPadOS 向けの Minecraft: Java Edition ランチャーです。包括的な Mod 管理、最適なレンダラーの自動選択、iOS に合わせた深いプラットフォーム統合により、洗練されたモバイル体験を提供します。

---

## 目次

- [主な機能](#主な機能)
- [はじめに](#はじめに)
  - [対応デバイス](#対応デバイス)
  - [サイドロードの準備](#サイドロードの準備)
  - [インストール](#インストール)
  - [JIT を有効にする](#jit-を有効にする)
- [貢献者](#貢献者)
- [翻訳について](#翻訳について)
- [サードパーティーコンポーネント](#サードパーティーコンポーネント)
- [支援](#支援)

## 主な機能

- **モダンな UI** — 現代的で見やすい操作感を目指して、インターフェースを大幅に刷新しました。
- **リソース管理とダウンロード** — Mod、シェーダーパック、リソースパックなどを一覧・有効化・無効化・削除でき、Modrinth と CurseForge から直接ダウンロードできます。
- **Modパックのインポート** — ZIP 形式の Modパックをランチャーから直接インポートできます。
- **スマートなダウンロード元** — Mojang 公式、BMCLAPI ミラーなどを切り替え、通信環境に応じてダウンロード速度を最適化できます。
- **日本語・中国語を含む多言語対応** — 設定から表示言語を切り替えられ、日本語が既定で選択されています。
- **アカウントの制限なし** — ローカルアカウント、デモモード、サードパーティー認証に対応。ゲームのダウンロードとプレイに Microsoft アカウントは必須ではありません。
- **複数アカウント** — Microsoft、ローカル、サードパーティー認証のアカウントをシームレスに切り替えられます。
- **レンダラー自動選択** — Auto 設定時は、MobileGlues、MoltenVK などを含む最適な描画バックエンドを自動的に選択します。
- **Java の自動選択** — ゲームのバージョンに合わせて Java 8、17、21、25 を自動選択します。
- **Minecraft 26.x 対応** — Minecraft 26.x を実験的にサポートしています。
- **カスタムマウスポインター** — 設定からゲーム内の仮想マウスポインター画像を変更できます。
- **カスタムニュース URL** — ランチャーのホーム画面で表示するニュースフィードの URL を設定できます。
- **TouchController 対応** — UDP ローカルプロキシと XCFramework を通じて TouchController Mod と連携し、iOS で完全なタッチ操作を提供します。
- **AI 統合** — 開発中。リソースのダウンロードやインスタンス管理などを AI が補助できるようにする予定です。
- **カスタムアプリアイコン** — 開発中。

さらに多くの機能を用意しています。

> [!NOTE]
> このリマスター版を Android に移植する予定はありません。Android には [Zalith Launcher](https://github.com/ZalithLauncher/ZalithLauncher)、[Fold Craft Launcher](https://github.com/FCL-Team/FoldCraftLauncher)、ShardLauncher など、優れたランチャーがあります。公式 Android 版は [Amethyst-Android](https://github.com/AngelAuraMC/Amethyst-Android) を参照してください。

## はじめに

詳細な手順は [Amethyst 公式 Wiki](https://wiki.angelauramc.dev/wiki/getting_started/INSTALL.html#ios) または [Bilibili のチュートリアル](https://b23.tv/KyxZr12) を参照してください。以下は簡易ガイドです。

### 対応デバイス

| 区分 | iOS バージョン | 対応デバイス |
|------|-------------|-------------------|
| **最低要件** | iOS 14.0 以降 | iPhone 6s 以降、iPad 第5世代以降、iPad Air 2 以降、iPad mini 4 以降、すべての iPad Pro、iPod touch 第7世代 |
| **推奨** | iOS 14.5 以降 | iPhone XS 以降（XR・第2世代 SE を除く）、iPad 第10世代以降、iPad Air 第4世代以降、iPad mini 第6世代以降、iPad Pro（9.7インチを除く） |

> [!CAUTION]
> iOS 14.0〜14.4.2 には重大な互換性上の問題があります。**iOS 14.5 以降へのアップデートを強く推奨します。** iOS 17.x・18.x はサポートされていますが、初回の JIT 設定にはコンパニオンコンピューターが必要です（[公式 JIT ガイド](https://wiki.angelauramc.dev/wiki/faq/ios/JIT.html#what-are-the-methods-to-enable-jit)を参照）。iOS 26.x にはインストールできますが、専用の最適化は行われていないため、予期しない挙動が発生する場合があります。

### サイドロードの準備

永続署名と JIT 自動有効化に対応するツールを優先してください。

1. **TrollStore**（推奨）— 永続署名、JIT の自動有効化、メモリ上限の拡張に対応します。一部の iOS バージョンで利用できます。[公式リポジトリから入手](https://github.com/opa334/TrollStore)
2. **AltStore / SideStore**（代替手段）— 定期的な再署名が必要です。初期設定にはコンピューターと Wi-Fi が必要で、**開発用証明書**（JIT には `com.apple.security.get-task-allow` エンタイトルメントが必要）にのみ対応します。配布用証明書の署名サービスは利用できません。

> [!WARNING]
> サイドロードツールと IPA は、公式または信頼できる配布元からのみ入手してください。非公式ソフトウェアの使用により発生したデバイスの問題について、作者は責任を負いません。脱獄端末では永続署名が可能ですが、日常的に使用する端末の脱獄は推奨しません。

### インストール

<details>
<summary><b>正式リリース（TrollStore）</b></summary>

1. [Releases](https://github.com/386612/Amethyst-JP/releases) から `.tipa` パッケージをダウンロードします。
2. iOS の共有メニューで TrollStore を選択して開くと、インストールが完了します。
</details>

<details>
<summary><b>正式リリース（AltStore / SideStore）</b></summary>

1. [Releases](https://github.com/386612/Amethyst-JP/releases) から `.ipa` パッケージをダウンロードします。
2. 使用するサイドロードツールの通常の手順に従って IPA を読み込み、インストールします。
</details>

<details>
<summary><b>Nightly ビルド（開発・テスト用）</b></summary>

> [!CAUTION]
> Nightly ビルドには、クラッシュや起動失敗などの重大な不具合が含まれる可能性があります。開発およびテスト目的でのみ使用してください。

1. [GitHub Actions](https://github.com/386612/Amethyst-JP/actions) から最新の IPA アーティファクトをダウンロードします。
2. AltStore、SideStore などのサイドロードツールに IPA を読み込んでインストールします。
</details>

### JIT を有効にする

JIT（Just-In-Time コンパイル）は、快適にプレイするために不可欠です。利用環境に合った方法を選んでください。

| ツール | 外部デバイス | Wi-Fi | 自動有効化 | 備考 |
|------|:---:|:---:|:---:|-------|
| TrollStore | 不要 | 不要 | 対応 | 最優先。追加操作は不要です。 |
| AltStore | 必要 | 必要 | 対応 | ローカルネットワーク上で AltServer を実行する必要があります。 |
| SideStore | 初回のみ | 初回のみ | 非対応 | 初期設定後はデバイス・ネットワーク不要です。 |
| StikDebug | 初回のみ | 初回のみ | 対応 | 初期設定後はデバイス・ネットワーク不要です。 |
| Jitterbug | 必要（VPN なしの場合） | 必要 | 非対応 | 手動で有効化する必要があります。 |
| 脱獄端末 | 不要 | 不要 | 対応 | システムレベルで自動的にサポートされます。 |

## 貢献者

- [@yitenchen123](https://github.com/yitenchen123) — プロジェクトメンテナー
- [@EternityQwQ](https://github.com/EternityQwQ) — Metal Universal Mod 対応を追加し、Metal で Minecraft を描画できるようにしました
- [@LanRhyme](https://github.com/LanRhyme) — iOS 26 対応とログ機能の改善
- [@WeiErLiTeo](https://github.com/WeiErLiTeo) — Mod ダウンロード統合、TouchController 最適化、2本指長押しによるキーボード呼び出し
- [@Li2548](https://github.com/Li2548) — 上流との同期
- [@Gsjsjzhznsz](https://github.com/Gsjsjzhznsz) — SDL3 の表示対応、Minecraft 26.3 の黒画面・解像度自動復旧の修正、MobileGlues のデッドロック修正、Zink OpenGL ブリッジ

## 翻訳について

翻訳への協力は [Crowdin](https://crowdin.com/project/amethyst-ios-remastered) からお願いします。

## サードパーティーコンポーネント

| コンポーネント | 用途 | ライセンス | ソース |
|-----------|---------|---------|--------|
| Caciocavallo | AWT ランタイムフレームワーク | GPL-2.0 | [GitHub](https://github.com/PojavLauncherTeam/caciocavallo) |
| jsr305 | コード注釈のサポート | BSD-3 | [Google Code](https://code.google.com/p/jsr-305) |
| Boardwalk | コア機能の適応 | Apache-2.0 | [GitHub](https://github.com/zhuowei/Boardwalk) |
| GL4ES | OpenGL から GLES への変換 | MIT | [GitHub](https://github.com/ptitSeb/gl4es) |
| Mesa 3D | 3D グラフィックスライブラリ | MIT | [GitLab](https://gitlab.freedesktop.org/mesa/mesa) |
| MetalANGLE | Metal から OpenGL ES への変換 | BSD-2 | [GitHub](https://github.com/khanhduytran0/metalangle) |
| MoltenVK | Vulkan から Metal への変換 | Apache-2.0 | [GitHub](https://github.com/KhronosGroup/MoltenVK) |
| openal-soft | クロスプラットフォームの音声ライブラリ | LGPL-2.0 | [GitHub](https://github.com/kcat/openal-soft) |
| Azul Zulu JDK | Java ランタイム（8/17/21/25） | GPL-2.0 | [公式サイト](https://www.azul.com/downloads/?package=jdk) |
| LWJGL3 | Java ゲーム開発ライブラリ | BSD-3 | [GitHub](https://github.com/PojavLauncherTeam/lwjgl3) |
| LWJGLX | LWJGL2 互換レイヤー | — | [GitHub](https://github.com/PojavLauncherTeam/lwjglx) |
| DBNumberedSlider | UI スライダーコントロール | Apache-2.0 | [GitHub](https://github.com/khanhduytran0/DBNumberedSlider) |
| fishhook | 動的ライブラリの再バインド | BSD-3 | [GitHub](https://github.com/facebook/fishhook) |
| shaderc | シェーダーコンパイラー | Apache-2.0 | [GitHub](https://github.com/google/shaderc) |
| NRFileManager | ファイル管理ユーティリティ | MPL-2.0 | [GitHub](https://github.com/mozilla-mobile/firefox-ios) |
| AltKit | AltStore 統合 | — | [GitHub](https://github.com/rileytestut/AltKit) |
| UnzipKit | ZIP 解凍処理 | BSD-2 | [GitHub](https://github.com/abbeycode/UnzipKit) |
| DyldDeNeuralyzer | ライブラリ検証の回避 | — | [GitHub](https://github.com/xpn/DyldDeNeuralyzer) |
| MobileGlues | サードパーティー製レンダラー | LGPL-2.1 | [GitHub](https://github.com/MobileGL-Dev/MobileGlues) |
| LTW | OpenGL Core から ES へのラッパー | LGPL-3.0 | [GitHub](https://github.com/MojoLauncher/LTW) |
| authlib-injector | サードパーティー認証のサポート | AGPL-3.0 | [GitHub](https://github.com/yushijinhun/authlib-injector) |

さらに、Minecraft アバターサービスを提供する [MCHeads](https://mc-heads.net)、Mod 配信の [Modrinth](https://modrinth.com)、Minecraft ダウンロードミラーの [BMCLAPI](https://bmclapidoc.bangbang93.com) に感謝します。

## 支援

このプロジェクトが役に立った場合は、[Ko-fi](https://ko-fi.com/herbrine8403)、[愛発電](https://afdian.com/a/herbrine8403)、または [WeChat 支援コード](donate.png) から開発支援をご検討ください。
