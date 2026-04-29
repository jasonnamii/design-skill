# color-system.md — design-skill v3.0 컬러 시스템 SSOT

design-skill 전체 컬러 단일 권위. 8조 헌법 H1·H2·H4 위임 본체.

---

## 0. 핵심 원칙 (3줄)

1. **배경 = 검정 OR 흰색만.** 그라디언트·다른색 ✗ (H1).
2. **글자색 = 검정·흰색·6액센트만. 회색 원천 금지** (H4).
3. **컬러 사용처 = 박스 배경·시각화·형광펜만** (H2).

---

## 1. 6액센트 팔레트

PDF 21개 + 형 결정 = **6색 + 보라**.

```css
:root {
  /* 배경 (H1) */
  --bg-light: #ffffff;
  --bg-dark:  #000000;

  /* 텍스트 (H4) */
  --text-light: #000000;  /* 라이트 배경 위 */
  --text-dark:  #ffffff;  /* 다크 배경 위 */

  /* 6액센트 — 박스·시각화·형광펜 (H2) */
  --accent-yellow: #f0c850;  /* 옐로우 */
  --accent-mint:   #5dcaa5;  /* 민트 */
  --accent-pink:   #ed93b1;  /* 핑크 */
  --accent-blue:   #378add;  /* 블루 */
  --accent-coral:  #d85a30;  /* 코랄 */
  --accent-purple: #7f77dd;  /* 보라 (v3.0 신규) */

  /* 형광펜 = 액센트 50% 알파 */
  --hi-yellow: rgba(240, 200, 80, 0.5);
  --hi-mint:   rgba(93, 202, 165, 0.5);
  --hi-pink:   rgba(237, 147, 177, 0.5);
  --hi-blue:   rgba(55, 138, 221, 0.4);
  --hi-coral:  rgba(216, 90, 48, 0.4);
  --hi-purple: rgba(127, 119, 221, 0.5);
}
```

---

## 2. 회색 금지 (H4)

**원천 금지:** `#888`·`#666`·`#ccc`·`#999`·`gray`·`grey`·`darkgray`·`lightgray`·`silver` 등 모든 회색 키워드·헥스.

**검증:**
```bash
grep -nE '#([0-9a-f]{3}|[0-9a-f]{6})|gray|grey|silver' output.html
# 매칭 = H4 위반
```

**알파 대체 (극단 예외):**
- 비활성 placeholder: `rgba(0,0,0,0.3)` (라이트) / `rgba(255,255,255,0.3)` (다크)
- 비활성 버튼: `rgba(127, 119, 221, 0.2)` (보라 20%)
- 보더: 검정·흰색·액센트 헥스 그대로 사용 (회색 알파 ✗)

---

## 3. 형광펜 사용법 (H3)

### 기본 패턴

```html
<p>처음부터 <span class="hi-mint">간편하고</span>, 계속해서 <span class="hi-mint">간편한</span> IT.</p>

<style>
  .hi-yellow { background: linear-gradient(transparent 60%, var(--hi-yellow) 60%); padding: 0 2px; }
  .hi-mint   { background: linear-gradient(transparent 60%, var(--hi-mint)   60%); padding: 0 2px; }
  .hi-pink   { background: linear-gradient(transparent 60%, var(--hi-pink)   60%); padding: 0 2px; }
  .hi-blue   { background: linear-gradient(transparent 60%, var(--hi-blue)   60%); padding: 0 2px; }
  .hi-coral  { background: linear-gradient(transparent 60%, var(--hi-coral)  60%); padding: 0 2px; }
  .hi-purple { background: linear-gradient(transparent 60%, var(--hi-purple) 60%); padding: 0 2px; }
</style>
```

### 페이지당 권장 양

- 권장: 1~3개 단어
- 0개 = G7 경고
- 9+ = G7 FAIL

### 컬러 선택

- 동일 섹션 = 동일 색
- 톤(낮/밤)별 디폴트:
  - 낮: 민트·옐로우 권장 (대비)
  - 밤: 옐로우·핑크·보라 권장 (밝은 대비)

---

## 4. 박스(카드) 컬러 (H2)

### 라이트 모드

- 카드 배경: 흰색·6액센트 중 1
- 카드 텍스트: 검정 (흰 카드) 또는 흰색 (액센트 카드)
- 카드 보더: 검정 1px 또는 액센트 1px (회색 ✗)

