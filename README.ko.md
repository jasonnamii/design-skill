# design-skill

> 🇺🇸 [English README](./README.md)

**Apple 디자인 엔진: 4층 콘텐츠→디자인 자동 매핑. 6포맷·5톤·18패턴.**

## 사전 요구

- **Claude Cowork 또는 Claude Code** 환경

## 목표

design-skill은 Apple급 디자인 원칙을 결정론적 파이프라인으로 인코딩하여 임의적 스타일링 판단을 제거합니다. 콘텐츠가 입력되면 엔진이 톤을 자동 감지하고, 섹션 역할을 부여하고, 블록 패턴을 선택한 뒤, 요소 수준 포인트 디자인을 적용합니다 — 4개 공리와 7개 불변 핵심 규칙이 전 과정을 지배합니다.

## 사용 시점 & 방법

시각적으로 정돈된 결과물이 필요할 때 호출합니다 — 문서, 프레젠테이션, 대시보드, 웹페이지, 옵시디언 노트 등. "만들어줘", "이쁘게", "디자인해줘" 등의 요청에 자동 발동되며, 포맷별 스킬(pptx, docx, xlsx, pdf, html-div-style)로 캐스케이드합니다.

## 사용 사례

| 상황 | 프롬프트 | 동작 |
|---|---|---|
| 보고서 디자인 | `"깔끔하게 만들어줘"` | 톤 자동감지→섹션 역할→블록 패턴 선택→포맷별 산출 |
| 프레젠테이션 | `"이쁘니 해줘"` | 4층 엔진이 타이포그래피 비율, 3색 시스템, 여백 규칙 적용 |
| 옵시디언 노트 | `"디자인 적용해줘"` | md 시각문법(이쁘니 프로토콜)으로 위계·리듬·여백 적용 |
| 데이터 대시보드 | `"디자인해줘"` | pro-grid 톤→비교/근거 패턴→≤55% 콘텐츠 밀도 |

## 아키텍처

### 4대 공리
- **X1 인지 유한성** — 뷰당 정보량 제한
- **X2 위계 효율** — 시각적 무게가 읽기 순서를 안내
- **X3 리듬 원칙** — 밀도 교대로 피로 방지
- **X4 여백 증폭** — 빈 공간이 인접 콘텐츠를 증폭

### 7대 핵심 규칙 (불변)
타이포그래피 비율(4:2.3:1.5:1), 폰트 웨이트 대비(≥300), 3색 시스템, 여백 철학(≤55% 콘텐츠), 정렬 이분법, 텍스트-이미지 분리, 반복 금지 리듬.

### 4층 엔진
1. **톤 자동감지** — dark-cinema · warm-human · clean-info · pro-grid · story-dark
2. **섹션 역할** — hero · feature intro · evidence · comparison · CTA · closing · appendix
3. **블록 패턴** — 콘텐츠 유형별 18개 패턴(S1–S18) 매핑
4. **요소 수준 포인트 디자인** — 미시적 타이포그래피, 간격, 악센트 결정

### 6개 출력 포맷
| 포맷 | 참조 파일 | 캐스케이드 대상 |
|---|---|---|
| HTML | `format-html.md` | 단독 또는 html-div-style |
| Markdown | `format-md.md` | 옵시디언 via protocol-pretty |
| PPTX | `format-pptx.md` | pptx 스킬 |
| DOCX | `format-docx.md` | docx 스킬 |
| XLSX | `format-xlsx.md` | xlsx 스킬 |
| PDF | `format-pdf.md` | pdf 스킬 |

### 5개 톤 프리셋
`tone-dark-cinema` · `tone-warm-human` · `tone-clean-info` · `tone-pro-grid` · `tone-story-dark`

## 연동 스킬

- **[deliverable-engine](https://github.com/jasonnamii/deliverable-engine)** — 문서 구조·품질; design-skill이 시각 레이어 담당
- **[html-div-style](https://github.com/jasonnamii/html-div-style)** — 옵시디언 안전 HTML div 래퍼
- **[ui-action-designer](https://github.com/jasonnamii/ui-action-designer)** — UI/UX 설계; design-skill이 시각 스타일링 담당

## 설치

```bash
git clone https://github.com/jasonnamii/design-skill.git ~/.claude/skills/design-skill
```

## 업데이트

```bash
cd ~/.claude/skills/design-skill && git pull
```

`~/.claude/skills/`에 배치된 스킬은 Claude Code 및 Cowork 세션에서 자동으로 사용 가능합니다.

## Cowork Skills

25개 이상의 커스텀 스킬 중 하나입니다. 전체 카탈로그: [github.com/jasonnamii/cowork-skills](https://github.com/jasonnamii/cowork-skills)

## 라이선스

MIT License — 자유롭게 사용, 수정, 공유 가능합니다.
