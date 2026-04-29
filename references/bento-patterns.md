# bento-patterns.md — Apple Keynote 벤또 패턴북 (v2.0 신설)

이 파일은 **이 스킬의 핵심 차별점**. Apple 키노트 발표 슬라이드 8장 분석 기반.

> 단순 그리드 ✗. **비대칭 그리드 + 텍스트多 셀 + 빅넘버 + 이미지 슬롯 + 포인트 컬러**의 조합 시스템.

---

## 0. 분석 기반 (Apple Keynote 8장 패턴 추출)

| 슬라이드 | 핵심 패턴 |
|---|---|
| iPhone 16e | 라이트 벤또·중앙 제품 이미지(span 2×2)·주변 라벨 셀(span 1×1) |
| iPhone 15 Pro | 다크 벤또·중앙 텍스트("Titanium" XL)·라벨 + 이미지 + 빅넘버 혼합 |
| iPadOS | 라이트 벤또·중앙 로고("iPadOS")·기능 셀 + 이미지 셀 비대칭 |
| iPhone 17 | 다크 벤또·중앙 제품·**포인트 컬러(보라·녹)** 빅넘버·재활용 아이콘 |
| AirPods Pro | 다크 벤또·**녹색 포인트**·빅넘버("2x more")·기능 셀 작게 |
| Apple Watch S9 | 다크 벤또·중앙 제품·**핑크 포인트**·텍스트 카드 + 이미지 카드 비대칭 |
| Apple Watch S11 | 라이트 벤또·**핑크·녹 포인트**·빅넘버 + 텍스트 + 이미지 3종 비율 1:1:1 |
| iOS | 라이트 벤또·중앙 로고·**텍스트多 셀 다수**·UI 캡처 슬롯 |

**공통 백본 1줄:** Apple 벤또 = **중앙 앵커(제품·로고·핵심메시지) + 비대칭 주변 셀(라벨·빅넘버·이미지·텍스트多) + 단일 포인트 컬러**.

---

## 1. 비대칭 그리드 5종 (grid-template-areas 기반)

벤또는 4×N 균등이 아니다. 각 셀의 정보 가치에 따라 **비대칭 면적**으로 위계를 만든다.

### Pattern A: 중앙 앵커형 (Apple iPhone 16e·15 Pro 패턴)

```
┌──┬──┬───────┬──┬──┐
│L │L │       │L │L │
├──┼──┤  HERO ├──┼──┤
│L │L │       │L │L │
├──┴──┼───────┼──┴──┤
│  M  │       │  M  │
├─────┼───────┼─────┤
│  M  │   B   │  M  │
└─────┴───────┴─────┘
L=라벨셀(작) M=중간셀 HERO=제품/로고(span 2×2) B=빅넘버
```

```css
.bento-anchor {
  display: grid;
  grid-template-columns: repeat(5, minmax(0, 1fr));
  grid-template-rows: auto;
  grid-template-areas:
    "l1 l2 hero hero l3"
    "l4 l5 hero hero l6"
    "m1 m1 hero hero m2"
    "m3 m3 big m2  m2";
  gap: 12px;
}
.hero { grid-area: hero; }
.big  { grid-area: big; }
```

### Pattern B: 좌중우 3분할 (Apple Watch S9 패턴)

```
┌────┬─────────┬────┐
│ L  │         │ L  │
├────┤  HERO   ├────┤
│ M  │ (제품)  │ M  │
├────┤         ├────┤
│ B  │         │ T  │
└────┴─────────┴────┘
L=라벨 M=중간 B=빅넘버 T=텍스트多 HERO=제품(span 1×3)
```

### Pattern C: 상단 빅넘버 + 본문 (KPI 대시보드형)

```
┌────────┬────────┬────────┐
│   B1   │   B2   │   B3   │  ← 빅넘버 3종 (한 줄)
├────────┴────────┼────────┤
│                 │        │
│   TEXT-DENSE    │   IMG  │  ← 텍스트多 셀 + 이미지
│                 │        │
└─────────────────┴────────┘
```

### Pattern D: 좌측 텍스트多 + 우측 카드 그리드 (보고서형)

```
┌─────────┬───┬───┐
│         │ S │ S │
│  TEXT-  ├───┼───┤
│  DENSE  │ S │ S │
│         ├───┼───┤
│         │ S │ S │
└─────────┴───┴───┘
```

