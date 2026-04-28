# Visualization (HTML·웹MD 전용) — C9 시각 전환 규칙

HTML 산출물에서 "표·문장으로만 처리된 시각화 소스"를 시각요소로 자동 전환. SKILL.md §1 C9의 풀텍스트. HTML 포맷 생성 시 1회 로드.

---

## 원칙

**원칙 1 — 콘텐츠가 시각형식을 결정한다.** 수치는 차트를 부르고, 프로세스는 플로우를 부르고, 시간축은 타임라인을 부른다. 표와 문장은 "최후의 수단"이다.

**원칙 2 — 인라인 SVG·순수 CSS 우선.** 외부 라이브러리(Chart.js·D3) 의존 금지. CDN은 형이 명시 요청 시만. 이유: 단일 파일 원칙(format-html SP1), 오프라인 동작, 렌더 속도.

**원칙 3 — Apple 미니멀 톤 유지.** 시각요소는 § 0 공리 X2(위계 효율)·X4(여백 증폭)와 충돌하면 안 됨. 차트 색상은 C3 3색 시스템 준수 — 배경+잉크+CTA 1색. 데이터 계열 ≥4개는 무채색 농도 차이로 표현.

---

## 1. 시각소스 감지 — 콘텐츠→시각형식 매핑

HTML 생성 착수 시 콘텐츠를 스캔해 아래 "시각소스"를 찾는다. 발견되면 **시각요소로 전환 의무**. 미전환 → C9 FAIL.

| # | 시각소스 신호 | 원본 형태 예시 | → 전환 대상 |
|---|--------------|--------------|------------|
| V1 | 수치 비교 (2+ 항목) | 표·문단 내 % 점수·금액 | **바차트 / 레이더차트 / 가로막대** |
| V2 | 시간축 이벤트 (3+ 시점) | 연도·날짜 + 사건 나열 | **타임라인 / 간트** |
| V3 | 순차 프로세스 (2+ 단계) | "1→2→3" 단계 설명 | **플로우차트 / 스텝 인디케이터** |
| V4 | 순환 구조 | A→B→C→A 되돌아옴 | **순환 다이어그램 (SVG)** |
| V5 | 2축 분류 (2×2 / 3×3) | "X축·Y축" 언급, 매트릭스 | **매트릭스 그리드** |
| V6 | 핵심 단일 수치 | "연 200~400억"·"10년 2000억" | **big-number 블록** |
| V7 | 계층·트리 구조 | 상위→하위 관계 | **트리 다이어그램 / nested card** |
| V8 | 관계망 (노드+엣지) | 엔티티 간 연결 | **노드 그래프 (SVG)** |
| V9 | 비율·분배 | 100% 내 분할 | **스택바 / 도넛** |
| V10 | 깔때기 (감소) | 진입→전환 축소 | **퍼널 SVG** |

**감지 정량 기준:**
- HTML 문서에 위 신호가 **2개 이상** 존재 → 시각요소 **최소 2개** 필수
- 문서 길이 500행+ → 시각요소 **최소 4개** 권장
- 0개 → 문서가 "시각화 소스 없음" — C9 면제 (순수 서사·단일 인용 등)

---

## 2. SVG·CSS 템플릿 카탈로그

각 템플릿은 복사→콘텐츠 치환만으로 즉시 사용 가능하도록 자급자족.

### V1. 바차트 (순수 CSS)

```html
<div class="bar-chart">
  <div class="bar-row">
    <div class="bar-label">A안 압축 타운</div>
    <div class="bar-track"><div class="bar-fill" style="width:40%">4/10</div></div>
  </div>
  <div class="bar-row">
    <div class="bar-label">C안 페스티벌</div>
    <div class="bar-track"><div class="bar-fill hi" style="width:80%">8/10</div></div>
  </div>
</div>
<style>
.bar-chart { margin: 24px 0; }
.bar-row { display: grid; grid-template-columns: 140px 1fr; gap: 12px; align-items: center; margin-bottom: 10px; }
.bar-label { font-size: 14px; color: var(--ink-soft); font-weight: 600; }
.bar-track { background: var(--line-soft); height: 28px; border-radius: 4px; overflow: hidden; }
.bar-fill { background: var(--ink-mute); color: #000; height: 100%; display: flex; align-items: center; justify-content: flex-end; padding-right: 10px; font-size: 12px; font-weight: 900; }
.bar-fill.hi { background: var(--accent); }
@media (max-width: 640px) { .bar-row { grid-template-columns: 100px 1fr; } }
</style>
```

