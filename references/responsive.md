# Responsive Design Rules (C8 상세)

design-skill CORE C8의 세부 적용 규칙. HTML·웹렌더 MD 전용. PDF·PPTX·DOCX·XLSX는 해당 없음(고정 포맷).

---

## 브레이크포인트 3단계

| 단계 | 범위 | 기본 레이아웃 |
|------|------|----------|
| 모바일 | ≤ 640px | 1열, 패딩 20~32px |
| 태블릿 | 641 ~ 1024px | 2열 허용, 패딩 40~60px |
| 데스크탑 | ≥ 1025px | 풀 위계(L1 XL), 3~4열 허용 |

---

## 필수 규칙 R1~R11

| # | 규칙 | 값 | 판정 |
|---|------|-----|------|
| R1 | 폰트 clamp | L1 `clamp(32px, 6vw, 64px)` · L2 `clamp(22px, 3vw, 36px)` · L3 `clamp(17px, 1.8vw, 24px)` · L4 `clamp(13px, 1.2vw, 16px)`. 톤별 변형 가능하되 C1 비율 4:2.3:1.5:1 유지 | 고정px→FAIL |
| R1a | **clamp 하한 모바일 역산** | 하한값은 **320~375px 뷰포트에서 실제 렌더 크기**로 검증. `clamp(26px, 5.5vw, 84px)`에서 375px 뷰포트 = 20.6px → 히어로로 약함. **히어로 하한 ≥40px, 섹션 타이틀 ≥26px** 강제. vw 계산 = `하한값 / (vw%) × 100` | 하한<권장→FAIL |
| R2 | viewport 메타 | `<meta name="viewport" content="width=device-width, initial-scale=1">` | 누락→FAIL |
| R3 | 터치 타겟 | CTA·링크·버튼 ≥ 44×44px | <44→FAIL |
| R4 | 그리드 붕괴 | 데스크탑 다열 → 태블릿 2열 → 모바일 1열. 기본: `grid-template-columns: repeat(auto-fit, minmax(280px, 1fr))` | 고정 다열→FAIL |
| R4a | **명시적 span 리셋 완전성** | `repeat(N,1fr)` + `grid-column:span K` 패턴(벤토) 사용 시, **base에 `span` 값을 선언한 모든 선택자**(`.col-*`, `.hero`, `.section-head`, `.elev`, `.think`, `.closing` 등 명명 컴포넌트 포함)를 @media 1024px에서는 `span 2` 이하, 640px에서는 `span 1`로 **전부 리셋**. 하나라도 누락시 자식 카드가 **암시적 트랙**을 생성해 그리드가 붕괴하지 않음 (모바일에서 화면 밖으로 밀려 잘림) | 누락→FAIL |
| R4b | **`minmax(0, 1fr)` 강제** | `repeat(N, 1fr)` = `repeat(N, minmax(auto, 1fr))`. grid item 기본 `min-width:auto`라 **콘텐츠가 칸 폭을 밀어냄**(+22.8% 같은 긴 텍스트 오버플로우). **반드시 `repeat(N, minmax(0, 1fr))`** 사용 | `repeat(N,1fr)` 단독→FAIL |
| R5 | 횡스크롤 금지 | 긴 테이블·코드는 `overflow-x: auto` 또는 분할. 검증: `document.scrollWidth <= window.innerWidth` (모든 타겟 폭에서) | 발생→FAIL |
| R6 | 패딩 축소 | 데스크탑 80~120px → 모바일 20~32px (미디어쿼리) | 모바일 80+→경고 |
| R7 | 이미지 반응형 | `max-width: 100%; height: auto` 기본 | 고정 width→경고 |
| R8 | **한글 `word-break`** | **`word-break:keep-all; overflow-wrap:break-word`** — 한글 히어로·헤드라인·박스 텍스트 전체. `break-all`·`break-word` 단독 = 세로 낙하 | 누락→FAIL |
| R9 | **`<br>` 강제 줄바꿈 금지** | 히어로·헤드라인에 `<br>`로 강제 줄바꿈하면 폭 바뀔 때 무조건 깨짐. 자연 wrap + `word-break:keep-all`에 맡김. 예외: 의도적 2줄 연출 + 각 줄이 **최단 뷰포트에서도** 1줄 보장 시만 | 폭 의존 `<br>`→FAIL |
| R10 | **인라인 `style="font-size:clamp(...)"` 금지** | 인라인 style specificity 1000이 미디어쿼리 덮어씌움 **불가**. 모바일 오버라이드 무력화. 전부 CSS 클래스·변수 경유 | 인라인 clamp→FAIL |
| R11 | **박스 내부 min-width:0 + overflow:hidden** | flex/grid 자식 박스가 콘텐츠에 밀려 부모 폭 초과. `.box { min-width:0; overflow:hidden }` + `.box .big-text { max-width:100%; overflow-wrap:break-word }` | 오버플로우→FAIL |
| R12 | **`text-wrap: pretty` 본문 강제** | 한글 본문 마지막 줄에 1~2자만 남는 고아(orphan) 방지. 카드/박스/단락 본문에 `text-wrap: pretty` 강제. Safari 17.4+·Chrome 117+, 미지원 브라우저는 무시(degrade gracefully) | 본문 누락→경고 |
| R13 | **`text-wrap: balance` 헤드라인** | 짧은 헤드라인(2~4줄)에 `text-wrap: balance` — 줄 길이 균등화. 어색한 단일 단어 줄 방지. 4줄 초과는 `pretty`로 폴백 | 헤드라인 누락→경고 |
| R14 | **어절 단위 nowrap 보호** | 끊기면 어색한 어절(예: "데이터를 쌓는다", "기회가 찾아오는") = `<span style="white-space:nowrap">` 또는 `.nowrap` 클래스. 자주 쓰는 패턴: 동사구·서술절·고유명사 | 어색한 단어 끊김→경고 |