### Pattern E: 정사각 4분할 + 중앙 메시지 (캠페인 복기형)

```
┌────────┬────────┐
│  IMG   │  TEXT  │
├────┬───┴───┬────┤
│ B  │ HERO  │ B  │
├────┴───┬───┴────┤
│  TEXT  │  IMG   │
└────────┴────────┘
```

---

## 2. 텍스트多 셀 8유형 (v2.0 핵심)

셀당 240자 초과 시 자동 분기. 8유형 중 콘텐츠 성격에 맞춰 선택.

### Type 1: 헤드라인 + 본문 (가장 흔함)

```html
<article class="cell text-dense">
  <h3 class="cell-headline">차별점 3가지.</h3>
  <p class="cell-body">
    첫째, 1초만에 답이 보인다. 스크롤·검색 없이 헤드라인 + 빅넘버로 결론 직진.
    둘째, 텍스트가 많아도 무너지지 않는다. line-height 1.65 + 큰 padding이 가독성 보장.
    셋째, 비대칭 그리드가 정보 위계를 만든다. 균등 그리드는 위계 ✗.
  </p>
</article>
```

```css
.text-dense {
  padding: clamp(28px, 4vw, 40px);
  line-height: 1.7;                  /* 한글 가독성 */
  background: #fff;
  border-radius: 20px;
  min-width: 0;                      /* R11 */
  word-break: keep-all;              /* R8 */
  overflow-wrap: break-word;
  text-wrap: pretty;                 /* R12 — 마지막 줄 고아 방지 */
}
.cell-headline {
  font-size: clamp(22px, 2.4vw, 28px);
  font-weight: 900;  /* 카드 제목 = 무조건 가장 굵게 (C2 ≥ 600 대비) */
  letter-spacing: -0.01em;
  margin-bottom: 16px;
  color: var(--label-info);  /* = #000 */
  word-break: keep-all;
  overflow-wrap: break-word;
  text-wrap: balance;                /* R13 — 짧은 헤드라인 균등화 */
  line-height: 1.25;
}
.cell-body {
  font-size: clamp(15px, 1.4vw, 16px);
  font-weight: 300;  /* Light — 제목 900과 600 대비 */
  color: var(--label-info);  /* = #000 (회색 추방) */
  word-break: keep-all;
  overflow-wrap: break-word;
  text-wrap: pretty;                 /* R12 */
  line-height: 1.7;
}
```

### Type 2: 빅넘버 + 캡션 + 본문 (KPI 셀)

```html
<article class="cell text-dense kpi">
  <div class="big-number" style="color: #30d158;">+247%</div>
  <p class="big-caption">전환율 (전년比)</p>
  <p class="cell-body">
    캠페인 리프트 제외 순수 증분. 메타·구글 분리 측정 결과
    동일 추세 확인. CTR 상승보다 LP 개선 영향이 컸음.
  </p>
</article>
```

```css
.big-number {
  font-size: clamp(56px, 8vw, 96px);
  font-weight: 950;
  line-height: 0.95;
  letter-spacing: -0.04em;
  margin-bottom: 8px;
}
.big-caption {
  font-size: clamp(13px, 1.3vw, 15px);
  font-weight: 600;
  color: var(--label-caption);
  margin-bottom: 20px;
  text-transform: uppercase;
  letter-spacing: 0.06em;
}
```

### Type 3: 번호 리스트 (압축 ≤4)

```html
<article class="cell text-dense list">
  <h3 class="cell-headline">실행 4단계.</h3>
  <ol class="cell-list">
    <li><strong>가설 수립</strong> — 데이터로 의심 구간 좁히기</li>
    <li><strong>실험 설계</strong> — 통제군·실험군 분리 조건 확정</li>
    <li><strong>측정 실행</strong> — 최소 2주 충분한 표본 확보</li>
    <li><strong>의사결정</strong> — 통계적 유의성 + 비즈 영향 동시 확인</li>
  </ol>
</article>
```

### Type 4: 인용 + 출처 (사례·증거 셀)