### V1-b. 레이더차트 (인라인 SVG, 4축)

```html
<svg viewBox="0 0 300 300" class="radar" aria-label="히트점수 레이더">
  <polygon points="150,40 260,150 150,260 40,150" fill="none" stroke="#d2d2d7" stroke-width="1"/>
  <polygon points="150,80 220,150 150,220 80,150" fill="none" stroke="#e8e8ed" stroke-width="1"/>
  <polygon points="150,60 240,150 150,200 90,150" fill="var(--accent)" fill-opacity="0.15" stroke="var(--accent)" stroke-width="2"/>
  <text x="150" y="30" text-anchor="middle" font-size="12" fill="#515154">혼합안 7~8</text>
  <text x="275" y="155" text-anchor="start" font-size="12" fill="#515154">C안 8</text>
  <text x="150" y="280" text-anchor="middle" font-size="12" fill="#515154">B안 5</text>
  <text x="25" y="155" text-anchor="end" font-size="12" fill="#515154">A안 4</text>
</svg>
```

### V2. 타임라인 (가로, CSS)

```html
<div class="timeline">
  <div class="tl-track"></div>
  <div class="tl-item">
    <div class="tl-dot"></div>
    <div class="tl-year">2026</div>
    <div class="tl-label">MOU 체결<br>월 Fee 시작</div>
  </div>
  <div class="tl-item">
    <div class="tl-dot active"></div>
    <div class="tl-year">2027</div>
    <div class="tl-label">프리 페스티벌<br>10~30억</div>
  </div>
  <div class="tl-item">
    <div class="tl-dot"></div>
    <div class="tl-year">2029</div>
    <div class="tl-label">Phase 1 개장<br>연 100~200억</div>
  </div>
  <div class="tl-item">
    <div class="tl-dot"></div>
    <div class="tl-year">2032+</div>
    <div class="tl-label">완전 가동<br>연 300~500억</div>
  </div>
</div>
<style>
.timeline { position: relative; display: grid; grid-template-columns: repeat(4, 1fr); gap: 0; margin: 32px 0; padding: 20px 0; }
.tl-track { position: absolute; top: 36px; left: 8%; right: 8%; height: 2px; background: var(--line); z-index: 0; }
.tl-item { position: relative; text-align: center; z-index: 1; }
.tl-dot { width: 16px; height: 16px; border-radius: 50%; background: #fff; border: 2px solid var(--ink-mute); margin: 0 auto 12px; }
.tl-dot.active { background: var(--accent); border-color: var(--accent); transform: scale(1.3); }
.tl-year { font-size: 13px; font-weight: 700; color: var(--accent); letter-spacing: 1px; margin-bottom: 4px; }
.tl-label { font-size: 13px; color: var(--ink-soft); line-height: 1.4; }
@media (max-width: 640px) { .timeline { grid-template-columns: 1fr; gap: 16px; } .tl-track { display: none; } .tl-item { text-align: left; padding-left: 24px; border-left: 2px solid var(--line); } .tl-dot { position: absolute; left: -9px; top: 0; margin: 0; } }
</style>
```

### V3. 플로우차트 (CSS grid, 4단계)

