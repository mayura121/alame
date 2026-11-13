# alame プロジェクト メモリ

このファイルはセッションをまたいで作業内容を共有するためのメモです。
別のセッション（PC接続）でも、最新を `git pull` してからこの内容を前提に作業してください。

## おまじない（合言葉）

> **「紅茶の部屋で、めざましの一杯を」**

別セッションでこの合言葉が出てきたら、「このCLAUDE.mdを読んで現在の進行状況を把握し、続きから作業する」という意味です。
このおまじないを唱えたら、まず `git fetch && git status` で最新状態を確認してください。

## プロジェクト概要

- **alame.pages.dev** … Cloudflare Pages でホストされている静的サイト
- もともとは **めざまし時計（PWAアラームアプリ）** の単一ページ
- 管理人は **紅茶アドバイザー・紅茶マイスター** の有資格者。サイト内に紅茶コラム「紅茶の部屋」を併設中

## サイト構成

| パス | 内容 |
|---|---|
| `/` (`index.html`) | めざまし時計アプリ（PWA・Web Audio・localStorage） |
| `/tea/` (`tea/index.html`) | 紅茶の部屋トップ（プロフィール＋記事一覧、ブログ型）。記事は `tea/*.html` に10本（ゴールデンルール・ダージリン・ミルクティー・アイスティー・チャイ・茶葉の種類・ティーポット選び・保存・健康・食べ合わせ・アフタヌーンティー） |
| `/coffee/` (`coffee/index.html`) | コーヒーの部屋（トップ＋記事10本、2026-06-27 作成） |
| `/translate/` | リアルタイム音声翻訳ツール VoiceBridge（2026-06-29、PR #1） |
| `sw.js` | Service Worker（キャッシュ。現在 `mezamashi-v6`。ページを足したり共通部分を変えたら名前を1つ上げる） |
| `manifest.json` / `icon-*.svg` | PWA関連 |

- GitHub は `mayura121/alame`（フォルダ名 `alarm-app` と違う。push 先を間違えると "Repository not found"）。`main` に push すると Cloudflare Pages が約1分で反映
- Cloudflare Pages は `.html` 付き URL を 308 で拡張子なしに転送する（`/tea/golden-rule.html` → `/tea/golden-rule`）。curl で確認するときは `-L`
- 全25ページの `</body>` 直前に「ちゃんまゆのリンク帯」`<nav class="cm-band">`（BOOTH・note・X・MAYUYU.c・VRC運動部・VRChat ラボ）がある（2026-11-10、4サイト共通。X は工房の @ChanmayuKobo、2026-11-13 にまゆさんの指示で個人 @mayura0121 から変更。文言は `E:\ClaudeProjects\web-hq\CLAUDE.md`）。CSS は各ページの `<style>` 内。ページを足すときは同じ帯を入れる
- robots.txt・sitemap.xml・404.html はまだ無い（2026-11-10 時点。Search Console 登録のときに足す）

## デザイン方針

- **めざまし時計**：寒色（青紫）グラデ＋ガラスカード（glassmorphism）、サンセリフ
- **紅茶の部屋**：暖色（琥珀・ブラウン）グラデ＋同じガラスカード、明朝体ベース
- 両者はガラスカードのデザイン言語を共有。CSS変数（`--accent` 等）でトーンを切り替え
- めざまし時計トップ下部に `☕ 紅茶の部屋` への導線リンクあり

## 作業ブランチ

- 2026-11-06 に開発ブランチ `claude/remote-control-vc73na` を `main` にマージ（`bcb5848`）し、紅茶の部屋・コーヒーの部屋を本番公開済み。以後は `main` で作業する
- リモートに古いブランチ `claude/avatar-translation-system-kcwzsf`（6-29、STATUS/SUMMON の文書だけ）が残っている。main より古いので使わない（削除はまゆさんに確認）
- 記事の変更・追加は本社（`E:\ClaudeProjects\ai-company`）に相談してから。解説動画（YouTube「まゆゆ軍団」）の誘導先がこのサイト
- 親: ウェブサイト司令塔（決まりは `E:\ClaudeProjects\web-hq\CLAUDE.md`）

## これまでの進行状況（〜2026-06-26。歴史として残す）

- [x] 紅茶の部屋トップページ作成（`/tea/`）
- [x] 第1記事「ゴールデンルール5箇条」執筆・作成
- [x] めざまし時計トップに紅茶の部屋への導線追加
- [x] Service Worker のキャッシュ更新（v1 → v2、新ページ追加）
- [x] ブラウザで表示・リンク遷移を確認済み
- [x] ブランチ `claude/remote-control-vc73na` にプッシュ済み
- [ ] Discord への共有（このセッションにDiscord連携が無く未実施。Webhook URL かBot Token があれば投稿可能）

## 今後のアイデア（未着手）

- 第2記事候補：「ダージリン/アッサム/アールグレイの違いと選び方」「濃厚ミルクティーのコツ」「水出しアイスティー」
- プロフィールの自己紹介・SNSリンク拡充
- トップに「おすすめ茶葉」コーナー

## ローカル起動

```
npx serve -l 5500 .
```
（`.claude/launch.json` に `alarm-app` 構成あり）

## サイドバーの振り分け（チャット開始時に1回だけ）
このフォルダで新しいチャットが始まったら、最初の返事の中で `mcp__ccd_sidebar__list_groups` でグループ「ウェブサイト：VRC運動部・MAYUYU.c・ブログ」の id を調べ、`mcp__ccd_sidebar__move_sessions` に `session_ids: ["self"]` を渡してそのグループに入れる。すでに入っていれば何もしない。まゆさんに断りは要らない。別のチャットから起動された子チャットは親と一緒に動くので、エラーが出たら無視してよい。