```html
<article class="cell text-dense quote">
  <blockquote class="cell-quote">
    "벤또 그리드는 단순 레이아웃이 아니다.
     정보의 위계를 시각으로 번역하는 압축 시스템이다."
  </blockquote>
  <cite class="cell-cite">— Apple Human Interface Guidelines, 2024</cite>
</article>
```

### Type 5: 비교 (Before/After)

```html
<article class="cell text-dense compare">
  <h3 class="cell-headline">변화.</h3>
  <div class="compare-grid">
    <div class="before">
      <span class="compare-label">Before</span>
      <p>4×N 균등 그리드. 모든 셀 같은 면적. 위계 0.</p>
    </div>
    <div class="after">
      <span class="compare-label">After</span>
      <p>비대칭 그리드. 핵심 2배 면적. 시선 동선 통제.</p>
    </div>
  </div>
</article>
```

### Type 6: 체크리스트 (실행 항목)

```html
<article class="cell text-dense checklist">
  <h3 class="cell-headline">출고 점검.</h3>
  <ul class="cell-checklist">
    <li>✓ 360·390·480·640·1024px 횡스크롤 0</li>
    <li>✓ XS 13px 하한 준수</li>
    <li>✓ 다크 컨테이너 역매핑 적용</li>
    <li>✓ 한글 keep-all + break-word 조합</li>
  </ul>
</article>
```

### Type 7: 정의 + 풀이 (개념 셀)

```html
<article class="cell text-dense define">
  <span class="cell-term">벤또 (Bento)</span>
  <h3 class="cell-define">정보를 셀에 담아 한 화면에 압축하는 기법.</h3>
  <p class="cell-body">
    일본 도시락에서 차용한 명칭. 셀마다 다른 정보를 담되, 전체로
    하나의 메시지가 되어야 한다. Apple Keynote 발표가 대표 사례.
  </p>
</article>
```

### Type 8: 타임라인 (시간순)

```html
<article class="cell text-dense timeline">
  <h3 class="cell-headline">3월 진행.</h3>
  <ul class="cell-timeline">
    <li><time>3/1</time> 가설 수립</li>
    <li><time>3/8</time> 실험 시작</li>
    <li><time>3/22</time> 1차 결과</li>
    <li><time>3/29</time> 의사결정</li>
  </ul>
</article>
```

---

## 3. 텍스트多 셀 공통 CSS (강제 적용)

```css
.text-dense {
  /* 패딩 강제 */
  padding: clamp(28px, 4vw, 40px);

  /* 가독성 강제 */
  line-height: 1.65;
  letter-spacing: -0.005em;

  /* 그리드 안전 */
  min-width: 0;
  overflow: hidden;
  word-break: keep-all;
  overflow-wrap: break-word;

  /* 시각 일관 */
  background: #fff;
  border-radius: 20px;
}

/* 다크 텍스트多 셀 */
.text-dense.dark {
  background: #1d1d1f;
  --label-info:    #fff;
  --label-caption: #fff;  /* 검정 배경 위 흰글자 예외 */
  --label-deco:    #fff;
  color: var(--label-info);
}

/* 본문 색상은 Tier 1 (caption 아님) */
.text-dense .cell-body { color: var(--label-info); }

/* 강제 줄바꿈 ✗ — 자연 wrap */
.text-dense br { display: none; }  /* 정말 필요할 때만 .force-br 클래스로 예외 */
```

---

## §A. 마케팅 분석 템플릿

### A1. 캠페인 성과 대시보드 (Pattern C 응용)

```
┌─────────┬─────────┬─────────┐
│ +247%   │ ₩2.3B   │  4.1x   │
│ 전환율   │ 매출     │  ROAS   │
├─────────┴─────────┴─────────┤
│ 📊 핵심 인사이트              │
│ (텍스트多 셀 — Type 2 활용)    │
├──────────────┬──────────────┤
│ 채널별 기여   │ 학습 포인트   │
│ (Type 3 리스트)│ (Type 6 체크)│
└──────────────┴──────────────┘
```

**구성 룰:**
- 상단 3 빅넘버 셀 = 1행 (포인트 컬러 1색만)
- 중앙 텍스트多 셀 = span 3 (Type 2 빅넘버+캡션+본문)
- 하단 2분할 = 채널 기여 + 학습 포인트

### A2. 채널·세그먼트 매트릭스 (Pattern D 응용)

