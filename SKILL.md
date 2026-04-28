---
name: design-skill
description: |
  Apple 디자인 엔진. 4층 콘텐츠→디자인 매핑. 6포맷·6톤·18패턴. md 이쁘니·HTML C8/C9 CORE. 키사스=young-playful 디폴트.
  P1: 디자인스킬, 디자인, 애플디자인, 미니멀, 이쁘니, 반응형, 시각화, 차트, 다이어그램, 인포그래픽, 빅넘버, 영톤, 플레이풀, young-playful, 키사스.
  P2: 디자인해줘, 이쁘니 해줘, 시각화해줘, 영하게, design this, visualize.
  P3: Apple design, responsive, visualization, young-playful, K-12 style, kisas design.
  P4: 산출물 생성시, 디자인 요청시, HTML 시각요소 필요시.
  P5: .html, .md, .pptx, .docx, .xlsx, .pdf.
  NOT: UI설계(→ui-action-designer), 옵시디언문법(→obsidian-markdown).
"@uses":
  - references/tokens.md
  - references/snippets.md
  - references/forbidden.md
  - references/qc.md
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
  - references/tone-young-playful.md
  - references/protocol-pretty.md
  - references/engine-4layer.md
  - references/ux-principles.md
  - references/core-rules.md
  - references/gotchas-extended.md
  - references/responsive.md
  - references/visualization-html.md
---

# Design Skill

디자인스킬(design-skill)은 Apple 디자인 원리 기반의 4층 엔진으로, 콘텐츠→시각화 매핑을 통해 인포그래픽·빅넘버·애플디자인 패턴을 6포맷(md·HTML·PPTX·DOCX·XLSX·PDF) 전체에 적용합니다.

콘텐츠가 디자인을 결정한다. Apple KR 20 페이지 기반 4층 엔진.

---

## §-1. 프로젝트 컨텍스트 분기 (Tone Preselect)

톤 판단(§4 Step2) 전에 프로젝트 컨텍스트를 선감지해 디폴트 톤을 바꾼다.

| 컨텍스트 감지 | 디폴트 톤 | 근거 |
|---------------|-----------|------|
| 프로젝트 CLAUDE.md에 `project: kisas` / 대화에 "키사스/kisas" / 명시 호출("영톤·플레이풀") | `young-playful` | K-12 Apple 교육 페이지 앵커 |
| 그 외 | 기존 5톤 중 콘텐츠 매칭 (warm-human / clean-info / dark-cinema / pro-grid / story-dark) | 기존 엔진 |

**오버라이드:** 사용자가 톤을 명시 지정하면 컨텍스트보다 우선. 예: 키사스 프로젝트에서도 "미니멀하게 가줘" → clean-info.
**C3 예외:** young-playful 선택 시 `tone-young-playful.md` 팔레트(형광펜 5색 + 블록배경 5색)가 C3 "유채색 1색"을 오버라이드한다. G8(그래디언트 1회)은 유지.

---

## 4블록 참조 구조

html-skill-refactor spine 공통 구조. 허브형 스킬 특성상 **4블록은 인덱스 역할**. 풀스펙은 기존 20개 스포크에 유지.

| 블록 | 역할 | 로드 시점 |
|------|------|-----------|
| `references/tokens.md` | 공통 토큰 인덱스 (타이포 5스케일·색 3티어·Oxford Blue·반응형 clamp) → core-rules·responsive·format-* | §1 CORE 진입시 1회 |
| `references/snippets.md` | 포맷×톤 스니펫 인덱스 → format-*·tone-*·engine 스포크 | §4 Step3·Step6 |
| `references/forbidden.md` | 금지 카탈로그 (CORE FAIL 9·GUARD 8·HTML R1~R11·MD 8·Obsidian 14·PPTX·PDF) | §3 GUARD + §4 Step7 |
| `references/qc.md` | 6층 QC 스코어카드 (CORE 9 trans·GUARD 8·포맷별 체크·정적게이트) | §4 Step7 QC |

**로딩 규칙:** 4블록은 **인덱스**라 가볍게 항상 참조. 실제 상세는 기존 스포크로 위임 (최대 3스포크 룰 유지).

---

## 라우팅

**로딩 규칙:** 작업당 최대 3스포크 — format 1 + tone 1 + (md→`protocol-pretty.md` | HTML→`visualization-html.md`). `engine-4layer.md`=§2 진입시 1회. `special-features.md`=S9·S14~S16 매칭시. `ux-principles.md`=CORE FAIL 후 QC 재검시. `visualization-html.md`=HTML 생성시 1회(C9).

