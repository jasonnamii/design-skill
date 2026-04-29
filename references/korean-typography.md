# korean-typography.md — design-skill v3.0 한글 타이포 SSOT

H5(헤드 900)·H6(본문 300)·H7(12 하한) 위임 본체.

---

## 0. 핵심 원칙 (4줄)

1. **헤드는 무조건 weight 900.** 표지·섹션·본문 헤드·카드 타이틀 모두 (H5).
2. **본문은 weight 300.** 캡션만 400 허용 (H6).
3. **최소 폰트 12px.** clamp 하한 12 절대 (H7).
4. **한글 줄바꿈:** `word-break: keep-all` + `overflow-wrap: break-word` (H8).

---

## 1. Pretendard 5단 스케일

```css
:root {
  --size-xl: clamp(48px, 8vw,   96px);   /* 표지 */
  --size-l:  clamp(32px, 5vw,   56px);   /* 섹션 */
  --size-m:  clamp(20px, 3vw,   32px);   /* 헤드 */
  --size-s:  clamp(15px, 1.6vw, 18px);   /* 본문 */
  --size-xs: clamp(12px, 1vw,   13px);   /* 캡션·라벨 (12 하한) */
}
```

**비율:** 96:56:32:18:12 ≈ 8:4.5:2.5:1.5:1 (C1 4:2.3:1.5:1 ±10% 통과)

---

## 2. Weight 위계 (H5·H6)

| 역할 | Weight | 사용처 |
|---|---|---|
| 표지 타이틀 | **900** | XL 사이즈 |
| 섹션 타이틀 | **900** | L 사이즈 |
| 본문 헤드 (h3, .head) | **900** | M 사이즈 |
| 카드 타이틀 | **900** | M 사이즈 |
| 본문 (p, .body) | **300** | S 사이즈 |
| 캡션 (.caption) | **400** | XS 사이즈 (예외 허용) |
| 라벨 (.label) | **600** | XS 사이즈 (라벨 한정) |

**Weight 대비:** 헤드 900 ↔ 본문 300 = 600 (C2 통과).

---

## 3. CSS 클래스

```css
/* 표지 */
.t-cover {
  font-family: "Pretendard Variable", Pretendard, -apple-system, sans-serif;
  font-size: var(--size-xl);
  font-weight: 900;
  line-height: 1.05;
  letter-spacing: -0.03em;
  word-break: keep-all;
  overflow-wrap: break-word;
}

/* 섹션 */
h1, .t-section {
  font-size: var(--size-l);
  font-weight: 900;
  line-height: 1.15;
  letter-spacing: -0.02em;
  word-break: keep-all;
}

/* 본문 헤드 */
h2, h3, .t-head {
  font-size: var(--size-m);
  font-weight: 900;
  line-height: 1.2;
  letter-spacing: -0.01em;
  word-break: keep-all;
}

/* 본문 */
p, .t-body {
  font-size: var(--size-s);
  font-weight: 300;  /* H6 */
  line-height: 1.65;
  word-break: keep-all;
  overflow-wrap: break-word;
  text-wrap: pretty;
}

/* 캡션 */
.t-caption {
  font-size: var(--size-xs);
  font-weight: 400;
  line-height: 1.4;
}

/* 라벨 (XS 12px 한정 600 허용) */
.t-label {
  font-size: var(--size-xs);
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.16em;
  line-height: 1;
}
```

---

## 4. 한글 줄바꿈 규칙 (H8)

### 필수 CSS

```css
body, h1, h2, h3, h4, p, .body, .head, .section, .cover {
  word-break: keep-all;       /* 어절 단위 끊김 */
  overflow-wrap: break-word;  /* 긴 단어는 줄바꿈 */
}
```

### `<br>` 사용

긴 문장은 의미 단위로 `<br>` 강제:
```html
<h1>처음부터 간편하고,<br>계속해서 간편한 IT.</h1>
```

### 모바일 대응

```css
@media (max-width: 640px) {
  h1.t-cover { font-size: clamp(36px, 9vw, 48px); }
  /* 모바일에서도 12 하한 유지 */
}
```

---

## 5. 12px 하한 (H7)

```css
/* OK */
font-size: 12px;
font-size: clamp(12px, 1vw, 13px);

/* FAIL */
font-size: 11px;
font-size: 10px;
font-size: clamp(10px, 1vw, 12px);  /* 하한 미달 */
```

**예외 ✗:** 어떤 라벨·캡션·푸터도 12 미만 ✗.

---

## 6. 자가검증

```bash
# H5: 헤드 weight 900 확인
grep -nE 'h[1-3][^>]*style[^>]*font-weight:\s*[1-8]00' output.html
# 매칭 = H5 위반

# H6: 본문 weight ≥600 확인
grep -nE '<p[^>]*style[^>]*font-weight:\s*[6-9]00' output.html
# 매칭 = H6 위반

# H7: 12 미만 확인
grep -nE 'font-size:\s*([0-9]|1[01])px(?!\d)' output.html
# 매칭 = H7 위반

# H8: word-break 확인
grep -q 'word-break:\s*keep-all' output.html || echo "H8 위반: word-break 누락"
```

---

## 7. Gotchas

- **본문 굵기 끌어올림:** 본문 = 300 절대. "조금 굵게" = H6 위반
- **헤드 사이즈 작아도:** 카드 타이틀이 16px여도 weight 900 (H5)
- **회색 굵기로 대체 불가:** "굵으면 회색이라도?" = H4 위반
- **clamp 하한 잊음:** 모바일 12 미만 ✗
- **letter-spacing -0.05em 이상:** 한글 깨짐. -0.03 이하만
- **line-height 1.4 미만 본문:** 한글 가독성 저하. 1.65 권장
