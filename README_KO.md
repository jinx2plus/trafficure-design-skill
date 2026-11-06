# TraffiCure 스타일 참고 UI Skill

Lepton Software 및 **TraffiCure** 홈페이지에서 확인되는 콘텐츠 구성과 교통정보 중심 UI 패턴을 참고해 만든 **비공식·독립형 디자인 스킬**입니다. 도로망·혼잡도 지도, 운영 KPI, 알림 패널, B2B 서비스 랜딩 페이지를 설계할 때 사용할 수 있습니다.

> **중요:** Lepton Software의 공식 디자인 가이드가 아닙니다. HEX 코드·글꼴·간격은 공식 CSS를 추출한 값이 아니라 본 프로젝트에서 제안한 재사용용 토큰입니다. 로고 및 사이트 이미지는 복제하지 않았습니다.

## 무엇이 들어 있나?

| 경로 | 역할 |
|---|---|
| `.agents/skills/trafficure-inspired-ui/SKILL.md` | Codex용 디자인 스킬 |
| `.claude/skills/trafficure-inspired-ui/SKILL.md` | Claude Code용 디자인 스킬 |
| `theme/tokens.css` | 색상·서체·간격·반경 등의 디자인 토큰 |
| `theme/components.css` | 버튼, 카드, 지도, KPI 및 반응형 구성 |
| `examples/dashboard.html` | 가상 교통 관제 대시보드 웹 예제 |
| `examples/preview.svg` | GitHub에서 바로 볼 수 있는 예시 화면 |
| `references/site-audit.md` | 확인된 웹사이트 특징과 확인 불가 사항 구분 |
| `references/implementation-guide.md` | 실제 제작에 활용할 프롬프트 및 UI 규칙 |
| `scripts/validate.py` | 기본 파일 구성·색상 대비 자동 검사 |

## 적용 방법

이 저장소를 프로젝트 폴더로 연 뒤 다음과 같이 지시합니다.

> `trafficure-inspired-ui` 스킬을 사용해 한국어 ITS 교통관제 대시보드를 만들어줘. 지도·구간 속도·혼잡도·돌발 이벤트·예측 지표를 보여주고, 업데이트 시각과 범례를 포함해. 가상 데이터는 DEMO로 명확하게 표시하고 모바일에도 대응해.

**Codex 전역 등록(Windows PowerShell)**

```powershell
Copy-Item -Recurse -Force .\.agents\skills\trafficure-inspired-ui "$HOME\.codex\skills\trafficure-inspired-ui"
```

**Claude Code 전역 등록(Windows PowerShell)**

```powershell
Copy-Item -Recurse -Force .\.claude\skills\trafficure-inspired-ui "$HOME\.claude\skills\trafficure-inspired-ui"
```

CSS 및 참고문서를 자동으로 활용하려면 이 저장소를 함께 열어 주세요.

## 소스 및 검토일

2026년 11월 6일 기준: [Lepton Software](https://leptonsoftware.com/) · [TraffiCure](https://leptonsoftware.com/trafficure/). 기능/색상 관련 출처와 한계는 `references/site-audit.md`를 참고하세요.
