---
name: design-skill
description: |
  심플·강력 디자인 엔진 v3.2. 4톤(낮/밤×벤또/스크롤) + 믹스 모드 + 6포맷 + 8조 헌법(회색금지·형광펜적극·헤드 900·본문 300). 페르소나 2종(young-playful·KISAS) + Apple Keynote DS 풀스택 자산(scaffold HTML·deck-stage.js).
  P1: 디자인스킬, 애플디자인, 애플벤또, 키노트벤또, 키노트스타일, 벤또그리드, bento grid, 낮모드, 밤모드, 라이트벤또, 다크벤또, 라이트스크롤, 다크스크롤, 큰글자스크롤, 믹스모드, Think패턴, 이쁘니디자인, 디자인반응형, 차트시각화, 다이어그램디자인, 인포그래픽디자인, 빅넘버디자인, 형광펜디자인, 영플레이풀, young-playful, 키사스디자인, KISAS, 마케팅벤또, KPI벤또, 분석벤또, 카드벤또, HTML스캐폴드, 스크롤스캐폴드, 벤또스캐폴드, 덱스테이지, HTML발표, HTML슬라이드, design scaffold.
  P2: 디자인해줘, 이쁘니 해줘, 시각화해줘, 영하게, 벤또로, 키노트로, 낮모드로, 밤모드로, 큰글자로, 믹스로, design this, visualize, transform.
  P3: light bento, dark bento, light scroll, dark scroll, mix mode, responsive, visualization, big number, highlighter, persona young-playful, persona KISAS.
  P4: 산출물 생성시, HTML 시각요소 필요시, 마케팅 분석 한장 압축, KPI 대시보드, 캠페인 복기, 기능 요약 압축.
  P5: .html, .md, .pptx, .docx, .xlsx, .pdf.
  NOT: UI설계(→ui-action-designer), 옵시디언문법(→obsidian-markdown), 일반HTML단순래핑(→html-div-style).
"@uses":
  - references/constitution.md
  - references/color-system.md
  - references/korean-typography.md
  - references/fold-scroll.md
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
  - references/tone-light-bento.md
  - references/tone-dark-bento.md
  - references/tone-light-scroll.md
  - references/tone-dark-scroll.md
  - references/tone-mix.md
  - references/persona-young-playful.md
  - references/persona-kisas.md
  - references/bento-patterns.md
  - references/mode-html-bento.md
  - references/mode-html-scroll.md
  - references/layout-safety.md
  - references/protocol-pretty.md
  - references/engine-4layer.md
  - references/ux-principles.md
  - references/core-rules.md
  - references/gotchas-extended.md
  - references/responsive.md
  - references/visualization-html.md
  - references/scaffold-scroll.html
  - references/scaffold-bento.html
  - references/scaffold-deck.md
---

# Design Skill v3.2

심플·강력 디자인 엔진. **8조 헌법** + **4톤(낮/밤 × 벤또/스크롤)** + **믹스 모드** + 6포맷.

**v3.2 (2026-04-29):** §SELF_CHECK + §INVARIANT 신설·트리거 정밀화·Gotchas 보강 (skill-doctor 처방 4건 반영)

**v3.1 (2026-04-29):** Apple Keynote DS 자산 흡수 (scaffold-scroll·scaffold-bento·deck-stage.js)

**v3.0 (2026-04-29):** 헌법 교체 — 회색 원천 금지, 형광펜 적극, 헤드 무조건 900, 본문 300. 7톤 → 4톤 통폐합 + 믹스. 페르소나 2종 보존.

---

## §HEADER. 8조 헌법 (절대규칙)

| # | 조항 | 판정 |
|---|---|---|
| H1 | 배경 = 검정 OR 흰색 (낮/밤 2분법) | 그라디언트·다른색배경 → FAIL |
| H2 | 컬러풀 = 박스·시각화·형광펜에만 (액센트 6색) | 본문 다채색 → FAIL |
| H3 | 형광펜 적극 사용 (핵심 단어 강조) | 페이지당 0회 → 경고 |
| H4 | 글자색 = 검정·흰색·컬러풀만. **회색 원천 금지** (텍스트·배경·보더) | 회색 사용 → FAIL. 단 §EXCEPT 비활성 폼 한정 허용 |
| H5 | 표지·섹션·본문 헤드 = 가장 굵은 웨이트 (900) | <900 → FAIL |
| H6 | 본문 내용만 가는 웨이트 (300) | ≥600 본문 → FAIL |
| H7 | 최소 폰트 12px (PC 기준). 모바일 clamp는 12 하한 | <12 → FAIL |
| H8 | 반응형 100% — clamp·viewport·터치≥44·≤640 1열·횡스크롤✗·한글줄바꿈 | 위반 → FAIL |

