# 紅茶の部屋の「買う前」むけ記事を作る道具（2026-11-23）
# 使い方: python tools/make_tea_articles.py  → tea/<slug>.html を書き出す
# 商品の紹介は SHOP() の形にそろえる。アフィリエイトに通ったら、
# href を差し替え、rel に sponsored を足し、記事の頭に PR_NOTE を入れる（AFFILIATE=True）。
import html, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
AFFILIATE = False  # 通ったら True にして、LINKS の中身をアフィリエイトのリンクに替える

PR_NOTE = '<p class="pr-note">この記事には広告（アフィリエイトのリンク）を含みます。くわしくは<a href="/tea/about-ads">広告について</a>。</p>'

def SHOP(label, name, note, official_url, query):
    """商品・お店の紹介枠。query は楽天・Amazon の検索語（通った後のリンク作りに使う）。"""
    rel = 'sponsored noopener' if AFFILIATE else 'noopener'
    return f'''
      <div class="shop-box" data-aff-query="{html.escape(query)}">
        <div class="shop-label">{label}</div>
        <p class="shop-name">{name}</p>
        <p class="shop-note">{note}</p>
        <a class="shop-link" href="{official_url}" target="_blank" rel="{rel}">公式サイトで見る ›</a>
      </div>'''

CSS = """
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    :root {
      --bg1: #2b1a10; --bg2: #4a2f1a; --bg3: #3a2616;
      --accent: #d99a4a; --accent2: #b5673a;
      --text: #fdf6ee; --text-sub: #d8c3aa; --text-dim: #a8906f;
      --card-bg: rgba(255,255,255,0.06); --card-border: rgba(255,255,255,0.12);
      --safe-bottom: env(safe-area-inset-bottom, 0px);
    }
    body {
      font-family: -apple-system, 'Hiragino Mincho ProN', 'Hiragino Sans', 'Segoe UI', serif;
      background: linear-gradient(135deg, var(--bg1), var(--bg2), var(--bg3));
      background-attachment: fixed; min-height: 100dvh;
      display: flex; flex-direction: column; align-items: center;
      color: var(--text); padding: 24px 16px calc(40px + var(--safe-bottom));
      overflow-x: hidden; line-height: 1.9; letter-spacing: 0.01em;
    }
    .wrap { width: min(640px, 100%); }
    .crumb { font-size: 0.78rem; color: var(--text-dim); margin-bottom: 18px; }
    .crumb a { color: var(--text-sub); text-decoration: none; }
    .crumb a:hover { color: var(--accent); }
    .crumb span { margin: 0 6px; opacity: 0.5; }
    .article-head { margin-bottom: 24px; }
    .article-head .meta { font-size: 0.74rem; color: var(--text-dim); letter-spacing: 0.06em; margin-bottom: 10px; }
    .article-head h1 { font-size: clamp(1.5rem, 6vw, 2.1rem); font-weight: 600; line-height: 1.5; letter-spacing: 0.02em; text-shadow: 0 0 30px rgba(217,154,74,0.3); }
    .card { background: var(--card-bg); backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px); border: 1px solid var(--card-border); border-radius: 22px; padding: 28px 24px; box-shadow: 0 18px 50px rgba(0,0,0,0.4); }
    .lead { font-size: 1rem; color: var(--text-sub); border-left: 3px solid var(--accent); padding-left: 14px; margin-bottom: 28px; }
    .card h2 { font-size: 1.2rem; font-weight: 600; margin: 30px 0 12px; padding-bottom: 8px; border-bottom: 1px solid rgba(217,154,74,0.25); letter-spacing: 0.02em; }
    .card h2 .icon { margin-right: 6px; }
    .card p { font-size: 0.95rem; margin-bottom: 14px; }
    .card a { color: var(--accent); }
    .card strong { color: #fff; font-weight: 600; }
    .card em { color: var(--accent); font-style: normal; font-weight: 600; }
    .material-card { background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.09); border-radius: 16px; padding: 18px 20px; margin: 14px 0; }
    .material-card h3 { font-size: 1rem; font-weight: 600; color: var(--text); margin-bottom: 8px; }
    .material-card h3 .icon { margin-right: 6px; }
    .material-card p { font-size: 0.88rem; color: var(--text-sub); margin-bottom: 0; }
    .tag-row { display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 10px; }
    .tag { font-size: 0.72rem; border-radius: 999px; padding: 3px 10px; }
    .tag.good { color: #7ecf7e; background: rgba(126,207,126,0.1); border: 1px solid rgba(126,207,126,0.3); }
    .tag.bad { color: #e89090; background: rgba(232,144,144,0.1); border: 1px solid rgba(232,144,144,0.3); }
    .tip { background: rgba(217,154,74,0.1); border: 1px solid rgba(217,154,74,0.25); border-radius: 14px; padding: 14px 16px; font-size: 0.88rem; color: var(--text-sub); margin: 18px 0; }
    .tip b { color: var(--accent); }
    table.cmp { width: 100%; border-collapse: collapse; font-size: 0.85rem; margin: 10px 0 18px; }
    table.cmp th, table.cmp td { border: 1px solid rgba(255,255,255,0.12); padding: 8px 10px; text-align: left; vertical-align: top; }
    table.cmp th { color: var(--accent); font-weight: 600; background: rgba(217,154,74,0.08); }
    table.cmp td { color: var(--text-sub); }
    .shop-box { background: rgba(255,255,255,0.05); border: 1px dashed rgba(217,154,74,0.45); border-radius: 16px; padding: 16px 18px; margin: 16px 0; }
    .shop-label { display: inline-block; font-size: 0.7rem; color: var(--bg1); background: var(--accent); border-radius: 999px; padding: 1px 10px; margin-bottom: 8px; }
    .shop-name { font-weight: 600; color: var(--text); margin-bottom: 4px !important; }
    .shop-note { font-size: 0.86rem !important; color: var(--text-sub); }
    .shop-link { display: inline-block; text-decoration: none; color: var(--accent); border: 1px solid rgba(217,154,74,0.5); border-radius: 999px; padding: 6px 16px; font-size: 0.85rem; }
    .shop-link:hover { background: rgba(217,154,74,0.12); }
    .pr-note { font-size: 0.78rem !important; color: var(--text-dim); border: 1px solid rgba(255,255,255,0.12); border-radius: 10px; padding: 6px 12px; margin-bottom: 18px !important; }
    .summary { margin-top: 30px; padding-top: 20px; border-top: 1px solid rgba(255,255,255,0.12); }
    .summary ul { list-style: none; }
    .summary li { font-size: 0.92rem; padding: 8px 0 8px 28px; position: relative; color: var(--text-sub); }
    .summary li::before { content: '☕'; position: absolute; left: 0; top: 8px; font-size: 0.9rem; }
    .related { margin-top: 22px; font-size: 0.88rem; color: var(--text-sub); }
    .related a { display: block; padding: 4px 0; }
    .nav-foot { margin-top: 22px; text-align: center; }
    .btn-back { display: inline-block; text-decoration: none; color: var(--accent); border: 1px solid rgba(217,154,74,0.4); border-radius: 999px; padding: 10px 22px; font-size: 0.88rem; transition: background .2s; }
    .btn-back:hover { background: rgba(217,154,74,0.12); }

    /* ---- ちゃんまゆのリンク帯 ---- */
    .cm-band {
      width: min(640px, 100%); margin: 28px auto 0; padding: 14px 12px 4px;
      border-top: 1px solid var(--card-border, rgba(255,255,255,0.12));
      display: flex; flex-wrap: wrap; justify-content: center; gap: 0.4em 1em;
      font-size: 0.8rem; line-height: 1.6; flex-shrink: 0; box-sizing: border-box;
    }
    .cm-band a { color: var(--text-dim, rgba(255,255,255,0.55)); text-decoration: none; white-space: nowrap; transition: color .2s; }
    .cm-band a:hover, .cm-band a:focus-visible { color: var(--accent, #fff); }
    .cm-band a + a::before { content: "｜"; opacity: .5; margin-right: 1em; color: var(--text-dim, rgba(255,255,255,0.55)); }
"""

