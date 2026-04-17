---
name: design-skill
description: |
  Apple 디자인 엔진. 4층 콘텐츠→디자인 자동 매핑. 6포맷·5톤·18패턴. 공리 4개. md 이쁘니 프로토콜. HTML/웹MD 모바일 반응형 기본(C8 CORE).
  P1: 디자인스킬, design skill, 디자인, 애플디자인, 심플디자인, 미니멀디자인, 깔끔하게, 이쁘게만들어, 디자인적용, 이쁘니, 반응형디자인, 모바일디자인.
  P2: 디자인해줘, 만들어줘, 적용해줘, 꾸며줘, 이쁘니 해줘, design this, apply design, style this.
  P3: Apple design, minimal design, content-driven, responsive, mobile-first.
  P4: 산출물 생성시, 문서 디자인 요청시, 포맷 스킬 cascade시, md 시각문법 적용시.
  P5: .html로, .md로, .pptx로, .docx로, .xlsx로, .pdf로.
  NOT: UI설계(→ui-action-designer), 옵시디언문법(→obsidian-markdown), 산출물구조.
"@uses":
  - references/format-html.md
  - references/format-md.md
  - references/format-pptx.md
  - references/format-docx.md
  - references/format-xlsx.md
  - references/format-pdf.md
  - references/special-features.md
  - references/tone-dark-cinema.md
  - references/tone-warm-human.md
  - references/tone-clean-info.md
  - references/tone-pro-grid.md
  - references/tone-story-dark.md
  - references/protocol-pretty.md
  - references/engine-4layer.md
  - references/ux-principles.md
  - references/core-rules.md
  - references/gotchas-extended.md
  - references/responsive.md
---

# Design Skill

콘텐츠가 디자인을 결정한다 (매체 제약에 의한 최소 압축 허용). Apple KR 20개 페이지 기반 4층 디자인 엔진.

---

## 라우팅

### 로딩 규칙

- **1회 작업당 최대 3개 스포크** — format spoke 1개 + tone spoke 1개 + (md 포맷일 때) `protocol-pretty.md`
- **`engine-4layer.md`는 §2 진입 시 1회 로드** (§2 워크플로우 진입 시점에만)
- **`special-features.md`는 S9·S14·S15·S16 등 패턴 매칭 시에만 로드**
- **`ux-principles.md`는 CORE FAIL 발생 후 QC 재검 시 1회 로드** (§G AXIOM_UX_MAPPING 참조)

| 출력 포맷 | 로드 대상 | 비고 |
|-----------|-----------|------|
| HTML | → `references/format-html.md` | |
| Markdown (.md) | → `references/format-md.md` + `references/protocol-pretty.md` | |
| PPTX | → `references/format-pptx.md` | 콘텐츠 압축 규칙 포함 |
| DOCX | → `references/format-docx.md` | |
| XLSX | → `references/format-xlsx.md` | |
| PDF | → `references/format-pdf.md` | 톤이 페이지 방향 결정 (dark-cinema/story-dark=landscape) |
| 특수 기능 (형광펜, 그래디언트 등) | → `references/special-features.md` | "해당 없음" fallback 규칙 포함 |
| 톤 세부조정 필요시 | → `references/tone-{preset}.md` | |
| 4층 엔진 매칭표 | → `references/engine-4layer.md` | L1~L4 표 풀텍스트 |

**충돌 시 우선순위**: tone spoke > format spoke > CORE 기본값.
톤이 문서 전체의 분위기를 결정하므로, 포맷의 기본 구현을 톤이 오버라이드한다.
단, CORE 중 FAIL 판정 규칙(C1~C7)은 톤으로도 오버라이드 불가 — 예외 시 §0 공리에서 도출한 부명제로 정당화 필수 (§1 CORE 예외 참조).

---

## §0. 공리 — 4개 자명명제

모든 규칙의 근거. 규칙표에 없는 상황에서는 이 공리로 돌아가 판단한다.

