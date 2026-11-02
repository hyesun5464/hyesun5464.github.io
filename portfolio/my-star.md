# My Star

**집중하기 전에 보상을 정하고, 완료한 작은 성취를 별로 모으는 집중 타이머 앱입니다.**

[Google Play](https://play.google.com/store/apps/details?id=com.dohae.my_star) · [공식 소개](https://hyesun5464.github.io/my-star/) · [프로필로 돌아가기](https://github.com/hyesun5464/hyesun5464.github.io/blob/main/portfolio/README.md)

## 앱 화면

<p>
  <img src="https://raw.githubusercontent.com/hyesun5464/hyesun5464/main/assets/my-star-home.png" width="230" alt="My Star 홈 화면" />
  <img src="https://raw.githubusercontent.com/hyesun5464/hyesun5464/main/assets/my-star-focus.png" width="230" alt="My Star 집중 타이머 화면" />
</p>

<p>
  <img src="https://raw.githubusercontent.com/hyesun5464/hyesun5464/main/assets/my-star-rewards.png" width="230" alt="My Star 보상 목록" />
  <img src="https://raw.githubusercontent.com/hyesun5464/hyesun5464/main/assets/my-star-idea-pack.png" width="230" alt="My Star 아이디어팩" />
</p>

<p>
  <img src="https://raw.githubusercontent.com/hyesun5464/hyesun5464/main/assets/my-star-completion.png" width="230" alt="My Star 집중 완료와 별 획득" />
  <img src="https://raw.githubusercontent.com/hyesun5464/hyesun5464/main/assets/my-star-constellation.png" width="230" alt="My Star 밤하늘 별자리" />
</p>

## 해결하려는 문제

해야 할 일을 알아도 시작하기 어려울 때가 있습니다. My Star는 집중을 마친 뒤 받을 보상을 미리 정해 두고, 완료 후 보상을 뽑는 과정으로 시작에 대한 기대를 만들고자 했습니다.

## 핵심 사용 흐름

1. 커피 마시기, 웹툰 읽기처럼 자신이 원하는 보상을 등록합니다.
2. 집중할 시간을 정하고 타이머를 시작합니다.
3. 줄어드는 면적으로 남은 시간을 확인합니다.
4. 집중을 완료하면 보상을 뽑고 별을 모읍니다.

## 주요 기능

- 사용자가 직접 등록하는 보상과 보상 뽑기
- 남은 시간을 면적으로 보여주는 시각 타이머
- 집중 완료 후 별 적립과 별자리 시각화
- 집중 기록 확인
- 중단해도 모은 별을 차감하지 않는 구조

기능과 제공 범위는 앱 버전에 따라 다를 수 있습니다.

## 제작 과정에서 중요하게 본 점

| 고민 | 설계 방향 |
|---|---|
| 먼 미래의 성과만으로는 시작이 어려울 수 있습니다. | 사용자가 원하는 보상을 먼저 등록하게 했습니다. |
| 숫자만으로 남은 시간을 체감하기 어렵습니다. | 시간이 면적으로 줄어드는 시각 타이머를 구성했습니다. |
| 중단한 경험이 다시 시작하는 부담이 될 수 있습니다. | 중단해도 기존 별을 차감하지 않도록 했습니다. |
| 작은 완료가 잘 드러나지 않습니다. | 집중 완료를 별과 별자리로 표현했습니다. |

이는 사용 경험을 위한 설계 의도이며, 집중력 개선 효과를 측정하거나 보장하는 주장은 아닙니다.

## 맡은 역할과 작업 방식

개인 프로젝트로 서비스 기획, 보상 흐름과 화면 구성 결정, AI 도구를 활용한 구현, 사용 점검, Android 배포와 운영을 진행합니다. 구현 과정에는 Claude Code와 Codex 등을 활용합니다.

## 프로젝트에서 활용한 기술

Flutter · Dart · Riverpod

## 다음 개선의 기준

보상을 등록하고 집중을 시작하기까지의 흐름이 이해하기 쉬운지, 중단 후에도 다시 시작하기 편한지를 중심으로 사용 경험을 살핍니다.

---

이 문서는 공개용 프로젝트 소개입니다. 앱 소스 코드와 사용자 자료는 포함하지 않습니다.