BAND = """  <nav class="cm-band" aria-label="ちゃんまゆのリンク">
    <a href="https://mayuyu.booth.pm/" target="_blank" rel="noopener">ちゃんまゆ工房（BOOTH）</a>
    <a href="https://note.com/cute_serval922" target="_blank" rel="noopener">note</a>
    <a href="https://x.com/ChanmayuKobo" target="_blank" rel="noopener">X @ChanmayuKobo</a>
    <a href="https://mayuyu-c.pages.dev/" target="_blank" rel="noopener">MAYUYU.c</a>
    <a href="https://vrc-sports-club.pages.dev/" target="_blank" rel="noopener">VRC運動部</a>
    <a href="https://vrchat-blog-7i2.pages.dev/" target="_blank" rel="noopener">VRChat ラボ</a>
  </nav>"""

def page(slug, title, h1_html, crumb, desc, keywords, category, date, body):
    url = f"https://alame.pages.dev/tea/{slug}"
    d = date.replace('.', '-')
    pr = PR_NOTE if AFFILIATE else ''
    return f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover" />
  <title>{title} | 紅茶の部屋</title>

  <meta name="description" content="{desc}" />
  <meta name="keywords" content="{keywords}" />
  <meta name="robots" content="index, follow" />
  <link rel="canonical" href="{url}" />

  <meta property="og:type" content="article" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{desc}" />
  <meta property="og:url" content="{url}" />
  <meta property="og:image" content="https://alame.pages.dev/ogp.png" />
  <meta property="og:locale" content="ja_JP" />
  <meta property="og:site_name" content="紅茶の部屋" />

  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{title}" />
  <meta name="twitter:description" content="{desc}" />
  <meta name="twitter:image" content="https://alame.pages.dev/ogp.png" />

  <meta name="theme-color" content="#3a2616" />
  <link rel="apple-touch-icon" href="/icon-192.svg" />

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "{title}",
    "description": "{desc}",
    "datePublished": "{d}",
    "dateModified": "{d}",
    "inLanguage": "ja",
    "image": "https://alame.pages.dev/ogp.png",
    "author": {{ "@type": "Person", "name": "紅茶の部屋 管理人", "jobTitle": "紅茶アドバイザー・紅茶マイスター" }},
    "publisher": {{ "@type": "Organization", "name": "紅茶の部屋" }},
    "mainEntityOfPage": "{url}"
  }}
  </script>

  <style>{CSS}  </style>