**H 우선:** H1~H8은 톤·포맷·CORE 모두 우선. H 위반은 어떤 정당화도 무효.

---

## §EXCEPT. 회색 예외 (극단)

회색은 **거의** 0%. 다음 케이스만 5% 알파 컬러로 대체:
- 비활성 폼 placeholder → `검정 30% 알파` (낮) / `흰색 30% 알파` (밤)
- 비활성 버튼 → `보라 20% 알파`

**원칙:** "회색 쓰고 싶다 = 알파 낮춘 컬러로 대체". 진짜 #888 같은 회색 = 영구 금지.

---

## §-1. 컨텍스트 분기 (Tone Preselect)

| 감지 | 디폴트 톤 |
|---|---|
| `project: kisas` / "키사스" | `persona-kisas` |
| "영톤·플레이풀·young" | `persona-young-playful` |
| "낮모드·밝게·light·라이트" + "벤또" | `light-bento` |
| "밤모드·어둡게·dark·다크" + "벤또" | `dark-bento` |
| "큰글자스크롤·낮" / "낮 스크롤" | `light-scroll` |
| "큰글자스크롤·밤" / "밤 스크롤" / 디폴트 | `dark-scroll` |
| "믹스·섞어·mix" | `mix` |
| 디폴트 (분석·KPI·마케팅 한장) | `light-bento` |
| 디폴트 (제품·매니페스토·압축 키노트) | `dark-scroll` |

**오버라이드:** 사용자 명시 우선.

---

## §SSOT. 단일 권위 출처

| 블록 | 역할 | 위치 |
|---|---|---|
| `constitution.md` | 8조 헌법 풀버전 + 위반 카탈로그 | SSOT |
| `color-system.md` | 6컬러 팔레트(보라 추가)·형광펜·CSS변수 | SSOT |
| `korean-typography.md` | 헤드 900·본문 300·5단 스케일·12 하한 | SSOT |
| `fold-scroll.md` | 접기/펴기 scrollBy(delta) | SSOT |
| `tokens.md` | 토큰 인덱스 |
| `snippets.md` | 포맷×톤 스니펫 |
| `forbidden.md` | 금지 카탈로그 |
| `qc.md` | 6층 QC 스코어카드 |

본체는 SSOT에만. 다른 곳은 1줄 포인터.

---

## §ROUTING. 라우팅

작업당 최대 3스포크 = format 1 + tone 1 + 보조 1.

| 포맷 | 로드 |
|---|---|
| HTML 벤또 (light/dark) | `format-html` + `mode-html-bento` + `bento-patterns` + `layout-safety` + **`scaffold-bento.html`** |
| HTML 스크롤 (light/dark) | `format-html` + `mode-html-scroll` + `layout-safety` + **`scaffold-scroll.html`** |
| HTML 믹스 | `format-html` + `tone-mix` + 둘 다 |
| **HTML 슬라이드 발표** | `format-html` + **`scaffold-deck.md`** + `assets/deck-stage.js` |
| HTML 일반 | `format-html` + `visualization-html` |
| MD | `format-md` + `protocol-pretty` |
| PPTX/DOCX/XLSX/PDF | `format-{pptx·docx·xlsx·pdf}` |
| 톤 | `tone-{light·dark}-{bento·scroll}.md` 또는 `tone-mix.md` |
| 페르소나 | `persona-{young-playful·kisas}.md` (디폴트 4톤 무시·자체 컬러팔레트) |

**우선순위:** H헌법 > tone > format > CORE 기본값.

---

## §1. CORE — 9규칙 (H헌법 하위)

| # | 원칙 | 규칙 | 판정 |
|---|---|---|---|
| C1 | 타이포 비율 | L1:L2:L3:L4 = 4:2.3:1.5:1 (±10%) | 이탈→FAIL |
| C2 | Weight 대비 | 헤드 900 ↔ 본문 300 (대비 600) | <600→FAIL |
| C3 | 컬러 시스템 | **흰/검 + 6액센트(옐로우·민트·핑크·블루·코랄·보라)**. 본문 다채색 ✗ (H2) | 위반→FAIL |
| C4 | 여백 | 콘텐츠 ≤55% | >55%→경고 |
| C5 | 정렬 이분법 | 제목=중앙·본문=좌. md면제 | 본문중앙→FAIL |
| C6 | 이미지-텍스트 분리 | 오버레이 ✗ | →FAIL |
| C7 | 반복 금지 | 레이아웃·밀도 3연속 ✗ | 3연속→경고 |
| C8 | 반응형 | clamp·viewport·터치≥44·≤640 1열·횡스크롤✗·한글줄바꿈 (H8) | 위반→FAIL |
| C9 | 시각 전환 | 수치→차트, 프로세스→플로우, 시간축→타임라인, 관계→다이어그램, 핵심수치→big-number, 2축→매트릭스 | 소스2+ & 요소0→FAIL |