```
┌─────────────┬───┬───┐
│ 핵심 가설    │ 메│ 구│  ← 채널별 작은 카드
│ + 검증 결과  ├───┼───┤
│ (Type 1     │ 카│ 네│
│  텍스트多)  ├───┼───┤
│             │ 틱│ 유│
└─────────────┴───┴───┘
```

### A3. 퍼널 분석 (수직 흐름)

```
┌───────────────────────────┐
│ 노출 1.2M  ──────────▼    │
├───────────────────────────┤
│ 클릭 48K (CTR 4.0%) ─▼    │
├───────────────────────────┤
│ 가입 6.2K (CVR 12.9%) ▼   │
├───────────────────────────┤
│ 결제 1.1K (CVR 17.7%) ▼   │
├───────────────────────────┤
│ ROAS 4.1x — Type 2 본문   │
└───────────────────────────┘
```

---

## §B. 캠페인 복기 템플릿 (Pattern E 응용)

```
┌────────┬────────┐
│ 결과    │ 가설    │  ← Type 1 텍스트多 2개
│ (이미지 │ (검증/  │
│  키비주)│  반증)  │
├────┬───┴───┬────┤
│Big │히트율 │Big │
│247%│ 패턴  │ 4.1│
├────┴───┬───┴────┤
│ 학습    │ 다음    │
│ 포인트  │ 액션    │
└────────┴────────┘
```

---

## §C. 기능 요약 템플릿 (Apple Keynote 정형)

```
┌──┬──┬───────┬──┬──┐
│라│라│       │라│라│
├──┼──┤제품·로고├──┼──┤
│라│라│       │라│라│
├──┼──┴───────┴──┼──┤
│라│              │라│
└──┴──────────────┴──┘
```

각 라벨 셀 = Type 1 (헤드라인 1줄 + 캡션 1줄) 또는 Type 2 (빅넘버 + 캡션).

---

## §D. 주기 리뷰 템플릿 (주간·월간)

```
┌──────────┬──────────┐
│  핵심지표 │ 시그널    │
│  (Type 2)│ (Type 6)  │
├──────────┼──────────┤
│  학습     │ 다음주    │
│  (Type 1)│ 액션      │
│          │ (Type 3)  │
└──────────┴──────────┘
```

---

## §E. 텍스트多 강제 분류 룰 (240자 초과 시)

| 자수 | 분기 | Type 추천 |
|---|---|---|
| 240-400자 | text-dense Type 1·4·7 | 헤드라인 + 본문 단락 |
| 401-700자 | text-dense Type 1 + 부제 | 헤드라인 + 부제 + 본문 |
| 701자+ | **셀 분리 필수** | 1개 카드 → 2-3개 카드로 쪼개기 |

**셀 분리 판정:** 700자 초과 시 단일 셀 강행 ✗. 자연스러운 분기점(소제목·번호) 기준으로 셀 분할. 같은 색·padding으로 시각 통일성 유지.

---

## §F. 보고서형 템플릿 (Pattern D 응용)

```
┌─────────────┬───┬───┐
│ 핵심 결론    │ 근│ 근│  ← 좌측 텍스트多 (span 1×3)
│ (Type 1)    ├───┼───┤
│             │ 거│ 거│  ← 우측 6카드 (근거·데이터)
│             ├───┼───┤
│             │ 1 │ 4 │
└─────────────┴───┴───┘
```

---

## 적용 체크리스트

- [ ] 콘텐츠 유형 판정 (마케팅·복기·기능·리뷰·매뉴얼·보고)
- [ ] 텍스트 밀도 측정 (셀당 자수)
- [ ] 적정 패턴 선택 (A~F + 비대칭 그리드 1~5)
- [ ] 텍스트多 셀 Type 1~8 매핑
- [ ] 포인트 컬러 1문서 1색·≤15% 면적
- [ ] 빅넘버 셀 line-height 0.95·letter-spacing -0.04em
- [ ] 텍스트多 셀 line-height 1.65·padding clamp(28px, 4vw, 40px)
- [ ] grid-template-areas 또는 span N 명시·@media 전수 리셋
- [ ] 360·390·480·640·1024px 횡스크롤 0 실측
- [ ] 6계층 스코어카드 (qc.md) 합격
