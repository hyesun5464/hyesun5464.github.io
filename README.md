# hyesun5464.github.io

도해가 만든 앱들의 공식 웹사이트. AdMob `app-ads.txt` 인증과 Google Play 등록에 필요한
개인정보처리방침 · 이용약관을 호스팅한다.

## 구조

```
/
├── app-ads.txt        ← 전 앱 공통. 반드시 루트에 있어야 한다
├── index.html         ← 앱 목록 허브
├── style.css          ← 전 페이지 공용 스타일
├── build.py           ← 페이지 생성 스크립트
├── my-star/
│   ├── index.html     앱 소개
│   ├── privacy.html   개인정보처리방침
│   └── terms.html     이용약관
└── daesa-note/
    ├── index.html
    └── privacy.html
```

## Play Console에 넣을 주소

| 앱 | 항목 | 주소 |
|---|---|---|
| 공통 | 웹사이트 (스토어 설정 → 연락처 세부정보) | `https://hyesun5464.github.io/` |
| My Star | 개인정보처리방침 | `https://hyesun5464.github.io/my-star/privacy.html` |
| 대사노트 | 개인정보처리방침 | `https://hyesun5464.github.io/daesa-note/privacy.html` |

`app-ads.txt`는 앱마다 만들 필요가 없다. 같은 AdMob 퍼블리셔 ID를 쓰는 앱은
루트의 파일 하나로 전부 인증된다.

## 페이지 다시 만들기

방침·약관 원문은 이 저장소가 아니라 **각 앱 저장소의 `docs/`** 에 있다.
원문을 고친 뒤 이 저장소에서 아래를 실행하면 HTML이 다시 만들어진다.

```
pip install markdown
python build.py
```

전제 폴더 배치 (전부 형제 폴더여야 한다):

```
dev/
├── my_star/                docs/privacy_policy.md, docs/terms_of_service.md
├── line-memorizer/         docs/privacy_policy.md
└── hyesun5464.github.io/   ← 여기서 실행
```

앱을 추가할 때는 `build.py` 상단의 `APPS` 리스트에 항목을 하나 더 넣고 다시 돌리면 된다.

## 배포

`main` 브랜치에 푸시하면 GitHub Pages가 자동 배포한다.
Settings → Pages → Source = `Deploy from a branch` / `main` / `/ (root)`.

배포 후 확인:

- https://hyesun5464.github.io/
- https://hyesun5464.github.io/app-ads.txt ← **텍스트 한 줄**이 그대로 보여야 한다
- https://hyesun5464.github.io/my-star/privacy.html
- https://hyesun5464.github.io/daesa-note/privacy.html