</head>
<body>
  <div class="wrap">

    <nav class="crumb">
      <a href="/tea/">紅茶の部屋</a><span>›</span>{crumb}
    </nav>

    <header class="article-head">
      <div class="meta">{date} ・ {category}</div>
      <h1>{h1_html}</h1>
    </header>

    <article class="card">
      {pr}{body}
    </article>

    <div class="nav-foot">
      <a class="btn-back" href="/tea/">← 紅茶の部屋にもどる</a>
    </div>

  </div>
{BAND}
</body>
</html>
"""

ARTICLES = []

# ---------------------------------------------------------------- 1
ARTICLES.append(dict(
  slug="starter-tools",
  title="紅茶をはじめる道具 ― 最初にそろえるのはこの5つ",
  h1_html="紅茶をはじめる道具<br>― 最初にそろえるのはこの5つ",
  crumb="紅茶をはじめる道具",
  desc="ティーポット・茶こし・電気ケトル・ティースプーン・タイマー。リーフティー（茶葉）で紅茶をはじめるときに最初にそろえたい道具と、選ぶときの見どころをまとめました。",
  keywords="紅茶,道具,初心者,そろえる,ティーポット,茶こし,電気ケトル,温度,ティースプーン",
  category="道具選び", date="2026.11.23",
  body=f"""<p class="lead">ティーバッグから一歩進んで、茶葉（リーフティー）で紅茶をいれてみたい。そう思ったときに、最初にそろえる道具は多くありません。家にある物で代わりになる物も多いので、足りない物だけ足していけば大丈夫です。</p>

      <h2><span class="icon">🫖</span>1. ティーポット</h2>
      <p>茶葉がお湯の中で動ける広さのあるポットを選びます。丸みのある形だと、お湯を注いだときに茶葉が上下に舞う「ジャンピング」が起きやすくなります。1〜2人なら<em>400ml前後</em>が使いやすい大きさです。</p>
      <p>素材ごとの得意・不得意は<a href="/tea/teapot-choice">ティーポットの選び方</a>にまとめています。迷ったら、香りが移りにくく手入れもしやすい磁器か、ジャンピングが目で見えるガラスから。</p>
{SHOP("道具の例", "ガラスのティーポット（HARIO）", "耐熱ガラスのメーカー。茶こしつきのポットもあり、ジャンピングや水色（すいしょく）を見ながらいれられます。", "https://www.hario.com/", "HARIO ティーポット")}

      <h2><span class="icon">🍵</span>2. 茶こし（ストレーナー）</h2>
      <p>カップに注ぐときに茶葉を受け止める道具です。ポットに茶こしがついていれば、別に買わなくてもかまいません。茶こしつきのポットでも、細かい茶葉（BOP や CTC）は網をすり抜けることがあるので、網目の細かい物を1つ持っておくと安心です。</p>
      <div class="tip"><b>ひとこと：</b> ポットの中に入れる「ティーインフューザー（茶こしのかご）」は手軽ですが、かごが小さいと茶葉が広がりきらず、味が出にくくなります。かごは大きめを。</div>

      <h2><span class="icon">♨️</span>3. 電気ケトル（やかんでも可）</h2>
      <p>紅茶は<em>沸騰したての熱いお湯（95〜98℃ほど）</em>でいれるのが基本です（<a href="/tea/golden-rule">ゴールデンルール</a>）。ですから紅茶だけなら、しっかり沸騰させられればやかんでも電気ケトルでもかまいません。</p>
      <p>電気ケトルを選ぶなら、見るところは次の3つです。</p>
      <div class="material-card">
        <h3><span class="icon">🌡️</span>温度を選べるか</h3>
        <p>紅茶は沸騰したてでいれるので、温度設定は必須ではありません。緑茶やコーヒーもいれる人は、温度を選べる機種だと使い分けが楽になります。</p>
      </div>
      <div class="material-card">
        <h3><span class="icon">💧</span>注ぎ口の形</h3>
        <p>細い注ぎ口は、お湯の量と勢いを調整しやすい形です。紅茶は「高い位置から勢いよく」注ぐので、ふつうの注ぎ口でも困りません。ハンドドリップのコーヒーもいれるなら細口が便利です。</p>
      </div>
      <div class="material-card">
        <h3><span class="icon">⏱️</span>保温機能の使い方</h3>
        <p>保温しておいたお湯や、一度冷めたお湯の沸かし直しは、空気が抜けて味がぼやけやすくなります。紅茶をいれるときは、汲みたての水を沸かすのがいちばんです。</p>
      </div>
{SHOP("道具の例", "温度が選べる電気ケトル（ティファール）", "公式サイトに「温度コントロールケトル」の並びがあります。容量・選べる温度・保温の有無は機種ごとに違うので、公式の仕様で確かめてください。", "https://www.t-fal.co.jp/", "ティファール 電気ケトル 温度調節")}

      <h2><span class="icon">🥄</span>4. ティースプーン（計量スプーン）</h2>
      <p>茶葉の量は、カップ1杯（約150〜160ml）にティースプーン1杯が目安です。細かい茶葉はすり切り、大きな茶葉は山盛り。毎回同じスプーンで量ると、味がぶれにくくなります。紅茶用の「メジャースプーン」もありますが、家のティースプーンで十分はじめられます。</p>

      <h2><span class="icon">⏰</span>5. タイマー</h2>
      <p>蒸らし時間の目安は、細かい茶葉で2〜3分、大きな茶葉で3〜4分。砂時計でもキッチンタイマーでも、スマホでもかまいません。このサイトの<a href="/">めざまし時計</a>もブラウザでそのまま使えます。</p>

      <h2><span class="icon">✨</span>あると楽しい道具</h2>
      <table class="cmp">
        <tr><th>道具</th><th>あるとうれしいこと</th></tr>
        <tr><td>ティーコジー（ポットカバー）</td><td>蒸らしている間にポットが冷めにくい。ガラスのポットと相性がよい</td></tr>
        <tr><td>茶葉の保存缶</td><td>光・湿気・においから茶葉を守る（<a href="/tea/storage">茶葉の保管方法</a>）</td></tr>
        <tr><td>ミルクパン（小鍋）</td><td>鍋で煮出すロイヤルミルクティーやチャイが作れる（<a href="/tea/milk-tea">ミルクティーのコツ</a>）</td></tr>
        <tr><td>ティーカップ</td><td>口が広く浅いカップは香りが立ちやすく、水色もよく見える</td></tr>
      </table>

      <div class="summary">
        <p><strong>今日のまとめ</strong></p>
        <ul>
          <li>最初の5つ：ティーポット・茶こし・ケトル・ティースプーン・タイマー</li>
          <li>ポットは茶葉が動ける丸い形。1〜2人なら400ml前後</li>
          <li>紅茶は沸騰したてでいれるので、ケトルの温度設定は「あると便利」</li>
          <li>保温や沸かし直しのお湯より、汲みたての水を沸かす</li>
          <li>家にある物で足りるなら、足りない物だけ足せばOK</li>
        </ul>
      </div>
      <div class="related">関連する記事
        <a href="/tea/golden-rule">› おいしい紅茶のいれ方 ― ゴールデンルール5箇条</a>
        <a href="/tea/teabag-vs-leaf">› ティーバッグとリーフティー、どう選ぶ？</a>
      </div>"""))

# ---------------------------------------------------------------- 2
ARTICLES.append(dict(
  slug="teabag-vs-leaf",
  title="ティーバッグとリーフティー（茶葉）のちがいと選び方",
  h1_html="ティーバッグとリーフティー<br>― ちがいと選び方",
  crumb="ティーバッグとリーフティー",
  desc="ティーバッグと茶葉（リーフティー）は何がちがう？ 茶葉の大きさ・出方・手間・向いている飲み方を比べ、ティーバッグをおいしくいれるコツもまとめました。",
  keywords="ティーバッグ,リーフティー,茶葉,ちがい,選び方,紅茶,いれ方,初心者",
  category="茶葉の選び方", date="2026.11.23",
  body=f"""<p class="lead">ティーバッグはおいしくない、というわけではありません。ちがうのは主に「中の茶葉の大きさ」と「手間」です。それぞれの得意なことを知って、場面で使い分けるのがいちばん楽しい付き合い方です。</p>

      <h2><span class="icon">🔍</span>いちばんのちがいは茶葉の大きさ</h2>
      <p>ティーバッグには、短い時間で味が出るように<strong>細かくした茶葉</strong>が多く使われます。細かい茶葉はお湯にふれる面が広いので、色も味も早く、濃く出ます。</p>
      <p>リーフティーは、葉の形が残った大きめの茶葉も選べます。大きな茶葉はゆっくり開きながら、香りや味の移り変わりを楽しめます。茶葉の形と等級の話は<a href="/tea/tea-leaves-type">OP・BOP・CTC の違い</a>にくわしく書いています。</p>

      <table class="cmp">
        <tr><th></th><th>ティーバッグ</th><th>リーフティー</th></tr>
        <tr><td>中の茶葉</td><td>細かい物が多い</td><td>大きい物から細かい物まで選べる</td></tr>
        <tr><td>出方</td><td>早く、濃く出やすい</td><td>茶葉の大きさしだい。大きいとゆっくり</td></tr>
        <tr><td>手間</td><td>量らなくてよい。後片づけが楽</td><td>量る・こす・ポットを洗う手間がある</td></tr>
        <tr><td>向いている場面</td><td>朝や職場、1杯だけ飲みたいとき</td><td>休日にゆっくり、来客、飲み比べ</td></tr>
        <tr><td>種類の選びやすさ</td><td>手に入りやすく、試しやすい</td><td>産地・農園・季節など選べる幅が広い</td></tr>
      </table>

      <h2><span class="icon">☕</span>ティーバッグをおいしくいれる4つのコツ</h2>
      <p>ティーバッグでも、<a href="/tea/golden-rule">ゴールデンルール</a>の考え方はそのまま使えます。</p>
      <div class="material-card">
        <h3><span class="icon">1️⃣</span>カップを先に温める</h3>
        <p>お湯を入れて温め、そのお湯を捨ててから始めます。温度が下がりにくくなります。</p>
      </div>
      <div class="material-card">
        <h3><span class="icon">2️⃣</span>お湯が先、ティーバッグは後</h3>
        <p>沸騰したてのお湯をカップに注いでから、ティーバッグをそっと沈めます。ティーバッグにお湯を直接かけるより、湯の中で茶葉が動きやすくなります。</p>
      </div>
      <div class="material-card">
        <h3><span class="icon">3️⃣</span>ふたをして、時間を守る</h3>
        <p>小皿などでふたをして蒸らします。時間はパッケージの表示を目安に。濃くしたいときは時間をのばすより、ティーバッグの数を増やすほうが渋くなりにくいです。</p>
      </div>
      <div class="material-card">
        <h3><span class="icon">4️⃣</span>振らない・しぼらない</h3>
        <p>取り出すときにティーバッグを振ったりスプーンでしぼったりすると、渋みや雑味が出やすくなります。静かに引き上げましょう。</p>
      </div>

      <h2><span class="icon">🧭</span>どちらを選ぶ？ 場面別の目安</h2>
      <table class="cmp">
        <tr><th>こんなとき</th><th>おすすめ</th></tr>
        <tr><td>毎朝さっと1杯</td><td>ティーバッグ</td></tr>
        <tr><td>ミルクティーを濃く</td><td>CTC やアッサムのティーバッグ、または細かい茶葉（<a href="/tea/milk-tea">ミルクティーのコツ</a>）</td></tr>
        <tr><td>香りをじっくり楽しみたい</td><td>ダージリンなどのリーフティー（<a href="/tea/darjeeling">3銘柄の違い</a>）</td></tr>
        <tr><td>お客さまに数杯ぶん</td><td>リーフティーをポットで</td></tr>
        <tr><td>いろいろ試してみたい</td><td>ティーバッグの詰め合わせや、少量のリーフ</td></tr>
      </table>
      <div class="tip"><b>ひとこと：</b> ティーバッグの形には平たい物のほか、三角すい（テトラ）型などもあります。中が広い形は、茶葉がお湯の中で動きやすいのが特徴です。</div>