| 포맷 | 로드 |
|------|------|
| HTML | `format-html.md` + `visualization-html.md`(C9 필수) |
| MD | `format-md.md` + `protocol-pretty.md` |
| PPTX | `format-pptx.md` (압축 포함) |
| DOCX/XLSX | `format-docx.md` / `format-xlsx.md` |
| PDF | `format-pdf.md` (톤이 방향 결정) |
| 특수기능 | `special-features.md` |
| 톤조정 | `tone-{preset}.md` |
| 4층 | `engine-4layer.md` |

**우선순위:** tone > format > CORE 기본값. CORE FAIL 규칙(C1~C9)은 톤으로도 오버라이드 ✗ — 예외는 §0 공리 부명제로 정당화.

---

## §0. 공리 — 4개

규칙표에 없으면 공리로 판단.

| # | 공리 | 도출 |
|---|------|------|
| X1 | 인지 유한성 | C3·C4·C6 |
| X2 | 위계 효율 | C1·C2·C5 |
| X3 | 리듬 원리 | C5·C7 |
| X4 | 여백 증폭 | C4 |

**부명제:** X2-a(고밀도=위계 간격 축소. clean-info C1 조정). 도출불가 → 형 확인.
**UX 매핑(Nielsen10+Norman5):** → `ux-principles.md#G_AXIOM_MAPPING`. CORE 위반시 동시 점검.

---

## §1. CORE — 9규칙

위반 불가. 톤(L1) 결정 시 자동 세팅.

