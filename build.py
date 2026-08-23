#!/usr/bin/env python3
"""hyesun5464.github.io 정적 사이트 빌더.

각 앱 저장소의 docs/*.md 를 읽어 이 저장소의 HTML 페이지를 다시 만든다.
폴더 배치 전제 (전부 C:\\dev 아래 형제 폴더):

    dev/
    ├── my_star/               docs/privacy_policy.md, docs/terms_of_service.md
    ├── line-memorizer/        docs/privacy_policy.md
    └── hyesun5464.github.io/  ← 이 저장소. 여기서 python build.py

사용법:
    pip install markdown
    python build.py
"""
import re
import sys
from pathlib import Path

try:
    import markdown
except ImportError:
    sys.exit("markdown 패키지가 필요합니다:  pip install markdown")

ROOT = Path(__file__).resolve().parent
DEV = ROOT.parent

CONTACT = "hyesun5464@gmail.com"
OWNER = "도해 (Dohae)"

# ---------------------------------------------------------------- 앱 정의

APPS = [
    {
        "slug": "my-star",
        "name": "My Star",
        "emoji": "&#11088;",
        "tagline": "작은 성공을 모으는 습관",
        "blurb": "집중하기 전에 내 보상을 만들고, 25분을 버티면 랜덤으로 뽑는 보상 자판기 타이머.",
        "package": "com.dohae.my_star",
        "repo": "my_star",
        "hero": (
            "radial-gradient(ellipse 120% 90% at 50% -10%, "
            "#3b3382 0%, #201c4a 45%, #14122c 100%)"
        ),
        "features": [
            ("&#127873;", "집중하기 ‘전에’ 보상을 만들어요",
             "커피, 웹툰 한 화, 게임 30분… 내가 진짜 원하는 걸 미리 등록해 둡니다. "
             "남이 정해준 배지가 아니라, 내가 고른 실제 보상이에요."),
            ("&#127920;", "25분을 버티면 ‘뽑아요’",
             "완료하면 보상 자판기가 열립니다. 무엇이 나올지는 아무도 몰라요. "
             "랜덤이라서 기대되고, 기대되니까 START를 누르게 됩니다."),
            ("&#9733;", "별은 쌓이기만 해요, 절대 줄지 않아요",
             "포기해도, 며칠 쉬어도 별은 그대로입니다. "
             "“3일째 안 하셨네요” 같은 죄책감 알림은 보내지 않아요."),
            ("&#9203;", "시간이 눈에 보여요",
             "숫자 카운트다운 대신, 원이 실제로 줄어드는 시각 타이머입니다. "
             "10 / 15 / 25 / 45분 중에서 고를 수 있어요."),
            ("&#129504;", "ADHD를 위한 설계",
             "3번의 탭이면 타이머가 돌아가고, 할 일 선택은 건너뛸 수 있으며, "
             "실패에 벌점이 없습니다."),
        ],
        "docs": [
            ("privacy.html", "개인정보처리방침", "privacy_policy.md"),
            ("terms.html", "이용약관", "terms_of_service.md"),
        ],
    },
    {
        "slug": "daesa-note",
        "name": "대사노트",
        "emoji": "&#127908;",
        "tagline": "대본 암기 · 리딩 연습",
        "blurb": "대본을 붙여넣거나 PDF로 가져오면 문장·화자 단위로 분리되고, "
                 "한 줄씩 떠올리며 스스로 암기를 점검할 수 있어요.",
        "package": "com.linememorizer.line_memorizer",
        "repo": "line-memorizer",
        "hero": (
            "radial-gradient(ellipse 120% 90% at 50% -10%, "
            "#7a2f43 0%, #45203a 45%, #1e1226 100%)"
        ),
        "features": [
            ("&#128220;", "붙여넣거나, PDF에서 가져오거나",
             "대본을 붙여넣으면 문장과 화자 단위로 자동 분리됩니다. "
             "PDF에서 텍스트를 뽑아오는 것도 기기 안에서 처리돼요."),
            ("&#128065;", "한 줄씩 떠올리며 점검",
             "내가 맡은 역할의 대사를 가려두고, ‘다음 문장 보기’로 하나씩 확인합니다. "
             "외웠는지 스스로 검증할 수 있어요."),
            ("&#127911;", "연습 녹음",
             "리딩 연습을 녹음해서 다시 들어볼 수 있습니다. "
             "녹음 파일은 기기 안에만 저장돼요."),
            ("&#128200;", "회독수와 연속 기록",
             "대본별 회독수가 쌓이고, 며칠 연속으로 연습했는지 확인할 수 있습니다."),
            ("&#128274;", "계정 없이, 기기 안에서만",
             "로그인이 없습니다. 대본과 녹음은 서버로 올라가지 않고 "
             "내 기기에만 저장됩니다."),
        ],
        "docs": [
            ("privacy.html", "개인정보처리방침", "privacy_policy.md"),
        ],
    },
]

# ---------------------------------------------------------------- 템플릿


