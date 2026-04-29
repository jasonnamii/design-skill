# MODE 2: HTML 벤토 (한 페이지 그리드)

| 항목 | 값 |
|------|-----|
| 배경 | `#f5f5f7` |
| 폰트 | `Pretendard Variable` wght 300,400,600,700,950. CDN: jsdelivr pretendardvariable.min.css |
| 그리드 | `repeat(4, 1fr)`, gap `12px` |
| 카드 | `#fff`, `border-radius: 20px`, padding `28px 30px` |
| 다크카드제목 | L `48px` wght 950, 라벨 XS `13px` wght 700 `#fff` (검정 배경 예외) |
| 히어로 | `#000`, span 2col, XL `80px` wght 950 |
| 섹션헤더 | XS `13px` wght 700, uppercase, `letter-spacing: 2px`, **`#000`** (회색 추방) |
| 본문 | S `clamp(16px,1.6vw,18px)` wght 400, `#1d1d1f`, `line-height: 1.65` |
| 캡션·설명 | XS `13px` wght 300 (Light), **`#000`** (회색 추방) |
| 사례·각주 | S `16px` wght 300, **`#000`** (회색 추방, weight로 위계) |
| 체크리스트 | 넘버 `#000` 900 + 텍스트 `#000` 300 |
| 프로그레스바 | `7px` height, `#f0f0f0` bg, `#1d1d1f` fill |
| 태그 | `#f5f5f7` bg, `1.5px solid #e5e5ea` |
| 플로우 | 가로 배치, `#fafafa` bg, `1.5px solid #e8e8e8` |
| 배치원칙 | 다크제목 좌 + 설명카드 우 = 한 행 = 한 맥락 |

## 반응형 (벤토 전용)

벤토는 `repeat(4,1fr)` 고정 그리드 + `grid-column:span N` 유틸로 배치. 단순 `auto-fit`과 다르게 **각 컴포넌트마다 span 값이 박혀있어**, 미디어쿼리에서 **전수 리셋**하지 않으면 모바일에서 붕괴 실패. design-skill responsive R4a와 동기.

### 브레이크포인트별 span 리셋

| 폭 | 그리드 | span 리셋 대상 | 목표 span |
|-----|--------|------|-----|
| ≥ 1025px | `repeat(4,1fr)` | — | base 그대로 (`.hero:2`·`.section-head:4`·`.closing:4`·`.elev:3`·`.think:2`·`.col-3:3`·`.col-4:4`) |
| 641 ~ 1024px | `repeat(2,1fr)` | `.col-3, .col-4, .hero, .section-head, .think, .elev, .closing` | `span 2` |
| ≤ 640px | `1fr` (1열) | `.col-1, .col-2, .col-3, .col-4, .hero, .section-head, .think, .elev, .closing` | `span 1` |

### 미디어쿼리 템플릿

```css
/* 🔴 base — 한글 줄바꿈 + 수축 허용 + 색상 3변수 */
:root {
  --label-info:    #1d1d1f;  /* Tier 1 정보성 */
  --label-caption: #000;  /* 회색 추방 (라이트 모드) */  /* Tier 2 캡션 */
  --label-deco:    #000;  /* 회색 추방 (라이트 모드) */  /* Tier 3 장식 */
}
body { word-break: keep-all; overflow-wrap: break-word; line-break: strict; color: var(--label-info); }
.grid > * { min-width: 0; }
.card { min-width: 0; overflow: hidden; }
img, svg, video, iframe { max-width: 100%; height: auto; display: block; }
table { table-layout: fixed; width: 100%; }

.caption, .case, .xs.info   { color: var(--label-caption); }
.deco, .date, .tag, .num     { color: var(--label-deco); }

/* 🔴 다크 컨테이너 자동 역매핑 — inline style="color:..." 전수 제거 필수 */
.dark, .key, .hot, .now, .region.hot, .think.dark,
.card.dark, [class*="-dark"] {
  --label-info:    #fff;
  --label-caption: #fff;   /* #424245·#6e6e73 다크배경 금지 */
  --label-deco:    #000;  /* 회색 추방 (라이트 모드) */
  color: var(--label-info);
}
.dark .caption, .dark .case, .hot .caption, .hot .case,
.think.dark .case { color: var(--label-caption); }
.dark .deco, .dark .date, .dark .tag, .dark .num,
.hot .deco, .hot .date, .hot .num { color: var(--label-deco); }

@media (max-width: 1024px) {
  .grid { grid-template-columns: repeat(2, 1fr); gap: 10px; }
  .col-3, .col-4, .hero, .section-head, .think, .elev, .closing { grid-column: span 2; }
}
@media (max-width: 640px) {
  .grid { grid-template-columns: 1fr; gap: 10px; }
  .col-1, .col-2, .col-3, .col-4, .hero, .section-head, .think, .elev, .closing { grid-column: span 1; }
  .card { padding: 20px 22px; }
}
```