세부: `core-rules.md`·`responsive.md`·`visualization-html.md`·`color-system.md`.

---

## §2. 4층 엔진

`L1 톤 → L2 섹션 → L3 블록 → L4 요소`

- **L1** 4톤(light-bento·dark-bento·light-scroll·dark-scroll) + 믹스 + 페르소나 2(young-playful·KISAS)
- **L2** 7역할 (히어로·기능·증거·비교·CTA·클로징·부록) + 배경교대(C7)
- **L3** 12 콘텐츠형태 → S1~S18 + 벤또 패턴 A~E
- **L4** 자동(S1·S9·S12) + 수동(S14~S16) + 텍스트多 셀 Type 1~8

풀매칭표·충돌해결 → `engine-4layer.md`.

---

## §3. GUARD — 패턴 과용 방지

| # | 규칙 | 판정 |
|---|---|---|
| G1 | 이미지 비율 ≤3 | 4+→경고 |
| G2 | 섹션 CTA ≤2 | 3+→FAIL |
| G3 | 인용 ≥L2 | L3↓→경고 |
| G4 | 테이블 ≤6열 | 7+→분할 |
| G5 | 폰트 단계 ≤4 | 5+→FAIL |
| G6 | 감성선언 ≤2 | 3+→경고 |
| G7 | **형광펜 페이지당 ≥1 (적극) ~ ≤8 (과용방지)** | 0=경고·9+=FAIL |
| G8 | 그래디언트 ✗ (H1 강제) | 1+→FAIL |

---

## §4. 워크플로우

```
1. 콘텐츠 수신
1-b. §-1 분기 → tone 확정
2. H헌법 8조 사전점검 (배경·컬러·웨이트·폰트하한·반응형)
3. 포맷 결정 → format 1 + tone 1
4. L2 섹션 분해
5. L3 블록 매칭 (벤또 A~E + 텍스트多 1~8)
6. L4 요소
7. QC: H헌법 8 + CORE9 + GUARD8 + UX_MAPPING
   ├─ H 위반 → 즉시 차단 (어떤 정당화도 무효)
   ├─ md → protocol-pretty ①~⑧
   ├─ HTML → C8(viewport·clamp·터치·1열·한글) + C9(전환율) + 회색 grep
   ├─ HTML 정적게이트 → `bash scripts/qc-mobile.sh output.html`
   ├─ 회색 grep → `grep -E '#[0-9a-f]{3,6}|gray|grey' output.html` 매칭 시 H4 위반
   ├─ FAIL → 롤백 (H→Step2·C→Step4·G→Step6·3회 → 형)
8. 출력
```

---

## §5. 스킬 연동

- pptx/docx/xlsx/pdf — design-skill=값, 해당스킬=기술
- html-div-style — 옵시디언 md+div, design-skill 완료 후 cascade
- ui-action-designer — PRD·HTML cascade
- protocol-pretty(이쁘니) — md SSOT

---

## §SELF_CHECK. 자가검증 게이트

스킬 출고 전 자가검증 필수 — 무자각 차단.

```bash
# 1. SKILL.md 무결성 (8헌법 + 9CORE + 8GUARD 카운트·스포크 36개·hub 한도)
python scripts/validate.py ./

# 2. 출력 HTML 8헌법 grep (회색·웨이트·폰트)
bash scripts/qc-mobile.sh output.html

# 3. 회색 위반 grep (H4 절대규칙)
grep -nE '#([0-9a-f]{3}|[0-9a-f]{6})|gray|grey|silver' output.html | \
  grep -vE 'rgba\(' | \
  grep -vE '#000|#fff|#f0c850|#5dcaa5|#ed93b1|#378add|#d85a30|#7f77dd'
# 매칭 = H4 위반·차단

# 4. 본문 굵기 위반 (H6)
grep -nE '<p[^>]*style[^>]*font-weight:\s*[6-9]00' output.html

# 5. 12 미만 폰트 (H7)
grep -nE 'font-size:\s*([0-9]|1[01])px(?!\d)' output.html
```

**실패 처리:** 1개라도 매칭 → STOP·재작성. silent ✗.

---

## §INVARIANT. 절대 보호

| # | 항목 | 위반 결과 |
|---|---|---|
| INV1 | **8조 헌법 H1~H8** (constitution.md) — 어떤 정당화도 무효 | 즉시 차단·재작성 |
| INV2 | **NO_WORK_LABEL** — 산출물·대화 = 인간 언어 | 출력 폐기·재출력 |
| INV3 | **6액센트 팔레트** — 옐로우·민트·핑크·블루·코랄·보라 (변경·추가·삭제 ✗) | 색 추가 시 색 정의 변경 ✗·v 신설 |
| INV4 | **회색 원천 금지 (H4)** — 텍스트·배경·보더 모두 검/흰/액센트만 | grep 매칭 시 즉시 차단 |
| INV5 | **헤드 900 + 본문 300** — 모든 톤·페르소나에 동일 적용 | 위반 시 롤백 |

