<div align="center">
  <img src="Natives/Assets.xcassets/AppIcon-Light.appiconset/1024x1024.png" alt="空気アイコン" width="120" style="border-radius: 24px;">
</div>

<h1 align="center">空気</h1>
<p align="center"><sub>アメジスト iOS リマスター</sub></p>

<div align="center">
  <img alt="ビルド ステータス" src="https://github.com/herbrine8403/Amethyst-iOS-MyRemastered/actions/workflows/development.yml/badge.svg?branch=main">
  <img alt="ダウンロード" src="https://img.shields.io/github/downloads/herbrine8403/Amethyst-iOS-MyRemastered/total?label=Downloads&style= flat">
  <img alt="リリース" src="https://img.shields.io/github/v/release/herbrine8403/Amethyst-iOS-MyRemastered?style= flat">
  <img alt="ライセンス" src="https://img.shields.io/github/license/herbrine8403/Amethyst-iOS-MyRemastered?style= flat">
  <a title="Crowdin" target="_blank" href="https://crowdin.com/project/amethyst-ios-remastered"><img alt="Crowdin" src="https://badges.crowdin.net/amethyst-ios-remastered/localized.svg">
</div>

<p align="center">
  <a href="./README.md">英語</a> | <a href="./README_CN.md">中国語</a>
</p>

