# VoiceBridge — プロジェクト状況（ライブ状態ファイル）

**最終更新: 2026-06-29**

> このファイルは「持ち運べるプロジェクトの記憶」です。
> 別のチャットやチャンネル（Discord・別のClaude・ChatGPT等）に貼ると、
> 相手が現状を認識して**続きから**作業できます。
> 呼び出し方は [`SUMMON.md`](./SUMMON.md)（おまじない）を参照。
> Web版: https://alame.pages.dev/STATUS.md

---

## 🎯 プロジェクトの正体

言語の違う相手とコミュニケーションを取るための **リアルタイム音声翻訳ツール「VoiceBridge」**。
最終的には VRChat のアバターが自分の代わりに同時通訳で話す構想で、その**共通エンジン（話す→認識→翻訳→出力）**を作っている。

- リポジトリ: `mayura121/alame`
- 開発ブランチ: `claude/avatar-translation-system-kcwzsf`
- 本番: `main`（Cloudflare Pages → https://alame.pages.dev ）

---

## ✅ 現在のステータス

| 項目 | 状態 |
|---|---|
| VoiceBridge MVP | **完成・mainにマージ済み（PR #1, merged）** |
| ライブURL | https://alame.pages.dev/translate/ |
| CI (Cloudflare Pages) | ✅ グリーン |
| 既存のめざまし時計アプリ | そのまま稼働（https://alame.pages.dev/ ） |

---

## 🧩 完成している機能（MVP）

- 🎤 **話す → 認識 → 翻訳 → 画面表示＋読み上げ**（コアの通訳ループ）
- 👫 2言語モード（「あなた」「相手」を選んで話者切替）、🌏 16言語対応
- 🖥️ 提示モード（翻訳を大画面表示。相手に見せる／配信に重ねる用）
- ⌨️ 文字入力フォールバック（マイク非対応のSafari/Firefox向け）
- 🔁 連続認識、🔊 読み上げON/OFF、言語入れ替え
- 📱 PWA（ホーム画面追加・オフラインUI）

---

## 🏗️ アーキテクチャ（重要）

- 単一HTML（`translate/index.html`）にCSS/JSインライン。依存ライブラリなし。
- 音声認識 = Web Speech API（Chrome/Edgeで安定）。
- 翻訳 = `translate(text, from, to)` の**1関数に集約＝差し替え可能**。
  - 既定: **MyMemory**（無料・キー不要・CORS対応）
  - 設定でカスタムサーバーに切替可（`POST {text, from, to}` → `{translatedText}`）
  - ここをサーバー化すれば「Claude/AIの再配布問題」を回避できる（キーはサーバー側に隠す）。

---

## 🗺️ ロードマップと次の一手

1. **通訳ツール（VoiceBridge）** ← ✅ いまここ（土台完成）
2. 配信オーバーレイ：翻訳テロップを Discord / OBS に重ねる
3. VRChat アバター連携：自分の発話をアバターが同時通訳で代弁（OSC経由）
4. ペット／追従アイテムへの AI＋翻訳プラグイン

**おすすめの次の一手 →** ②の前に **翻訳の自前サーバー化**（Cloudflare Worker等）。
品質UP＋キー秘匿ができ、③④の土台にもなる。

### 未確認・宿題
- 実ブラウザでの「話す→翻訳」動作の実機確認（開発環境からは翻訳APIが叩けず未検証）。
- 既定エンジン MyMemory は無料ゆえ品質は割り切り（差し替え前提）。

---

## 🤖 このプロジェクトを引き継ぐAIへの指示

あなたは「VoiceBridge」プロジェクトの開発パートナーです。上記の状況を前提に、
ユーザーの次の指示に対して**続きから**動いてください。実装するなら開発ブランチ
`claude/avatar-translation-system-kcwzsf` で作業し、勝手にPRを作らないこと。

---

## 📦 状態ブロック（機械可読・コピペ用）

```
=== VOICEBRIDGE STATE v1 ===
project: VoiceBridge (real-time voice translation -> future VRChat avatar interpreter)
repo: mayura121/alame
dev_branch: claude/avatar-translation-system-kcwzsf
live: https://alame.pages.dev/translate/
status: MVP merged to main (PR#1), CI green
engine: pluggable translate(text,from,to); default=MyMemory(free); custom server supported
features: STT(WebSpeech)->translate->TTS, 2-lang mode, 16 langs, presentation mode, text fallback, PWA
roadmap: 1.tool(done) 2.stream-overlay(Discord/OBS) 3.VRChat-avatar(OSC) 4.pet/item AI+translate plugin
next: self-hosted translation backend (Cloudflare Worker) for quality + key secrecy
updated: 2026-06-29
=== END ===
```