---

## 톤별 조정

| 톤 | 반응형 조정 |
|----|------|
| dark-cinema | 모바일에서도 어두운 배경 유지. 히어로 XL clamp 최소값 40~48px |
| story-dark | 동일. 시네마틱 여백은 모바일에서 축소 허용 |
| clean-info | 고밀도. 모바일 폰트 최소값 상향(L3 18px+)로 가독성 확보 |
| warm-human | 기본 clamp. 여백 감성 유지하되 모바일에선 절반으로 |
| pro-grid | 그리드 기본. 모바일 1열 붕괴, 카드 패딩 축소 |

---

## MD(웹렌더) 특례

Obsidian·GitHub은 자체 반응형. HTML div 래핑 시에만 C8 적용. `html-div-style` cascade 시 반응형 규칙 동기.

---

## 미디어쿼리 템플릿 (v1.6 — R4b·R8·R11 반영)

```css
/* 모바일 우선 기본값 */
.container { padding: 20px; }
.grid { grid-template-columns: minmax(0, 1fr); gap: 16px; }  /* R4b */
h1, .headline {
  font-size: clamp(32px, 6vw, 64px);
  word-break: keep-all;                 /* R8 */
  overflow-wrap: break-word;
  text-wrap: balance;                   /* R13 — 헤드라인 균등화 */
  line-height: 1.2;
}
.box, .card, p, .body {
  min-width: 0;                         /* R11 */
  overflow: hidden;
  word-break: keep-all;                 /* R8 */
  overflow-wrap: break-word;
  text-wrap: pretty;                    /* R12 — 본문 고아 방지 */
  line-height: 1.7;                     /* 한글 본문 가독성 */
}
.box .big-text {
  max-width: 100%;                      /* R11 */
  overflow-wrap: break-word;
}
/* R14 — 어절 끊김 방지 유틸 */
.nowrap { white-space: nowrap; }

/* 태블릿 */
@media (min-width: 641px) {
  .container { padding: 40px; }
  .grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }  /* R4b */
}

/* 데스크탑 */
@media (min-width: 1025px) {
  .container { padding: 80px; }
  .grid { grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); }
}
```

---

## 데스크톱 기준 설계의 함정 (KISAS Manifesto 2026-04-23 교훈)

**증상:** 데스크톱은 완벽한데 모바일에서 (a) 히어로 글자 왜소 (b) 박스 밖 오버플로우 (c) 섹션별 대여섯 군데 깨짐

**근본 원인 3가지:**
1. **`clamp(min, vw, max)` 하한이 모바일 기준 아님** — 데스크톱 기준 vw값이면 375px에서 하한값으로 수렴. vw 계산을 모바일 뷰포트(375px)에서 먼저 검증.
2. **`repeat(N, 1fr)` grid** — item 기본 `min-width:auto`라 긴 콘텐츠가 칸 폭을 밀어냄. `minmax(0, 1fr)` 필수(R4b).
3. **한글 `word-break` 미지정** — 영문 기본 wrap이 한글 어절을 애매하게 끊음. `keep-all` 필수(R8).

**교정 순서:** 모바일 375px 뷰포트에서 먼저 디자인 → 데스크톱으로 확장 (mobile-first). 반대 순서 = 수정 루프 3~5회 발생.

---

## QC 체크리스트 (v1.6)

- [ ] R1: 모든 폰트 크기가 clamp() 또는 상대단위(rem·em·vw)
- [ ] R1a: 히어로 clamp 하한 ≥40px, 섹션 타이틀 ≥26px (모바일 375px 실측)
- [ ] R2: `<head>`에 viewport 메타 존재
- [ ] R3: CTA·버튼·링크 실측 ≥44×44px
- [ ] R4: 다열 그리드가 모바일에서 1열로 붕괴
- [ ] R4a: base의 모든 `grid-column:span N` 선언(명명 컴포넌트 포함)이 1024px·640px @media에서 각각 리셋 선언 존재
- [ ] **R4b: 모든 `repeat(N, 1fr)` → `repeat(N, minmax(0, 1fr))`** (`grep -E "repeat\([0-9]+, *1fr\)" *.html` = 0)
- [ ] R5: Playwright/DevTools 360·375·390·480·640·768·1024px 전 폭에서 `document.scrollWidth == window.innerWidth` (실측. 눈대중 금지)
- [ ] R6: 모바일 패딩 ≤32px
- [ ] R7: 이미지 `max-width:100%` 적용
- [ ] **R8: 한글 헤드라인·박스 전체에 `word-break:keep-all; overflow-wrap:break-word`** (`grep -c "word-break" *.html` ≥ 1)
- [ ] **R12: 본문에 `text-wrap: pretty`** — 카드·박스·단락 본문 (`grep -c "text-wrap: pretty" *.html` ≥ 1)
- [ ] **R13: 짧은 헤드라인에 `text-wrap: balance`** — 2~4줄 헤드라인 (`grep -c "text-wrap: balance" *.html` ≥ 1)
- [ ] **R14: 어색한 어절 끊김 방지 — 동사구·서술절은 `.nowrap`** 또는 `<span style="white-space:nowrap">`로 묶기
- [ ] **R9: `<br>` 강제 줄바꿈 0건 (히어로·헤드라인)** — 자연 wrap으로 전환
- [ ] **R10: 인라인 `style="font-size:clamp(...)"` 0건** (`grep -E 'style="[^"]*font-size:[^"]*clamp' *.html` = 0)
- [ ] **R11: `.box` 선언에 `min-width:0; overflow:hidden` 포함**