> [!重要]
> **これは唯一の公式 Air リポジトリです:** [herbrine8403/Amethyst-iOS-MyRemastered](https://github.com/herbrine8403/Amethyst-iOS-MyRemastered)。
> 「Air」名を使用した非公式のフォークやミラー リポジトリに注意してください。リポジトリの所有者が [@herbrine8403](https://github.com/herbrine8403) であり、URL が上記のリンクと一致していることを常に確認してください。

---

公式 Amethyst プロジェクトに基づいて一から再構築された、iOS および iPadOS 用のプレミアム Minecraft: Java Edition ランチャー。包括的な MOD 管理、インテリジェントなレンダラーの選択、および緊密なプラットフォーム統合により、洗練されたモバイル エクスペリエンスを提供します。

---

## 目次

- [コア機能](#core-features)
- [クイックスタート](#quick-start)
  - [デバイス要件](#device-requirements)
  - [サイドロードの準備](#sideload-preparation)
  - [インストール](#installation)
  - [JIT を有効にする](#enable-jit)
- [寄稿者](#contributors)
- [サードパーティ コンポーネント](#third-party-components)
- [スポンサー](#スポンサー)

## コア機能

- **最新の UI 再設計** -- インターフェイスは、現代的で洗練されたビジュアル スタイルに合わせて大幅に改良されました。
- **リソース管理とダウンロード** -- 統合された Modrinth および CurseForge ダウンロード サポートを使用して、MOD、シェーダー パック、リソース パック、その他のアセットを参照、有効化、無効化、および削除します。
- **Modpack Import** -- ZIP 形式の Modpack をランチャー インターフェイスから直接インポートします。
- **スマート ダウンロード ソース** -- Mojang 公式、BMCLAPI ミラー、その他のソースをその場で切り替えて、最適なダウンロード速度を実現します。
- **完全な中国語ローカライズ** -- ネイティブ品質の中国語サポートを備えた完全に翻訳されたインターフェイス。
- **無制限のアカウント** -- ローカル アカウント、デモ モード、サードパーティ認証がすべてサポートされています。ダウンロードしてプレイするために Microsoft アカウントは必要ありません。
- **マルチアカウント** -- Microsoft、ローカル、サードパーティの認証アカウントをシームレスに切り替えます。
- **自動レンダラー選択** -- 自動に設定すると、最適なレンダリング バックエンド (MobileGlues、MoltenVK などを含む) が自動的に選択されます。
- **自動 JVM 選択** -- ゲームのバージョンに基づいて、正しい JVM バージョン (Java 8、17、21、または 25) を自動的に選択します。
- **Minecraft 26.X サポート** -- Minecraft 26.x の実験的サポート。
- **カスタム マウス ポインター** -- 設定で仮想マウス ポインターのスキンをカスタマイズします。
- **カスタム ニュース URL** -- ランチャー ホーム画面のカスタム ニュース フィード URL を構成します。
- **TouchController サポート** -- UDP ローカル プロキシと XCFramework の両方を介して TouchController Mod と通信し、iOS 上で完全なタッチスクリーン コントロールを提供します。
- **AI 統合** -- (開発中) 目標は、AI がリソースのダウンロードやインスタンス管理を含むランチャーを完全に管理できるようにすることです。
- **カスタム アプリ アイコン** -- (開発中)

...その他にも探索すべきことがたくさんあります。

> [!NOTE]
> このリマスター版を Android に移植する予定はありません。のAndroid エコシステムには、[Zalith Launcher](https://github.com/ZalithLauncher/ZalithLauncher)、[Fold Craft Launcher](https://github.com/FCL-Team/FoldCraftLauncher)、ShardLauncher などの優れたランチャーがすでにあります。 Android の公式バージョンについては、[Amethyst-Android](https://github.com/AngelAuraMC/Amethyst-Android) にアクセスしてください。

## クイックスタート

完全なドキュメントについては、[Amethyst 公式 Wiki](https://wiki.angelauramc.dev/wiki/getting_started/INSTALL.html#ios) または [Bilibili チュートリアル](https://b23.tv/KyxZr12) を参照してください。以下は要約されたガイドです。

### デバイス要件

|階層 | iOS バージョン |サポートされているデバイス |
|------|-------------|--------|
| **最小値** | iOS 14.0以降 | iPhone 6s 以降、iPad 第 5 世代以降、iPad Air 2 以降、iPad mini 4 以降、すべての iPad Pro、iPod touch 第 7 世代 |
| **推奨** | iOS 14.5以降 | iPhone XS+ (XR/SE 第 2 世代を除く)、iPad 第 10 世代以降、iPad Air 第 4 世代以降、iPad mini 第 6 世代以降、iPad Pro (9.7 インチを除く) |

> [!注意]
> iOS 14.0--14.4.2 には既知の重大な互換性の問題があります。 **iOS 14.5 以降にアップグレードすることを強くお勧めします。** iOS 17.x および 18.x はサポートされていますが、初期 JIT 構成にはコンパニオン コンピューターが必要です ([公式 JIT ガイド](https://wiki.angelauramc.dev/wiki/faq/ios/JIT.html#what-are-the-methods-to-enable-jit) を参照)。 iOS 26.x はインストール可能ですが、専用の適応は行われていません。予測できない動作が予想されます。

### サイドロードの準備

永久署名と自動 JIT 有効化をサポートするツールを優先します。

1. **TrollStore** *(推奨)* -- 永久署名、自動 JIT、メモリ制限の増加。一部の iOS バージョンと互換性があります。 [公式リポジトリからダウンロード](https://github.com/opa334/TrollStore)
2. **AltStore / SideStore** *(代替)* -- 定期的な再署名が必要です。初期設定にはパソコンとWi-Fiが必要です。 **開発証明書**とのみ互換性があります (JIT の `com.apple.security.get-task-allow` 資格を含める必要があります)。配布証明書署名サービスはサポートされていません。

> [!警告]
> サイドローディング ツールと IPA ファイルは、公式または信頼できるソースからのみダウンロードしてください。作者は、非公式ソフトウェアによって引き起こされたデバイスの問題については責任を負いません。ジェイルブレイクされたデバイスは永久署名をサポートしますが、毎日のドライバーのジェイルブレイクは推奨されません。

### インストール

<詳細>
<summary><b>正式リリース (TrollStore)</b></summary>

1. [リリース](https://github.com/herbrine8403/Amethyst-iOS-MyRemastered/releases) から `.tipa` パッケージをダウンロードします。
2. システム共有メニューから TrollStore でファイルを開き、インストールを完了します。
</詳細>

<詳細>
<summary><b>正式リリース (AltStore / SideStore)</b></summary>

1. [リリース](https://github.com/herbrine8403/Amethyst-iOS-MyRemastered/releases) から `.ipa` パッケージをダウンロードします。
2. 標準のインストール手順に従って、IPA をサイドローディング ツールにインポートします。
</詳細>

<詳細>
<summary><b>夜間ビルド (開発テスト)</b></summary>

> [!注意]
> Nightly ビルドには、クラッシュや起動失敗などの重大なバグが含まれる可能性があります。開発およびテストの目的でのみ使用してください。

1. [GitHub Actions](https://github.com/herbrine8403/Amethyst-iOS-MyRemastered/actions) ページに移動し、最新の IPA アーティファクトをダウンロードします。
2. IPA をサイドローディング ツール (AltStore、SideStore など) にインポートしてインストールします。
</詳細>

### JIT の有効化

JIT (Just-In-Time コンパイル) は、スムーズなゲームプレイに不可欠です。環境に合ったアプローチを選択してください。

|ツール |外部デバイス | Wi-Fi が必要 |自動有効化 |メモ |
|------|:---:|:---:|:---:|------|
|トロールストア |いいえ |いいえ |はい |好ましい。追加のアクションは必要ありません。
|オルタナティブストア |はい |はい |はい |ローカル ネットワーク上で AltServer が実行されている必要があります |
|サイドストア |初回のみ |初回のみ |いいえ |初期セットアップ後はデバイス/ネットワーク不要 |
|スティックデバッグ |初回のみ |初回のみ |はい |初期セットアップ後はデバイス/ネットワーク不要 |
|ジッターバグ |はい (VPN なし) |はい |いいえ |手動トリガーが必要 |
|脱獄 |いいえ |いいえ |はい|システムレベルの自動サポート |

## 貢献者

- [@yitenchen123](https://github.com/yitenchen123) -- プロジェクト管理者
- [@EternityQwQ](https://github.com/EternityQwQ) -- Metal Universal Mod サポートを追加し、ランチャーが Minecraft のレンダリングに Metal を使用できるようにします。
- [@LanRhyme](https://github.com/LanRhyme) -- ShardLauncher 作者。 iOS 26の互換性とログの改善
- [@WeiErLiTeo](https://github.com/WeiErLiTeo) -- Mod ダウンロードの統合、TouchController の最適化、2 本指の長押しキーボード トリガー
- [@Li2548](https://github.com/Li2548) -- アップストリーム同期
- [@Gsjsjzhznsz](https://github.com/Gsjsjzhznsz) -- SDL3 プレゼンテーションの適応、Minecraft 26.3 のブラック スクリーン (FBO0 ヒール ブリット) と解像度の自己修復の修正、MobileGlues のデッドロックの修正、Zink OpenGL ブリッジ

## 翻訳について

このプロジェクトの翻訳に貢献したい場合は、[Crowdin](https://crowdin.com/project/amethyst-ios-remastered) にアクセスしてください。

## サードパーティ製コンポーネント

|コンポーネント |目的 |ライセンス |出典 |
|----------|----------|----------|----------|
|カチョカヴァロ | AWT ランタイム フレームワーク | GPL-2.0 | [GitHub](https://github.com/PojavLauncherTeam/caciocavallo) |
| jsr305 |コード注釈のサポート | BSD-3 | [Google コード](https://code.google.com/p/jsr-305) |
|ボードウォーク |コア機能の適応 | Apache-2.0 | [GitHub](https://github.com/zhuowei/Boardwalk) |
| GL4ES | OpenGL から GLES への変換 |マサチューセッツ工科大学 | [GitHub](https://github.com/ptitSeb/gl4es) |
|メサ3D | 3Dグラフィックスライブラリ |マサチューセッツ工科大学 | [GitLab](https://gitlab.freedesktop.org/mesa/mesa) |
|メタルアングル | Metal から OpenGL ES への変換 | BSD-2 | [GitHub](https://github.com/khanhduytran0/metalangle) |
|モルテンVK |バルカンからメタルへの変換 | Apache-2.0 | [GitHub](https://github.com/KhronosGroup/MoltenVK) |
|オープナルソフト |クロスプラットフォーム 3D オーディオ | LGPL-2.0 | [GitHub](https://github.com/kcat/openal-soft) |
|アズール・ズールーJDK | Java ランタイム (8/17/21/25) | GPL-2.0 | [ウェブサイト](https://www.azul.com/downloads/?package=jdk) |
| LWJGL3 | Java ゲーム開発ライブラリ | BSD-3 | [GitHub](https://github.com/PojavLauncherTeam/lwjgl3) |
| LWJGLX | LWJGL2 互換性レイヤー | -- | [GitHub](https://github.com/PojavLauncherTeam/lwjglx) |
| DB番号付きスライダー | UIスライダーコントロール | Apache-2.0 | [GitHub](https://github.com/khanhduytran0/DBNumberedSlider) |
|釣り針動的ライブラリの再バインド | BSD-3 | [GitHub](https://github.com/khanhduytran0/fishhook) |
|シェーダー | Vulkan シェーダーのコンパイル | Apache-2.0 | [GitHub](https://github.com/khanhduytran0/shaderc) |
| NRファイルマネージャー |ファイル管理ユーティリティ | MPL-2.0 | [GitHub](https://github.com/mozilla-mobile/firefox-ios) |
|オルトキット | AltStore の統合 | -- | [GitHub](https://github.com/rileytestut/AltKit) |
|解凍キット | ZIP アーカイブの処理 | BSD-2 | [GitHub](https://github.com/abbeycode/UnzipKit) |
|ディルドデニューラライザー |ライブラリ検証バイパス | -- | [GitHub](https://github.com/xpn/DyldDeNeuralyzer) |
|モバイルグルー |サードパーティのレンダラー | LGPL-2.1 | [GitHub](https://github.com/MobileGL-Dev/MobileGlues) |
| LTW | OpenGL Core-to-ES ラッパー | LGPL-3.0 | [GitHub](https://github.com/MojoLauncher/LTW) |
| authlib-インジェクター |サードパーティ認証 | AGPL-3.0 | [GitHub](https://github.com/yushijinhun/authlib-injector) |

さらに、Minecraft アバター サービスの [MCHeads](https://mc-heads.net)、MOD 配布の [Modrinth](https://modrinth.com)、Minecraft ダウンロード ミラーリングの [BMCLAPI](https://bmclapidoc.bangbang93.com) に感謝します。

## スポンサー

このプロジェクトに価値があると思われる場合は、[Ko-Fi](https://ko-fi.com/herbrine8403)、[Afdian](https://afdian.com/a/herbrine8403)、または [WeChat 報酬コード](donate.png) を通じて開発をサポートすることを検討してください。

## スターの歴史

<a href="https://www.star-history.com/?type=date&repos=herbrine8403%2FAmethyst-iOS-MyRemastered">
 <写真>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=herbrine8403/Amethyst-iOS-MyRemastered&type=date&theme=dark&legend=top-left&sealed_token=q1uFKbS7fO8owrcjy_kYTkCnnl8PNgHAgBSrWop8Y3ULDdvwOwDfORslSVVXABSTwrsdu14OM3fshRaNbXouxMU5IenXF0T5r5L6rxKIN2n29T6Fv4UYyA" />
   <ソースメディア="(カラースキームを優先: ライト)" srcset="https://api.star-history.com/chart?repos=herbrine8403/Amethyst-iOS-MyRemastered&type=date&legend=top-left&sealed_to ken=q1uFKbS7fO8owrcjy_kYTkCnnl8PNgHAgBSrWop8Y3ULDdvwOwDfORslSVVXABSTwrsdu14OM3fshRaNbXouxMU5IenXF0T5r5L6rxKIN2n29T6Fv4UYyA" />
   <img alt="スターの歴史グラフ" src="https://api.star-history.com/chart?repos=herbrine8403/Amethyst-iOS-MyRemastered&type=date&legend=top-left&sealed_tok en=q1uFKbS7fO8owrcjy_kYTkCnnl8PNgHAgBSrWop8Y3ULDdvwOwDfORslSVVXABSTwrsdu14OM3fshRaNbXouxMU5IenXF0T5r5L6rxKIN2n29T6Fv4UYyA" />
 </ピクチャ>
</a>