```html
<div class="flow">
  <div class="flow-step"><div class="flow-num">1</div><div class="flow-title">MOU</div><div class="flow-desc">역할 독점 지정</div></div>
  <div class="flow-arrow">→</div>
  <div class="flow-step"><div class="flow-num">2</div><div class="flow-title">업무위탁</div><div class="flow-desc">SPC 승계 강제</div></div>
  <div class="flow-arrow">→</div>
  <div class="flow-step"><div class="flow-num">3</div><div class="flow-title">주주간</div><div class="flow-desc">지분 + 거부권</div></div>
  <div class="flow-arrow">→</div>
  <div class="flow-step"><div class="flow-num">4</div><div class="flow-title">운영계약</div><div class="flow-desc">10년 + IP</div></div>
</div>
<style>
.flow { display: grid; grid-template-columns: 1fr auto 1fr auto 1fr auto 1fr; gap: 12px; align-items: center; margin: 32px 0; }
.flow-step { background: var(--bg-alt); border: 1px solid var(--line-soft); border-radius: 10px; padding: 20px 14px; text-align: center; }
.flow-num { width: 32px; height: 32px; border-radius: 50%; background: var(--accent); color: #000; font-weight: 900; display: flex; align-items: center; justify-content: center; margin: 0 auto 10px; font-size: 14px; }
.flow-title { font-weight: 700; color: var(--ink); margin-bottom: 4px; font-size: 15px; }
.flow-desc { font-size: 12px; color: var(--ink-soft); }
.flow-arrow { color: var(--ink-mute); font-size: 20px; font-weight: 300; }
@media (max-width: 640px) { .flow { grid-template-columns: 1fr; } .flow-arrow { transform: rotate(90deg); } }
</style>
```

### V4. 순환 다이어그램 (SVG)

```html
<svg viewBox="0 0 400 400" class="cycle" aria-label="순환 구조">
  <defs>
    <marker id="arr" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 10 3, 0 6" fill="#002147"/>
    </marker>
  </defs>
  <circle cx="200" cy="90" r="55" fill="#fff" stroke="#002147" stroke-width="2"/>
  <text x="200" y="95" text-anchor="middle" font-size="14" font-weight="700" fill="#002147">교육</text>
  <circle cx="310" cy="200" r="55" fill="#fff" stroke="#002147" stroke-width="2"/>
  <text x="310" y="205" text-anchor="middle" font-size="14" font-weight="700" fill="#002147">매칭</text>
  <circle cx="200" cy="310" r="55" fill="#fff" stroke="#002147" stroke-width="2"/>
  <text x="200" y="315" text-anchor="middle" font-size="14" font-weight="700" fill="#002147">프로덕션</text>
  <circle cx="90" cy="200" r="55" fill="#fff" stroke="#002147" stroke-width="2"/>
  <text x="90" y="205" text-anchor="middle" font-size="14" font-weight="700" fill="#002147">콘텐츠</text>
  <path d="M 250 110 Q 300 130 295 160" stroke="#002147" stroke-width="2" fill="none" marker-end="url(#arr)"/>
  <path d="M 295 240 Q 300 270 250 290" stroke="#002147" stroke-width="2" fill="none" marker-end="url(#arr)"/>
  <path d="M 150 290 Q 100 270 105 240" stroke="#002147" stroke-width="2" fill="none" marker-end="url(#arr)"/>
  <path d="M 105 160 Q 100 130 150 110" stroke="#002147" stroke-width="2" fill="none" marker-end="url(#arr)"/>
</svg>
```

### V5. 2×2 매트릭스