| # | 공리 | 의미 | 도출 규칙 |
|---|------|------|-----------|
| X1 | **인지 유한성** | 인간의 주의·작업기억은 유한하다 | → C3(3색), C4(여백), C6(분리) |
| X2 | **위계 효율** | 시각적 크기·무게 차이가 클수록 중요도 서열이 빠르게 인지된다 | → C1(타이포 비율), C2(Weight 대비), C5(정렬) |
| X3 | **리듬 원리** | 반복은 예측을 생성하고, 변화는 주의를 환기한다 | → C5(정렬 이분법), C7(반복 금지) |
| X4 | **여백 증폭** | 빈 공간은 인접 요소의 지각적 존재감을 높인다 | → C4(여백 철학) |

**부명제:** X2-a(고밀도=위계 간격 축소→탐색효율. clean-info C1 조정). 규칙 외 → 공리. 도출불가 → 형 확인.

**공리↔UX 매핑(Nielsen10+Norman5):** → `references/ux-principles.md#G_AXIOM_MAPPING`. QC CORE 위반시 대응 UX 원리 동시 점검.

---

## §1. CORE — 견고 규칙 7개

모든 포맷·톤·상황에서 위반 불가. 톤(L1)이 정해지면 CORE 값은 자동 세팅된다.

| # | 원칙 | 규칙 | 판정 | 공리 근거 |
|---|------|------|------|-----------|
| C1 | 타이포 비율 | L1:L2:L3:L4 = 4:2.3:1.5:1 (±10%) | 이탈→FAIL | X2 |
| C2 | Weight 대비 | 제목wght − 본문wght ≥ 300 | <300→FAIL | X2 |
| C3 | 3색 시스템 | 배경: 흰(#fff)/검(#000~#1d1d1f)/밝은그레이(#f5f5f7). 유채색: CTA 1색만 (기본 #0066cc, 형 override 가능). 그래디언트: 형 요청시만 | 유채색2+→FAIL | X1 |
| C4 | 여백 철학 | 콘텐츠 ≤ 55%, 나머지 여백 (xlsx: 행높이 ×1.2, 열너비 ×1.3으로 번역) | >55%→경고 | X4 |
| C5 | 정렬 이분법 | 제목=중앙, 본문=좌측. 병렬 레이아웃시 제목 좌측 허용. md 중앙정렬 면제 | 본문중앙→FAIL | X2, X3 |
| C6 | 텍스트-이미지 분리 | 이미지 위 텍스트 오버레이 금지. 영역 분리 | 오버레이→FAIL | X1 |
| C7 | 반복 금지 리듬 | 동일 레이아웃 3연속 금지, 동일 밀도 3연속 금지 | 3연속→경고 | X3 |
| C8 | 반응형 | HTML/웹MD 모바일 우선. clamp·viewport·터치≥44px·≤640px 1열·횡스크롤 금지 | 고정px·viewport누락·횡스크롤→FAIL | X1, X4 |

**CORE 보조·예외(폰트·열상한·CTA·톤별 3항):** → `references/core-rules.md`
**C8 반응형 세부(BP·R1~R7·톤별·템플릿):** → `references/responsive.md` (HTML·웹MD 전용)

---

## §2. 4층 디자인 엔진

콘텐츠→디자인 자동 판단 4층 구조:

```
Layer 1 문서전체(톤) → Layer 2 섹션(역할) → Layer 3 블록(패턴) → Layer 4 요소(포인트)
```

**L1~L4 풀 매칭표 + 충돌 해결 2단계:** → `references/engine-4layer.md`

각 층 핵심:
- **L1 톤 자동 판단** — 콘텐츠 신호 → 5개 톤(dark-cinema/warm-human/clean-info/pro-grid/story-dark) 중 1개
- **L2 섹션 역할** — 7개 역할(히어로·기능·증거·비교·CTA·클로징·부록) + 배경색 교대 리듬(C7 보조)
- **L3 블록 패턴 매칭** — 12개 콘텐츠 형태 → S1~S18 패턴 매핑, 충돌 시 [톤 친화도 → 구조성 서열] 2단계 체인
- **L4 요소 포인트** — 자동(S1·S9·S12) + 수동(S14·S15·S16) 트리거

---

## §3. GUARD — 패턴 과용 방지

**CORE = 모든 디자인의 하한선 (위반=FAIL). GUARD = 특정 S패턴의 과용 방지 (위반=경고→수정).**

| # | 규칙 | 판정 |
|---|------|------|
| G1 | 이미지 비율 3종 이내 | 4종+→경고 |
| G2 | 섹션당 CTA 2개 이내 | 3개+→FAIL |
| G3 | 인용문 L2급 이상 크기 | L3이하→경고 |
| G4 | 테이블 열 수 최대 6열 | 7열+→분할 |
| G5 | 페이지당 폰트 크기 4단계 | 5단계+→FAIL |
| G6 | 감성선언(S7) 1문서 2회 이내 ("이 문장이 정말 선언급인가?" 자문) | 3회+→경고 |
| G7 | 형광펜(S9) 1블록 2구절 이내 | 3구절+→경고 |
| G8 | 그래디언트(S14) 1문서 1회 | 2회+→FAIL |

---

## §4. 워크플로우

```
1. 콘텐츠 수신
2. Layer 1: 톤 판단 (형 명시 or 자동추론)
   ├─ 확신도 ≥70 → 3으로
   └─ 확신도 <70 → 형에게 "~톤으로 진행합니다" 1줄 확인 → 3으로
3. 포맷 결정 → 해당 format spoke 1개 + tone spoke 1개 로드
   ├─ md 포맷 → format-md.md + protocol-pretty.md 함께 로드
   └─ 기타 포맷 → 해당 format spoke만
4. Layer 2: 섹션 분해 + 역할 판단 + 리듬 설계
5. Layer 3: 블록별 콘텐츠 신호 탐지 → 패턴 자동 매칭 (충돌 시 engine-4layer.md 2단계 체인)
6. Layer 4: 요소별 포인트 디자인 (자동+수동)
7. QC: CORE 8 + GUARD 8 + UX_MAPPING
   ├─ md → protocol-pretty.md QC(①~⑧)
   ├─ HTML·웹MD → C8 체크(viewport·clamp·터치·1열·횡스크롤)
   ├─ UX_MAPPING → CORE 위반시 N4·N6·N8 동시 점검
   ├─ FAIL → 롤백(C1~C5·C8→Step4, G1~G8→Step6). 3회 FAIL → 형 에스컬레이션
8. 산출물 출력
```

---

## §5. 스킬 연동

- **pptx/docx/xlsx/pdf:** design-skill=디자인값, 해당스킬=기술구현
- **html-div-style:** 옵시디언 md+div 래핑. md+div 사용 시 design-skill 완료 후 cascade 필수
- **ui-action-designer:** UIAD가 아웃풋(PRD .md·HTML) 생성 시 design-skill cascade 필수. 대화문 분석만이면 skip
- **protocol-pretty(이쁘니):** design-skill 산하. md 시각문법 SSOT. `references/protocol-pretty.md`
- **apple-design-style:** 대체됨

---

## Gotchas

- **톤 과신:** 자동추론이 틀릴 수 있다. 확신도 <70이면 형에게 "~톤으로 진행합니다" 1줄 확인.
- **S 패턴 과적용:** 한 블록에 S 패턴 2개 이상 동시 적용 지양. 충돌 시 `engine-4layer.md` L3 2단계 체인 적용.
- **섹션 역할 미포괄:** §2 L2 7개 역할이 FAQ·용어집·타임라인 등 모든 유형을 포괄하지 못함. 유사 역할로 매핑하되 확신 없으면 형에게 확인.
- **UX 원리가 CORE를 덮어쓰려 함:** N7 FLEXIBILITY로 C3 3색 확장하려는 유혹 → CORE 우선. UX 원리는 CORE 내 해석 보강만.
- **engine-4layer 미로드 상태 §2 진입:** L3 충돌 해결 2단계 체인은 허브에 없음. §2 진입 시 반드시 `engine-4layer.md` 1회 로드.
- **C8 반응형 4함정:** 고정px폰트(→clamp)·viewport누락(→메타 필수)·고정 다열 그리드(→auto-fit·미디어쿼리)·고정포맷에 C8 강제(→HTML·웹MD 전용). 상세 → `references/responsive.md`

**포맷·프로토콜별 세부 함정(md 타이포 한계·XLSX 여백·이쁘니 직접수행 금지·md 콜아웃 SSOT·AXIOM_UX_MAPPING 미참조·spoke 배경색 충돌):** → `references/gotchas-extended.md`

---

## Version

- v1.2 (2026-04-18) — C8 반응형 CORE 신설, responsive.md
- v1.1 — 스포크 분리, AXIOM_UX_MAPPING
- v1.0 — 초기