def head(title, desc, depth, extra_css=""):
    up = "../" * depth
    return f"""<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="color-scheme" content="light dark">
<link rel="stylesheet" href="{up}style.css">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>&#11088;</text></svg>">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
{extra_css}</head>
<body>
"""


def site_head(depth, app=None):
    up = "../" * depth
    if app:
        brand = f'<a class="brand" href="index.html">{app["emoji"]} {app["name"]}</a>'
        links = "".join(
            f'<a href="{f}">{label}</a>' for f, label, _ in app["docs"]
        )
        links = f'<a href="{up}index.html">전체 앱</a>' + links
    else:
        brand = f'<a class="brand" href="{up}index.html"><span class="star">&#9733;</span> 도해</a>'
        links = ""
    return f"""<header class="site-head">
  <div class="wrap">
    {brand}
    <nav class="site-nav">{links}</nav>
  </div>
</header>
"""


def site_foot(depth):
    return f"""<footer class="site-foot">
  <div class="wrap">
    <span>&copy; 2026 {OWNER}</span>
    <span><a href="mailto:{CONTACT}">{CONTACT}</a></span>
  </div>
</footer>
</body>
</html>
"""


# ---------------------------------------------------------------- 빌더


def build_doc(app, filename, label, md_name):
    src = DEV / app["repo"] / "docs" / md_name
    if not src.exists():
        print(f"  ! 원문 없음, 건너뜀: {src}")
        return
    html = markdown.markdown(
        src.read_text(encoding="utf-8"),
        extensions=["tables", "sane_lists", "attr_list"],
    )
    html = re.sub(
        r"<p>(<strong>시행일자[^<]*</strong>[^<]*)</p>",
        r'<p class="effective">\1</p>', html, count=1,
    )
    html = re.sub(
        r"(<table>.*?</table>)", r'<div class="table-scroll">\1</div>',
        html, flags=re.S,
    )
    body = "\n".join("    " + ln for ln in html.splitlines())

    out = ROOT / app["slug"] / filename
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(
        head(f'{label} · {app["name"]}', f'{app["name"]} 앱의 {label}입니다.', 1)
        + site_head(1, app)
        + '<main>\n  <div class="wrap doc">\n'
        + body
        + "\n  </div>\n</main>\n"
        + site_foot(1),
        encoding="utf-8",
    )
    print(f"  {app['slug']}/{filename}")


HERO_CSS = """<style>
  .hero {{
    background: {hero};
    color: #f4f2fa; padding: 84px 0 76px; text-align: center;
    position: relative; overflow: hidden;
  }}
  .hero::after {{
    content: ""; position: absolute; inset: 0; opacity: .55; pointer-events: none;
    background-image:
      radial-gradient(1.6px 1.6px at 12% 22%, #fff, transparent),
      radial-gradient(1.4px 1.4px at 78% 16%, #fff, transparent),
      radial-gradient(1.2px 1.2px at 34% 68%, #ffe9b0, transparent),
      radial-gradient(1.5px 1.5px at 62% 78%, #fff, transparent),
      radial-gradient(1.1px 1.1px at 88% 56%, #fff, transparent),
      radial-gradient(1.3px 1.3px at 22% 88%, #ffe9b0, transparent),
      radial-gradient(1.2px 1.2px at 50% 34%, #fff, transparent);
  }}
  .hero .wrap {{ position: relative; z-index: 1; }}
  .hero-mark {{ font-size: 3rem; line-height: 1; display: block; margin-bottom: 18px; }}
  .hero h1 {{ font-size: 2.1rem; line-height: 1.3; margin: 0 0 14px;
              letter-spacing: -.02em; font-weight: 800; }}
  .hero p {{ margin: 0 auto; max-width: 30em; color: #cfcbe4; font-size: 1.02rem; }}
  .hero-cta {{ display: inline-block; margin-top: 30px; background: #f5c04e;
               color: #241f14; font-weight: 700; font-size: .95rem;
               padding: 12px 26px; border-radius: 999px; }}
  .hero-cta:hover {{ text-decoration: none; background: #ffcf6b; }}
  @media (max-width: 560px) {{
    .hero {{ padding: 64px 0 58px; }}
    .hero h1 {{ font-size: 1.65rem; }}
  }}
</style>
"""


def build_app_landing(app):
    features = "\n".join(
        f"""    <div class="feature">
      <div class="feature-icon">{icon}</div>
      <div>
        <h2>{title}</h2>
        <p>{text}</p>
      </div>
    </div>"""
        for icon, title, text in app["features"]
    )
    doc_links = "".join(
        f'        <a href="{f}">{label}</a>\n' for f, label, _ in app["docs"]
    )
    play = f'https://play.google.com/store/apps/details?id={app["package"]}'

    out = ROOT / app["slug"] / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(
        head(f'{app["name"]} · {app["tagline"]}', app["blurb"], 1,
             HERO_CSS.format(hero=app["hero"]))
        + f"""<section class="hero">
  <div class="wrap">
    <span class="hero-mark">{app["emoji"]}</span>
    <h1>{app["tagline"]}</h1>
    <p>{app["blurb"]}</p>
    <a class="hero-cta" href="{play}">Google Play에서 보기</a>
  </div>
</section>

<main>
  <div class="wrap features">
{features}

    <section class="legal">
      <h2>문서 및 문의</h2>
      <p>서비스 이용과 개인정보 처리에 관한 사항은 아래 문서를 확인해 주세요.</p>
      <div class="legal-links">
{doc_links}        <a href="mailto:{CONTACT}">문의하기</a>
      </div>
    </section>

    <p class="back"><a href="../index.html">&larr; 다른 앱 보기</a></p>
  </div>
</main>
"""
        + site_foot(1),
        encoding="utf-8",
    )
    print(f"  {app['slug']}/index.html")


