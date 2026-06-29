# 🪄 おまじない — VoiceBridge 召喚

別のチャット／チャンネル（Discord・新しいClaude・ChatGPT など）に貼ると、
相手が **VoiceBridge の現状を認識して続きから動ける** ようにするための合言葉集です。

仕組みはシンプル：「状況」は [`STATUS.md`](./STATUS.md) に置いてあり、
おまじないはそれを**読み込ませる／持ち込む**ための呪文です。

---

## ① 短い呪文 ―「ブリッジ、ひらけ」🌉

リポジトリやWebを読めるAI（Claude Code・このセッション等）向け。
*開けゴマ* のノリで、これを送るだけ：

```
ブリッジ、ひらけ
（= https://alame.pages.dev/STATUS.md を読んで、VoiceBridgeの現状を要約し、続きから始めて）
```

> 短縮形だけでも通じるよう、相手AIには「ブリッジ、ひらけ＝STATUS.mdを読んで続行」と解釈させます。

---

## ② 完全版おまじない ―「どこでも一発」📋

Web もリポジトリも読めない相手（ただのチャット、Discordの素のbot等）向け。
**この囲みの中をまるごとコピペ**すれば、それ単体で状況が伝わります。

```
🪄 VoiceBridge 召喚 — このブロックを読んで、プロジェクトの現状を把握し、続きから開発パートナーとして動いてください。

=== VOICEBRIDGE STATE v1 ===
project: VoiceBridge（リアルタイム音声翻訳ツール。将来はVRChatアバターが同時通訳で代弁する構想の共通エンジン）
repo: mayura121/alame ／ dev_branch: claude/avatar-translation-system-kcwzsf
live: https://alame.pages.dev/translate/
status: MVP完成・mainにマージ済み（PR#1 merged）／ CI(Cloudflare Pages)グリーン
engine: 翻訳は translate(text,from,to) の1関数に集約＝差し替え可能。既定=MyMemory(無料/キー不要)、カスタムサーバー対応
features: 音声認識(Web Speech)→翻訳→読み上げ／2言語モード・話者切替／16言語／提示モード(大画面)／文字入力フォールバック／PWA
roadmap: ①通訳ツール(完成) → ②配信オーバーレイ(Discord/OBS) → ③VRChatアバター連携(OSC) → ④ペット/追従アイテムへのAI＋翻訳プラグイン
next: 翻訳の自前サーバー化(Cloudflare Worker等)で品質UP＆APIキー秘匿
=== END ===

指示: 上を前提に、次のメッセージから「続き」として対応して。実装時は dev_branch で作業し、勝手にPRは作らないこと。最新の詳細は https://alame.pages.dev/STATUS.md にある。
```

---

## ③ Discord 用ミニ報告（共有したいだけのとき）

```
🌉 VoiceBridge 進捗：リアルタイム音声翻訳ツールが完成＆公開！
→ https://alame.pages.dev/translate/  （Chrome/Edge推奨・インストール不要）
話す→翻訳→読み上げ／16言語／提示モードで大画面表示。次は翻訳サーバー自前化。
状況の全文＆おまじない: https://alame.pages.dev/STATUS.md
```

---

## 使い分け早見表

| 貼る相手 | 使うおまじない |
|---|---|
| Claude Code / Web等（リポジトリ・URL読める） | ① ブリッジ、ひらけ |
| 素のチャット・Discord bot（何も読めない） | ② 完全版（ブロックごとコピペ） |
| ただ共有・報告したい | ③ ミニ報告 |

> 状況が進んだら `STATUS.md` を更新すれば、おまじないは同じものを使い回せます。
> （`STATUS.md` がプロジェクトの「最新の記憶」、`SUMMON.md` がその「呼び出し方」）