INV는 톤·포맷·CORE 모두 우선. 자가합리화·예외 정당화 = FAIL.

---

## §INV NO_WORK_LABEL

| 항목 | 정의 |
|---|---|
| RULE | 산출물·대화 = 인간 언어. 작업 라벨 ZERO. (1만 페이지 1단어 = FAIL) |
| 판정 | "사전 없이 읽을 수 있나?" NO → 금지 |
| ALLOW | 업계 전문용어(CSS·HTML·viewport·Pretendard·clamp·CTA) · 고유명사(Apple·KISAS·Keynote) |
| CONVERT | "4층 매핑·6포맷·4톤·H1~H8·C8/C9·light-bento·dark-scroll·이쁘니·벤또" → 결과만 노출 |
| SELF_CHECK | 출력 직전 자체 스캔. 1개라도 발견 = 차단·재작성 |

---

## Gotchas

- **회색 유혹:** "그냥 회색이 깔끔" → H4 영구 금지. 알파 낮춘 컬러로 대체
- **본문 굵기 끌어올림:** 본문이 굵어져 헤드와 구분 안 됨 → C2 위반. 본문은 무조건 300
- **형광펜 미사용:** 페이지에 형광펜 0개 → G7 경고. 핵심 단어 1~3개에 적극
- **헤드 사이즈 미달:** H5 헤드는 무조건 900. 사이즈 작아도 웨이트는 절대 900
- **모바일 12 미만:** clamp 하한이 12 미만이면 H7 위반
- **밤모드에 검정텍스트:** dark-{bento·scroll}에서 검정 텍스트는 절대 ✗ → 흰색
- **낮모드에 흰색텍스트:** light-{bento·scroll}에서 흰색 텍스트는 절대 ✗ → 검정 (단 컬러 박스 위에서는 흰색 OK)
- **그라디언트 욕구:** H1 → 단색만. 그라디언트 = 즉시 FAIL
- **C8 4함정:** 고정px·viewport누락·고정다열·고정포맷 → `responsive.md`
- **C9 3함정:** HTML표·문장만·ASCII·CDN의존 → `visualization-html.md`
- **자가검증 스킵:** §SELF_CHECK 5단계 grep 안 돌리고 출력 → 회색·웨이트 위반 누출
- **INV 자가합리화:** "이번엔 예외" "본질 보존" 정당화 = INV 위반·즉시 차단
- **모드 토글 누락:** scaffold-scroll·bento에서 `<body data-mode="dark|light">` 미설정 = 의도 불명
- **scaffold 직카피:** scaffold-{scroll·bento}.html을 그대로 쓰면 콘텐츠 미반영. 베이스로 복사 후 콘텐츠 교체

세부 → `gotchas-extended.md` · `constitution.md` 위반 카탈로그.

---

## Version

- **v3.2 (2026-04-29) — skill-doctor 처방 반영.** §SELF_CHECK 신설(5단계 grep 게이트) · §INVARIANT 신설(INV1~INV5 절대 보호) · P1 짧은키워드 제거(벤또·차트·영톤 → 벤또그리드·차트시각화·영플레이풀) · Gotchas 4행 추가(자가검증 스킵·INV 자가합리화·모드 토글·scaffold 직카피).
- **v3.1 (2026-04-29) — Apple Keynote DS 자산 흡수.** scaffold-scroll.html (5섹션 스크롤 풀세트·IntersectionObserver 페이드인) · scaffold-bento.html (4-col 그리드 + 9컴포넌트 + 1024/640 리셋) · assets/deck-stage.js (1920×1080 슬라이드·키보드 네비·Print PDF) · scaffold-deck.md (사용 가이드). 6액센트(보라 포함) 호환 변환·회색 0%·형광펜 적극.
- **v3.0 (2026-04-29) — 헌법 교체.** 8조 헌법 도입(회색금지·형광펜적극·헤드900·본문300·12하한). 7톤 → 4톤(light/dark × bento/scroll) + 믹스 + 페르소나 2. 6컬러 팔레트(보라 추가). C3 재정의(흰/검 + 6액센트).
- v2.0 (2026-04-29) — apple-design 흡수, 7톤·SSOT 3종.
- v1.8 (2026-04-29) — §C R1~R5 신설.
- v1.7 (2026-04-23) — 4블록 인덱스 spine.
- v1.6 (2026-04-23) — C8 R1~R11.
- v1.5 (2026-04-20) — young-playful + §-1 분기.
- v1.4 (2026-04-20) — C9 시각 전환 CORE.