**한글 세로 낙하 방지 (치명):** `word-break: break-word`·`break-all`·`overflow-wrap: anywhere` **단독 사용 금지**. 한글은 반드시 `word-break: keep-all; overflow-wrap: break-word` 조합. 상세: `→ references/layout-safety.md §3`.

**왜:** base CSS에서 명명 컴포넌트에 `grid-column:span N`을 선언하면, @media에서 그 선언이 살아있는 한 자식이 **암시적 트랙**을 생성한다. 즉 `grid-template-columns:1fr`로 바꿔도 span 4 카드는 4개 암시적 트랙을 만들어 횡스크롤 또는 화면 밖 잘림 발생. 규칙: **base에 span을 준 모든 선택자 = @media 리셋 필수.**

### 검증

- 360·390·480·640·768·1024px 각 폭에서 `document.scrollWidth == window.innerWidth`
- 640px 이하에서 모든 카드가 1열 세로 스택

---

## 체크리스트

- [ ] 벤토: 다크제목 + 설명카드 같은 행 배치
- [ ] 4열 그리드 + 12px gap
- [ ] base의 모든 `grid-column:span N` 선언(명명 컴포넌트 포함)이 @media 1024px·640px에서 전수 리셋
- [ ] 360·390·480·640·768px 실측 횡스크롤 0
- [ ] XS 13px 하한
- [ ] **모든 라이트 텍스트 `#000`** (회색 추방). 위계는 weight 900↔300으로만
- [ ] CSS 변수 3분리 선언 (`--label-info`/`--label-caption`/`--label-deco`). `--muted` 단일 변수 없음
- [ ] 다크 컨테이너 역매핑 CSS 선언 (`.dark`·`.hot`·`.key`·`.now`·`.region.hot`·`.think.dark`)
- [ ] 다크 배경(검정 컨테이너) 텍스트 = `#fff` 단일. 컬러 카드 배경 위 흰글자 ✗
- [ ] **본문에 `text-wrap: pretty` + `line-height: 1.7`** (한글 줄바꿈 자연화·고아 단어 방지)
- [ ] **헤드라인에 `text-wrap: balance`** (짧은 2~4줄 균등화)
- [ ] **어색한 어절은 `<span class="nowrap">` 보호** (동사구·서술절 끊김 방지)
- [ ] **`<details class="fold">` 토글 시 A 방안 `scrollBy(delta)` 적용** (viewport 점프 방지)
- [ ] inline `style="color:..."` 전수 0건 (`grep -n 'style="[^"]*color:' *.html` = 0)
- [ ] 라벨·섹션헤더 weight 700 (작은글자+light+muted 3중 약화 방지)
- [ ] `body { word-break: keep-all; overflow-wrap: break-word }` 선언
- [ ] `.grid > * { min-width: 0 }` 선언 (한글 세로낙하·카드이탈 방지)
- [ ] 레이아웃 붕괴 7대 원인 대조: → `references/layout-safety.md`