```html
<div class="matrix">
  <div class="mx-axis-x">영향력</div>
  <div class="mx-axis-y">대체 가능성</div>
  <div class="mx-cell q1"><div class="mx-title">총괄 기획권</div><div class="mx-note">高영향 · 低대체</div></div>
  <div class="mx-cell q2"><div class="mx-title">운영권</div><div class="mx-note">高영향 · 中대체</div></div>
  <div class="mx-cell q3"><div class="mx-title">IP 소유권</div><div class="mx-note">中영향 · 低대체</div></div>
  <div class="mx-cell q4"><div class="mx-title">수익 쉐어</div><div class="mx-note">中영향 · 中대체</div></div>
</div>
<style>
.matrix { display: grid; grid-template-columns: 40px 1fr 1fr; grid-template-rows: 1fr 1fr 40px; gap: 8px; margin: 32px 0; height: 360px; }
.mx-axis-y { grid-row: 1/3; grid-column: 1; writing-mode: vertical-rl; transform: rotate(180deg); display: flex; align-items: center; justify-content: center; font-size: 12px; color: var(--ink-mute); letter-spacing: 2px; }
.mx-axis-x { grid-row: 3; grid-column: 2/4; display: flex; align-items: center; justify-content: center; font-size: 12px; color: var(--ink-mute); letter-spacing: 2px; }
.mx-cell { border: 1px solid var(--line); border-radius: 10px; padding: 20px; display: flex; flex-direction: column; justify-content: center; }
.mx-cell.q1 { background: var(--accent); color: #000; }
.mx-cell.q1 .mx-note { color: rgba(255,255,255,0.75); }
.mx-cell.q2 { background: var(--accent-soft); }
.mx-cell.q3 { background: var(--bg-alt); }
.mx-cell.q4 { background: #fff; border-style: dashed; }
.mx-title { font-weight: 700; font-size: 16px; margin-bottom: 4px; }
.mx-note { font-size: 12px; color: var(--ink-mute); }
</style>
```

### V6. Big-Number 블록

```html
<div class="bignum-grid">
  <div class="bignum">
    <div class="bn-value">200<span class="bn-unit">~400억</span></div>
    <div class="bn-label">연간 합산 매출 (혼합안 기본)</div>
  </div>
  <div class="bignum">
    <div class="bn-value">2<span class="bn-unit">,000~3,000억</span></div>
    <div class="bn-label">10년 누적 기본 시나리오</div>
  </div>
  <div class="bignum">
    <div class="bn-value">12<span class="bn-unit">개</span></div>
    <div class="bn-label">반드시 박아넣을 계약 조항</div>
  </div>
</div>
<style>
.bignum-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 24px; margin: 32px 0; }
.bignum { padding: 24px; border-top: 3px solid var(--accent); }
.bn-value { font-size: clamp(36px, 5vw, 56px); font-weight: 800; color: var(--accent); line-height: 1; letter-spacing: -0.02em; }
.bn-unit { font-size: 0.5em; font-weight: 600; color: var(--ink-soft); margin-left: 4px; }
.bn-label { margin-top: 10px; font-size: 13px; color: var(--ink-soft); line-height: 1.5; }
</style>
```

### V9. 도넛 (SVG, 비율)

```html
<svg viewBox="0 0 200 200" class="donut" aria-label="수익 분배">
  <circle cx="100" cy="100" r="70" fill="none" stroke="#e8e8ed" stroke-width="28"/>
  <circle cx="100" cy="100" r="70" fill="none" stroke="#002147" stroke-width="28"
    stroke-dasharray="220 440" stroke-dashoffset="0" transform="rotate(-90 100 100)"/>
  <circle cx="100" cy="100" r="70" fill="none" stroke="#6e8fb8" stroke-width="28"
    stroke-dasharray="132 440" stroke-dashoffset="-220" transform="rotate(-90 100 100)"/>
  <text x="100" y="95" text-anchor="middle" font-size="28" font-weight="800" fill="#1d1d1f">100%</text>
  <text x="100" y="115" text-anchor="middle" font-size="11" fill="#86868b">수익 구조</text>
</svg>
```

### V10. 퍼널 (CSS)

```html
<div class="funnel">
  <div class="fn-step" style="width:100%"><span>인지 300만</span></div>
  <div class="fn-step" style="width:70%"><span>방문 189만</span></div>
  <div class="fn-step" style="width:45%"><span>재방문 85만</span></div>
  <div class="fn-step" style="width:20%"><span>팬 전환 38만</span></div>
</div>
<style>
.funnel { display: flex; flex-direction: column; align-items: center; gap: 6px; margin: 32px 0; }
.fn-step { background: var(--accent); color: #000; padding: 14px 0; text-align: center; font-weight: 900; clip-path: polygon(0 0, 100% 0, 95% 100%, 5% 100%); }
.fn-step:nth-child(2) { background: #254a74; }
.fn-step:nth-child(3) { background: #4a709e; }
.fn-step:nth-child(4) { background: #6e8fb8; }
</style>
```

---

## 3. 선택 로직