```css
.card-white  { background: #fff; color: #000; border: 1px solid #000; }
.card-yellow { background: var(--accent-yellow); color: #000; }
.card-mint   { background: var(--accent-mint);   color: #000; }
.card-pink   { background: var(--accent-pink);   color: #000; }
.card-blue   { background: var(--accent-blue);   color: #fff; }
.card-coral  { background: var(--accent-coral);  color: #fff; }
.card-purple { background: var(--accent-purple); color: #fff; }
```

### 다크 모드

- 카드 배경: 검정·6액센트 중 1
- 카드 텍스트: 흰색 (검정 카드) 또는 컬러별 매핑
- 카드 보더: 흰색 1px 또는 액센트 1px

```css
.card-black  { background: #000; color: #fff; border: 1px solid #fff; }
/* 액센트 카드는 라이트와 동일 톤 */
```

---

## 5. 시각화 컬러 (H2)

차트·다이어그램·아이콘에서 6액센트 사용. 카테고리 기반 매핑:

| 의미 | 색 |
|---|---|
| 긍정·성장·완료 | 민트 |
| 경고·강조 | 옐로우 |
| 부정·위험 | 코랄 |
| 정보·기본 | 블루 |
| 감성·관계 | 핑크 |
| 프리미엄·창의 | 보라 |

**원칙:** 색 = 의미 인코딩. 무지개 시퀀스 ✗.

---

## 6. 톤별 컬러 적용

| 톤 | 배경 | 텍스트 | 박스 | 형광펜 |
|---|---|---|---|---|
| `light-bento` | 흰 | 검 | 흰+1~3액센트 | 민트·옐로우 |
| `dark-bento` | 검 | 흰 | 검+1~3액센트 | 옐로우·핑크 |
| `light-scroll` | 흰 | 검 | 거의 없음 | 민트 1~2 |
| `dark-scroll` | 검 | 흰 | 거의 없음 | 옐로우 1~2 |
| `mix` | 섹션별 교대 | 모드별 | 자유 | 자유 |
| `young-playful` | 흰 | 검+컬러 | 6액센트 적극 | 6액센트 적극 |
| `KISAS` | KISAS 팔레트 (별도) | KISAS 정의 | KISAS | KISAS |

---

## 7. CSS 토큰 풀세트

```css
:root {
  /* === 배경 (H1) === */
  --bg-light: #ffffff;
  --bg-dark:  #000000;

  /* === 텍스트 (H4 — 회색 ✗) === */
  --text-on-light: #000000;
  --text-on-dark:  #ffffff;

  /* === 6액센트 (H2) === */
  --accent-yellow: #f0c850;
  --accent-mint:   #5dcaa5;
  --accent-pink:   #ed93b1;
  --accent-blue:   #378add;
  --accent-coral:  #d85a30;
  --accent-purple: #7f77dd;

  /* === 형광펜 (H3) === */
  --hi-yellow: rgba(240, 200, 80, 0.5);
  --hi-mint:   rgba(93, 202, 165, 0.5);
  --hi-pink:   rgba(237, 147, 177, 0.5);
  --hi-blue:   rgba(55, 138, 221, 0.4);
  --hi-coral:  rgba(216, 90, 48, 0.4);
  --hi-purple: rgba(127, 119, 221, 0.5);

  /* === 비활성 알파 (§EXCEPT 극단) === */
  --disabled-on-light: rgba(0, 0, 0, 0.3);
  --disabled-on-dark:  rgba(255, 255, 255, 0.3);
  --disabled-button:   rgba(127, 119, 221, 0.2);
}
```

---

## 8. 자가검증

```bash
# H4 회색 grep
grep -nE '#([0-9a-f]{3}|[0-9a-f]{6})|gray|grey|silver|darkgray|lightgray' output.html | \
  grep -vE 'rgba\(' | \
  grep -vE '#000|#fff|#ffffff|#000000|#f0c850|#5dcaa5|#ed93b1|#378add|#d85a30|#7f77dd'
# 매칭 = H4 위반

# H2 본문 다채색 grep
grep -nE '<p[^>]*style="[^"]*color:[^;]*(red|blue|green|yellow|orange|pink|purple)' output.html
# 매칭 = H2 위반
```
