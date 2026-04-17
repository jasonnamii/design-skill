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

## 필수 규칙 R1~R7

| # | 규칙 | 값 | 판정 |
|---|------|-----|------|
| R1 | 폰트 clamp | L1 `clamp(32px, 6vw, 64px)` · L2 `clamp(22px, 3vw, 36px)` · L3 `clamp(17px, 1.8vw, 24px)` · L4 `clamp(13px, 1.2vw, 16px)`. 톤별 변형 가능하되 C1 비율 4:2.3:1.5:1 유지 | 고정px→FAIL |
| R2 | viewport 메타 | `<meta name="viewport" content="width=device-width, initial-scale=1">` | 누락→FAIL |
| R3 | 터치 타겟 | CTA·링크·버튼 ≥ 44×44px | <44→FAIL |
| R4 | 그리드 붕괴 | 데스크탑 다열 → 태블릿 2열 → 모바일 1열. 기본: `grid-template-columns: repeat(auto-fit, minmax(280px, 1fr))` | 고정 다열→FAIL |
| R5 | 횡스크롤 금지 | 긴 테이블·코드는 `overflow-x: auto` 또는 분할 | 발생→FAIL |
| R6 | 패딩 축소 | 데스크탑 80~120px → 모바일 20~32px (미디어쿼리) | 모바일 80+→경고 |
| R7 | 이미지 반응형 | `max-width: 100%; height: auto` 기본 | 고정 width→경고 |

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

## 미디어쿼리 템플릿

```css
/* 모바일 우선 기본값 */
.container { padding: 20px; }
.grid { grid-template-columns: 1fr; gap: 16px; }
h1 { font-size: clamp(32px, 6vw, 64px); }

/* 태블릿 */
@media (min-width: 641px) {
  .container { padding: 40px; }
  .grid { grid-template-columns: repeat(2, 1fr); }
}

/* 데스크탑 */
@media (min-width: 1025px) {
  .container { padding: 80px; }
  .grid { grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); }
}
```

---

## QC 체크리스트

- [ ] R1: 모든 폰트 크기가 clamp() 또는 상대단위(rem·em·vw)
- [ ] R2: `<head>`에 viewport 메타 존재
- [ ] R3: CTA·버튼·링크 실측 ≥44×44px
- [ ] R4: 다열 그리드가 모바일에서 1열로 붕괴
- [ ] R5: 모바일 실기기 또는 DevTools 375px 뷰포트에서 횡스크롤 없음
- [ ] R6: 모바일 패딩 ≤32px
- [ ] R7: 이미지 `max-width:100%` 적용