{SHOP("お店の例", "日東紅茶（三井農林）", "国内の紅茶メーカー。ティーバッグを中心に、ふだん使いの紅茶をそろえています。", "https://www.nittoh-tea.com/", "日東紅茶 ティーバッグ")}
{SHOP("お店の例", "カレルチャペック紅茶店", "紅茶の専門店。ティーバッグとリーフの両方があり、公式通販サイトがあります。", "https://karelcapek.co.jp/", "カレルチャペック 紅茶")}

      <div class="summary">
        <p><strong>今日のまとめ</strong></p>
        <ul>
          <li>いちばんのちがいは中の茶葉の大きさ。ティーバッグは細かい茶葉が多い</li>
          <li>ティーバッグは早く濃く出て、手間が少ない</li>
          <li>リーフティーは選べる幅が広く、香りの移り変わりを楽しめる</li>
          <li>ティーバッグも「温める・お湯が先・ふた・振らない」でぐっとおいしく</li>
          <li>毎日はティーバッグ、休日はリーフ、の使い分けもおすすめ</li>
        </ul>
      </div>
      <div class="related">関連する記事
        <a href="/tea/starter-tools">› 紅茶をはじめる道具 ― 最初にそろえるのはこの5つ</a>
        <a href="/tea/gift">› 紅茶を贈るときの選び方</a>
      </div>"""))

# ---------------------------------------------------------------- 3
ARTICLES.append(dict(
  slug="gift",
  title="紅茶を贈るときの選び方 ― 相手に合わせる5つのポイント",
  h1_html="紅茶を贈るときの選び方<br>― 相手に合わせる5つのポイント",
  crumb="紅茶を贈るときの選び方",
  desc="紅茶のギフトで迷ったときに。相手の飲み方・ティーバッグかリーフか・カフェイン・量と賞味期限・缶やパッケージ、の5つの見どころで選び方をまとめました。",
  keywords="紅茶,ギフト,贈り物,プレゼント,選び方,ティーバッグ,デカフェ,缶",
  category="楽しみ方", date="2026.11.23",
  body=f"""<p class="lead">紅茶は、好みがはっきり分かれる飲み物です。だからこそ「相手がどう飲んでいるか」を少し想像するだけで、贈り物の満足度が大きく変わります。迷ったときに見る5つのポイントをまとめました。</p>

      <h2><span class="icon">1️⃣</span>相手の飲み方を思い浮かべる</h2>
      <p>ミルクを入れて飲む人には、濃く出るアッサムや細かい茶葉の紅茶が合います。ストレートで香りを楽しむ人にはダージリン、気分を変えたい人にはアールグレイのような香りのついた紅茶（フレーバーティー）。銘柄ごとの性格は<a href="/tea/darjeeling">ダージリン・アッサム・アールグレイの違い</a>にまとめています。</p>
      <p>フレーバーティーは香りの好みが分かれやすいので、相手の好みがわからないときは、定番の銘柄と組み合わせると安心です。</p>

      <h2><span class="icon">2️⃣</span>ティーバッグか、リーフか</h2>
      <p>ポットや茶こしを持っていない人に茶葉（リーフ）を贈ると、飲むまでのハードルが上がってしまいます。<strong>道具を持っているかわからないときはティーバッグ</strong>が無難です。紅茶好きの人や、道具をそろえている人にはリーフも喜ばれます。ちがいは<a href="/tea/teabag-vs-leaf">ティーバッグとリーフティーのちがい</a>へ。</p>

      <h2><span class="icon">3️⃣</span>カフェインを気にする人には</h2>
      <p>紅茶にはカフェインが含まれます。妊娠中の人や、夜に飲みたい人など、カフェインを控えている相手には、カフェインを取り除いた<strong>デカフェ（カフェインレス）の紅茶</strong>という選び方があります。</p>
      <div class="tip"><b>ことばの注意：</b> ルイボスティーやカモミールなどのハーブティーは、紅茶とは別の植物から作られた飲み物です。「ノンカフェインの紅茶」として贈る前に、原材料を確かめましょう。</div>

      <h2><span class="icon">4️⃣</span>量と賞味期限</h2>
      <p>開けた茶葉は少しずつ香りが落ちていきます（<a href="/tea/storage">茶葉の保管方法</a>）。大きな缶をひとつより、<strong>飲みきれる量を何種類か</strong>のほうが、飲み比べも楽しめて最後までおいしく飲めます。贈る前に、パッケージの賞味期限も見ておきましょう。</p>

      <h2><span class="icon">5️⃣</span>缶やパッケージ</h2>
      <p>紅茶のギフトは缶入りが多く、飲み終わった後も茶葉やお菓子の入れ物として使えます。光を通さず、ふたがしっかり閉まる缶は、保存容器としても実用的です。見た目で選ぶのも、紅茶のギフトの楽しいところです。</p>

      <h2><span class="icon">🎁</span>相手別の早見表</h2>
      <table class="cmp">
        <tr><th>相手</th><th>選び方の例</th></tr>
        <tr><td>紅茶をあまり飲まない人</td><td>ティーバッグの詰め合わせ。定番の銘柄を中心に</td></tr>
        <tr><td>ミルクティー好き</td><td>アッサムや CTC の紅茶</td></tr>
        <tr><td>紅茶好き・道具を持っている人</td><td>ダージリンなどのリーフを少量ずつ、飲み比べで</td></tr>
        <tr><td>カフェインを控えている人</td><td>デカフェの紅茶（ハーブティーと取り違えない）</td></tr>
        <tr><td>職場へのお配り</td><td>個包装のティーバッグ</td></tr>
      </table>

