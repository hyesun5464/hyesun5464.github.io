# 대사노트 · Line Memorizer

**대사를 가리고, 떠올리고, 한 문장씩 확인하는 대본 암기·리딩 연습 앱입니다.**

[웹에서 사용하기](https://line-memorizer.com/) · [Google Play](https://play.google.com/store/apps/details?id=com.linememorizer.line_memorizer) · [프로필로 돌아가기](https://github.com/hyesun5464/hyesun5464.github.io/blob/main/portfolio/README.md)

## 앱 화면

<p>
  <img src="https://raw.githubusercontent.com/hyesun5464/hyesun5464/main/assets/line-memorizer-input.png" width="220" alt="대사노트 대본 입력 화면" />
  <img src="https://raw.githubusercontent.com/hyesun5464/hyesun5464/main/assets/line-memorizer-role.png" width="220" alt="대사노트 내 역할 선택 화면" />
  <img src="https://raw.githubusercontent.com/hyesun5464/hyesun5464/main/assets/line-memorizer-practice.png" width="220" alt="대사노트 한 문장씩 공개하는 연습 화면" />
</p>

대본 입력 → 내 역할 선택 → 한 문장씩 확인하며 연습하는 흐름입니다.

## 해결하려는 문제

대본을 계속 읽는 것과 보지 않고 대사를 떠올리는 것은 다릅니다. 종이나 일반 메모에서 내 대사만 가리고 확인하는 작업을 반복해야 하는 불편을 줄이고자 했습니다.

## 핵심 사용 흐름

1. 대본을 붙여넣거나 텍스트 기반 PDF에서 가져옵니다.
2. 연습할 역할을 선택하고 해당 역할의 대사를 가립니다.
3. 대사를 떠올린 뒤 ‘다음 문장 보기’로 확인합니다.
4. 필요한 구간을 반복하고, 리딩을 녹음해 다시 들어봅니다.

## 주요 기능

- 문장·화자 단위 대본 분리
- 역할별 대사 가리기와 한 문장씩 공개
- 대본 저장과 연습 진행 상태 이어하기
- 녹음·재생 및 대본별 회독 기록
- Android와 웹에서 사용할 수 있는 Flutter 기반 앱

기능과 제공 범위는 플랫폼 및 앱 버전에 따라 다를 수 있습니다.

## 제작 과정에서 중요하게 본 점

| 고민 | 설계 방향 |
|---|---|
| 연습을 시작하기 전에 설정이 많으면 번거롭습니다. | 대본 입력에서 실행과 역할 선택으로 이어지는 흐름을 구성했습니다. |
| 대사를 공개할 때 화면이 크게 움직이면 읽던 위치를 잃기 쉽습니다. | 내 대사의 공간을 유지하고 공개된 줄을 따라갈 수 있도록 구성했습니다. |
| 연습이 한 번으로 끝나지 않습니다. | 저장한 대본의 진행 상태를 이어가고 회독수를 확인할 수 있게 했습니다. |
| 소리 내어 읽은 결과도 확인하고 싶습니다. | 같은 연습 흐름에서 녹음과 재생을 사용할 수 있게 했습니다. |

## 맡은 역할과 작업 방식

개인 프로젝트로 기능 기획, 사용 흐름 결정, AI 도구를 활용한 구현, 사용 점검, 배포와 운영을 진행합니다. 구현 과정에는 Claude Code와 Codex 등을 활용합니다.

## 프로젝트에서 활용한 기술

Flutter · Dart · Riverpod · 로컬 저장 · 녹음/재생 · PDF 텍스트 추출

## 운영과 개선

사용자 문의를 통해 입력 방식과 암기 연습 과정에서 생기는 요구를 확인하고 개선 항목을 검토합니다. 이 소개에는 이미지 OCR처럼 검토 중인 기능을 현재 제공 기능으로 포함하지 않았습니다.

---

이 문서는 공개용 프로젝트 소개입니다. 앱 소스 코드와 사용자 자료는 포함하지 않습니다.