| # | 원칙 | 규칙 | 판정 | 공리 |
|---|------|------|------|------|
| C1 | 타이포 비율 | L1:L2:L3:L4 = 4:2.3:1.5:1 (±10%) | 이탈→FAIL | X2 |
| C2 | Weight 대비 | 제목wght − 본문wght ≥ 600 (제목 Black 900 ↔ 본문 Light 300 기본) | <600→FAIL | X2 |
| C3 | 3색 시스템 | 배경 흰/검/밝은그레이, 유채색=CTA 1색(기본 #0066cc, Oxford Blue #002147 등록). 그래디언트=요청시. **라이트 배경=캔디 A 팔레트, 다크 배경=파스텔** (→ tokens.md §컬러풀 카드 팔레트). **카드/박스 안 텍스트는 항상 검정 — 흰글자는 검정 배경에서만 예외** | 유채색2+→FAIL | X1 |
| C4 | 여백 | 콘텐츠 ≤55% (xlsx: 행×1.2·열×1.3) | >55%→경고 | X4 |
| C5 | 정렬 이분법 | 제목=중앙, 본문=좌. 병렬시 제목좌 허용. md면제 | 본문중앙→FAIL | X2·X3 |
| C6 | 이미지-텍스트 분리 | 오버레이 ✗ | 오버레이→FAIL | X1 |
| C7 | 반복 금지 | 레이아웃·밀도 3연속 ✗ | 3연속→경고 | X3 |
| C8 | 반응형(HTML/웹MD) | clamp·viewport·터치≥44·≤640 1열·횡스크롤✗ | 위반→FAIL | X1·X4 |
| C9 | 시각 전환(HTML/웹MD) | 시각소스 블록은 시각요소로 전환: 수치비교→차트, 프로세스→플로우, 시간축→타임라인, 관계→다이어그램, 핵심수치→big-number, 2축→매트릭스 | 소스2+ & 요소0→FAIL | X1·X2 |

**세부:** `core-rules.md`(폰트·CTA 보조), `responsive.md`(C8), `visualization-html.md`(C9).

---

## §2. 4층 엔진

`L1 문서(톤) → L2 섹션(역할) → L3 블록(패턴) → L4 요소(포인트)`

풀매칭표·충돌해결 → `engine-4layer.md`.

- **L1** 6톤(dark-cinema/warm-human/clean-info/pro-grid/story-dark/young-playful) — young-playful는 §-1 컨텍스트 분기로 선감지
- **L2** 7역할(히어로·기능·증거·비교·CTA·클로징·부록) + 배경교대(C7)
- **L3** 12 콘텐츠형태 → S1~S18, 충돌시 [톤친화도→구조서열] 2단계
- **L4** 자동(S1·S9·S12) + 수동(S14~S16)

---

## §3. GUARD — 패턴 과용 방지

CORE=하한선(FAIL), GUARD=S패턴 과용(경고→수정).

| # | 규칙 | 판정 |
|---|------|------|
| G1 | 이미지 비율 3종↓ | 4+→경고 |
| G2 | 섹션당 CTA 2↓ | 3+→FAIL |
| G3 | 인용문 ≥L2 | L3↓→경고 |
| G4 | 테이블 6열↓ | 7+→분할 |
| G5 | 폰트 단계 4↓ | 5+→FAIL |
| G6 | S7 감성선언 2회↓ | 3+→경고 |
| G7 | S9 형광펜 블록당 2구↓ | 3+→경고 |
| G8 | S14 그래디언트 1회 | 2+→FAIL |

---

## §4. 워크플로우

```
1. 콘텐츠 수신
1-b. §-1 컨텍스트 분기 체크 (프로젝트=키사스 → young-playful 프리셀렉트)
2. L1 톤 판단 (확신도<70 → 형 1줄 확인). 프리셀렉트 있으면 해당 톤 우선
3. 포맷 결정 → format 1 + tone 1 로드 (md=+pretty, HTML=+visualization)
4. L2 섹션 분해 + 역할 + 리듬
5. L3 블록 신호 → 패턴 매칭 (충돌시 engine-4layer 2단계)
6. L4 요소 포인트 (자동+수동)
7. QC: CORE9 + GUARD8 + UX_MAPPING
   ├─ md → protocol-pretty QC(①~⑧)
   ├─ HTML → C8(viewport·clamp·터치·1열·횡스크롤) + C9(시각소스→요소 전환율)
   ├─ HTML 정적게이트 → `bash scripts/qc-mobile.sh output.html` (R2·R4b·R8·R9·R10·R11·R1a 검출)
   ├─ FAIL → 롤백(C1~C5·C8·C9→Step4, G→Step6). 3회 FAIL → 형
8. 출력
```

---

## §5. 스킬 연동

- **pptx/docx/xlsx/pdf:** design-skill=값, 해당스킬=기술
- **html-div-style:** 옵시디언 md+div. design-skill 완료 후 cascade
- **ui-action-designer:** PRD·HTML 생성시 cascade. 대화분석만=skip
- **protocol-pretty(이쁘니):** md 시각문법 SSOT. `protocol-pretty.md`
- **apple-design-style:** 대체됨

---


## §INV NO_WORK_LABEL (산출물·대화 본질 보호)

| 항목 | 정의 |
|------|------|
| RULE | 산출물·대화 = 인간 언어. 작업 라벨 ZERO. (1만 페이지 1단어 = FAIL) |
| 판정 | "이 단어, 이 대화 밖 사람이 사전 없이 읽을 수 있나?" NO → 작업 라벨 → 금지 |
| ALLOW | 업계 전문용어(CSS·HTML·SVG·UX·UI·CTA·CSS변수·flexbox·grid·viewport·Apple HIG) · 고유명사(Apple·KISAS) |
| CONVERT | 라벨 발견 → 실명·평문 풀어쓰기. 예) "4층 콘텐츠→디자인 매핑·6포맷·6톤·18패턴·C8/C9" → 결과만 노출 / "young-playful·이쁘니" → 톤 결과 평문 |
| SELF_CHECK | 최종 시각자료 출력 직전에서 자체 스캔. 1개라도 발견 = 차단·재작성. paper-engine cascade 경유 시 INV 13 자동 적용 |

---

## Gotchas

- **톤 과신:** 확신도<70 → 형 1줄 확인
- **S패턴 과적용:** 블록당 2개+ ✗. 충돌 → engine-4layer 2단계
- **L2 7역할 미포괄:** FAQ·용어집 등 유사 역할 매핑, 확신 ✗ → 형 확인
- **UX가 CORE 덮어쓰기:** CORE 우선. UX는 해석 보강만
- **engine-4layer 미로드 §2 진입:** §2 진입시 반드시 1회 로드
- **C8 4함정:** 고정px·viewport누락·고정다열·고정포맷강제 → `responsive.md`
- **C9 3함정:** HTML표·문장만·ASCII다이어그램·CDN차트라이브러리의존 → `visualization-html.md`

**세부 함정:** → `gotchas-extended.md`

---

## Version

- v1.7 (2026-04-23) — html-skill-refactor spine 적용. 4블록 인덱스(tokens·snippets·forbidden·qc) 추가, 기존 20스포크 유지.
- v1.6 (2026-04-23) — C8 반응형 6규칙 추가. `scripts/qc-mobile.sh` 정적 게이트 신설.
- v1.5 (2026-04-20) — young-playful 톤 신설 (K-12 Apple). §-1 프로젝트 컨텍스트 분기 추가.
- v1.4 (2026-04-20) — C9 시각 전환 CORE 신설, visualization-html.md 추가.