---

## v2.0 텍스트多 + 비대칭 그리드 (필수 참조)

**핵심:** 단순 4열 균등 그리드 ✗. Apple Keynote 벤또는 **비대칭 + 텍스트多**가 표준.

### 패턴 라우팅

| 콘텐츠 유형 | 패턴 | 참조 |
|---|---|---|
| 마케팅 분석 | KPI + 인사이트 | `→ bento-patterns.md §A` |
| 캠페인 복기 | 빅넘버 + 학습 | `→ bento-patterns.md §B` |
| 기능 요약 | 중앙 앵커 + 라벨 셀 | `→ bento-patterns.md §C` |
| 주기 리뷰 | 4분할 (지표·시그널·학습·액션) | `→ bento-patterns.md §D` |
| 텍스트多 | text-dense Type 1~8 | `→ bento-patterns.md §2 텍스트多` |
| 보고서형 | 좌측 결론 + 우측 근거 | `→ bento-patterns.md §F` |

### 비대칭 그리드 5종

```css
/* Pattern A: 중앙 앵커형 (제품·로고 span 2×2) */
.bento-anchor {
  grid-template-columns: repeat(5, minmax(0, 1fr));
  grid-template-areas:
    "l1 l2 hero hero l3"
    "l4 l5 hero hero l6"
    "m1 m1 hero hero m2"
    "m3 m3 big m2  m2";
}

/* Pattern B: 좌중우 3분할 (제품 span 1×3) */
.bento-3split {
  grid-template-columns: 1fr 2fr 1fr;
  grid-template-rows: repeat(3, auto);
}

/* Pattern C: 상단 빅넘버 + 본문 (KPI) */
.bento-kpi {
  grid-template-areas:
    "b1 b2 b3"
    "text text img";
}
```

**상세 + 8유형 텍스트多 셀 + 마케팅 템플릿:** `→ bento-patterns.md`

### 텍스트多 셀 핵심 CSS (240자 초과 시 강제)

```css
.text-dense {
  padding: clamp(28px, 4vw, 40px);
  line-height: 1.65;
  letter-spacing: -0.005em;
  min-width: 0;
  overflow: hidden;
  word-break: keep-all;
  overflow-wrap: break-word;
  background: #fff;
  border-radius: 20px;
}
.text-dense .cell-headline {
  font-size: clamp(22px, 2.4vw, 28px);
  font-weight: 700;
  margin-bottom: 16px;
}
.text-dense .cell-body {
  font-size: clamp(15px, 1.4vw, 16px);
  font-weight: 400;
  color: var(--label-info);  /* Tier 1 — caption 색상 ✗ */
}
```

### 빅넘버 셀 핵심 CSS (포인트 컬러 1문서 1색)

```css
.big-number {
  font-size: clamp(56px, 8vw, 96px);
  font-weight: 950;
  line-height: 0.95;
  letter-spacing: -0.04em;
  color: var(--point);   /* 5종 중 택1, 면적 ≤15% */
}
.big-caption {
  font-size: clamp(13px, 1.3vw, 15px);
  font-weight: 600;
  color: var(--label-caption);
  text-transform: uppercase;
  letter-spacing: 0.06em;
}
```

### v2.0 추가 체크리스트

- [ ] 콘텐츠 유형 판정 (마케팅·복기·기능·리뷰·매뉴얼·보고)
- [ ] 셀당 자수 측정 → 240자 초과 시 text-dense 클래스 적용
- [ ] 비대칭 그리드 (Pattern A~E 중 선택) 또는 명시 사유로 균등 그리드
- [ ] 포인트 컬러 1문서 1색·면적 ≤15%
- [ ] 빅넘버 셀 line-height 0.95·letter-spacing -0.04em
- [ ] 텍스트多 셀 line-height 1.65·padding clamp(28px, 4vw, 40px)