| 상황 | 선택 |
|------|------|
| 2~6개 항목 수치 비교 | V1 바차트 (기본) |
| 3~5개 축 균형 비교 | V1-b 레이더 |
| 시간축 이벤트 3+ | V2 타임라인 |
| 단계 3~6개 (선형) | V3 플로우 |
| A→B→C→A 되돌아옴 | V4 순환 SVG |
| 2축 교차 분류 | V5 매트릭스 |
| 단일 수치 강조 1~4개 | V6 big-number |
| 100% 내 분할 (2~5 구획) | V9 도넛 |
| 감소 단계 (깔때기) | V10 퍼널 |
| 관계망 (복잡) | V8 노드 그래프 (케이스별 SVG 수동) |

---

## 4. QC — C9 체크

HTML 산출물 생성 후 자가점검:

1. 시각소스(V1~V10 신호) 개수 **n** 파악
2. 적용된 시각요소(차트·다이어그램·타임라인 등) 개수 **m** 파악
3. **판정:**
   - n = 0 → 면제
   - n ≥ 2 & m = 0 → **FAIL** (전환 누락)
   - n ≥ 2 & m ≥ ⌈n/2⌉ → 통과
   - 그 외 → 경고, 1개 이상 추가 전환 권장

4. **색상 점검:** 차트 색이 C3 3색 시스템 이탈? → 무채색 + CTA 1색으로 수정
5. **접근성:** 각 SVG에 `aria-label` 있는가? 없으면 추가

---

## 5. 안티패턴 (피해야 할 처리)

| 안티패턴 | 왜 문제 | 교정 |
|---------|---------|------|
| 수치 비교를 **표로만** 처리 | C9 위반, 비교가 한눈에 안 읽힘 | 표 유지하되 **표 위에 V1 바차트** 추가 |
| ASCII 다이어그램 (`→`·`│`로 그림) | 모바일 깨짐, 접근성 0 | V3·V4 SVG로 승격 |
| 타임라인을 **연도표**로만 | 시간 흐름 시각 부재 | V2 타임라인 삽입 |
| 핵심 수치를 문장 중간에 매립 | 위계 손실 | V6 big-number 블록으로 분리 |
| 동일 SVG 색상 팔레트 3+ 혼재 | C3 위반 | 무채색 농도 + CTA 1색 |
| Chart.js·D3 CDN 기본 투입 | 단일 파일 원칙 위반 | 인라인 SVG·CSS 기본, 형 명시시만 CDN |

---

## 6. 톤별 시각화 조정

| 톤 | 배경 | 차트 기본색 | 특이사항 |
|----|------|------------|---------|
| dark-cinema | 검정 | CTA 1색 + 백색 | 대비 극단, 데이터 라벨 크게 |
| warm-human | 흰색 | 무채 + 따뜻한 CTA | 둥근 모서리, softer shadow |
| clean-info | 흰+그레이 | 무채 + CTA | **기본값**. 가장 많이 씀 |
| pro-grid | 흰+그레이 | 무채 + CTA (Oxford Blue 권장) | 격자 뚜렷, 라벨 정돈 |
| story-dark | 검+흰 교대 | 섹션 배경 따라 반전 | 다크 섹션 차트는 배경 투명 + 밝은 선 |

---

## Gotchas (외부 함정)

| 함정 | 대응 |
|------|------|
| "시각소스 있는데 표로도 충분" 판단 | C9는 표 **제거**가 아니라 **시각요소 추가**. 둘 다 공존 가능 |
| 시각요소 과잉 (문서 절반이 차트) | 시각소스 n개당 최대 n개. 초과 시 서사·맥락 복원 |
| aria-label 누락 | SVG는 항상 `aria-label` + 의미 있는 텍스트. 접근성 = C9 통과조건 |
| 반응형 누락 | 차트·타임라인 모두 ≤640px 미디어쿼리 필수. 가로 스크롤 허용(C8 예외) |
| 인쇄·PDF 변환 시 색 손실 | 데이터 라벨은 **텍스트로도** 함께 표기 (색만으로 구분 금지) |
