# hyesun5464.github.io

My Star 앱의 공식 웹사이트. AdMob `app-ads.txt` 인증과 Google Play 등록에 필요한
개인정보처리방침 · 이용약관을 호스팅한다.

## 파일

| 파일 | 용도 |
|---|---|
| `index.html` | 앱 소개 랜딩 페이지 (Play Console "웹사이트" 칸에 넣는 주소) |
| `app-ads.txt` | AdMob 인증용. **반드시 저장소 루트**에 있어야 한다 |
| `privacy.html` | 개인정보처리방침 (Play Console 필수 URL) |
| `terms.html` | 이용약관 |
| `style.css` | 세 페이지 공용 스타일 |
| `.nojekyll` | Jekyll 빌드 우회 — 파일을 올린 그대로 서빙 |

## 배포

`main` 브랜치에 푸시하면 GitHub Pages가 자동 배포한다.
Settings → Pages → Source = `Deploy from a branch` / `main` / `/ (root)`.

배포 후 확인할 주소:

- https://hyesun5464.github.io/
- https://hyesun5464.github.io/app-ads.txt  ← 브라우저에 **텍스트 한 줄**이 그대로 보여야 한다
- https://hyesun5464.github.io/privacy.html
- https://hyesun5464.github.io/terms.html

## 방침·약관 내용을 고칠 때

원문은 이 저장소가 아니라 앱 저장소(`my_star`)의 `docs/privacy_policy.md`,
`docs/terms_of_service.md`다. 원문을 고친 뒤 아래를 돌려 `privacy.html` /
`terms.html`을 재생성하고, 결과를 이 저장소에 복사해 푸시한다.

```
pip install markdown
python tool/build_site.py
```

## app-ads.txt 메모

내용은 AdMob 퍼블리셔 계정 한 줄뿐이다.

```
google.com, pub-8649405134895595, DIRECT, f08c47fec0942fa0
```

AdMob 크롤러는 **도메인 루트**만 본다. 하위 경로(`/my-star/app-ads.txt`)에 두면
인증되지 않는다. Play Console → 성장 → 스토어 등록정보 → **스토어 설정** →
"스토어 등록정보 연락처 세부정보"의 웹사이트 칸이 `https://hyesun5464.github.io/`
와 정확히 일치해야 한다.