def build_hub():
    cards = "\n".join(
        f"""      <a class="app-card" href="{a["slug"]}/index.html">
        <span class="app-emoji">{a["emoji"]}</span>
        <span class="app-text">
          <strong>{a["name"]}</strong>
          <span class="app-tagline">{a["tagline"]}</span>
          <span class="app-blurb">{a["blurb"]}</span>
        </span>
      </a>"""
        for a in APPS
    )
    (ROOT / "index.html").write_text(
        head("도해 — 만든 앱들", "도해가 만든 안드로이드 앱 모음. My Star, 대사노트.", 0,
             """<style>
  .intro { padding: 72px 0 8px; text-align: center; }
  .intro .mark { font-size: 2.6rem; display: block; margin-bottom: 16px; }
  .intro h1 { font-size: 1.9rem; margin: 0 0 10px; letter-spacing: -.02em; font-weight: 800; }
  .intro p { color: var(--text-muted); margin: 0; }
  .app-list { display: grid; gap: 14px; margin: 40px 0 64px; }
  .app-card {
    display: flex; gap: 18px; align-items: flex-start;
    border: 1px solid var(--border); background: var(--surface);
    border-radius: var(--radius); padding: 22px 24px; color: var(--text);
  }
  .app-card:hover { text-decoration: none; border-color: var(--accent); }
  .app-emoji {
    flex: 0 0 auto; width: 48px; height: 48px; border-radius: 14px;
    background: var(--accent-soft); display: grid; place-items: center; font-size: 1.4rem;
  }
  .app-text { display: block; }
  .app-text strong { display: block; font-size: 1.08rem; letter-spacing: -.01em; }
  .app-tagline { display: block; color: var(--accent); font-size: .88rem; margin: 2px 0 8px; }
  .app-blurb { display: block; color: var(--text-muted); font-size: .93rem; line-height: 1.6; }
  @media (max-width: 560px) {
    .intro { padding: 52px 0 4px; }
    .intro h1 { font-size: 1.5rem; }
    .app-card { padding: 18px 18px; gap: 14px; }
  }
</style>
""")
        + f"""<main>
  <div class="wrap intro">
    <span class="mark">&#11088;</span>
    <h1>도해가 만든 앱</h1>
    <p>작게, 실제로 쓰이는 앱을 만듭니다.</p>
  </div>
  <div class="wrap">
    <div class="app-list">
{cards}
    </div>
  </div>
</main>
"""
        + site_foot(0),
        encoding="utf-8",
    )
    print("  index.html (허브)")


# ---------------------------------------------------------------- 구버전 URL 유지

# 예전 평면 구조(루트에 privacy.html/terms.html)로 이미 등록해 둔 주소가 있어
# 404가 나지 않도록 리다이렉트 페이지를 남긴다.
# Play Console 등록 주소를 새 경로로 모두 바꾼 뒤에는 지워도 된다.
LEGACY = [
    ("privacy.html", "my-star/privacy.html", "My Star 개인정보처리방침"),
    ("terms.html", "my-star/terms.html", "My Star 이용약관"),
]


def build_legacy_redirects():
    for old, new, label in LEGACY:
        (ROOT / old).write_text(
            f"""<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{label}</title>
<meta name="robots" content="noindex">
<link rel="canonical" href="https://hyesun5464.github.io/{new}">
<meta http-equiv="refresh" content="0; url=./{new}">
<link rel="stylesheet" href="style.css">
</head>
<body>
<main>
  <div class="wrap doc" style="padding-top:64px">
    <h1>{label}</h1>
    <p>이 문서는 <a href="./{new}">새 주소</a>로 옮겨졌습니다. 잠시 후 자동으로 이동합니다.</p>
    <p><a href="./{new}">https://hyesun5464.github.io/{new}</a></p>
  </div>
</main>
<script>location.replace("./{new}");</script>
</body>
</html>
""",
            encoding="utf-8",
        )
        print(f"  {old} → {new} (리다이렉트)")


def main():
    print("빌드 중...")
    build_hub()
    for app in APPS:
        build_app_landing(app)
        for filename, label, md_name in app["docs"]:
            build_doc(app, filename, label, md_name)
    build_legacy_redirects()
    print("완료. 변경분을 커밋해서 푸시하면 GitHub Pages에 반영됩니다.")


if __name__ == "__main__":
    main()