{SHOP("お店の例", "ルピシア（LUPICIA）", "紅茶・緑茶・烏龍茶などのお茶の専門店。公式のオンラインストアがあります。", "https://www.lupicia.com/", "ルピシア 紅茶 ギフト")}
{SHOP("お店の例", "カレルチャペック紅茶店", "絵柄のパッケージが特徴の紅茶の専門店。公式通販サイトがあります。", "https://karelcapek.co.jp/", "カレルチャペック 紅茶 ギフト")}
      <p style="font-size:0.82rem;color:var(--text-dim);">のし・包装・配送日の指定ができるかは、お店によってちがいます。注文の前に各お店の案内で確かめてください。</p>

      <div class="summary">
        <p><strong>今日のまとめ</strong></p>
        <ul>
          <li>まず相手の飲み方（ミルク派・ストレート派）を思い浮かべる</li>
          <li>道具を持っているかわからなければティーバッグ</li>
          <li>カフェインを控えている人にはデカフェ。ハーブティーとは別物</li>
          <li>大きな缶ひとつより、飲みきれる量を何種類か</li>
          <li>缶は飲み終わった後も保存容器として使える</li>
        </ul>
      </div>
      <div class="related">関連する記事
        <a href="/tea/teabag-vs-leaf">› ティーバッグとリーフティー（茶葉）のちがいと選び方</a>
        <a href="/tea/afternoon-tea">› アフタヌーンティーを家で楽しむ</a>
      </div>"""))

if __name__ == "__main__":
    for a in ARTICLES:
        out = ROOT / "tea" / f"{a['slug']}.html"
        out.write_text(page(**a), encoding="utf-8", newline="\n")
        print("wrote", out)
