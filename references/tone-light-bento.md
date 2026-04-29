# tone-light-bento.md — 낮 모드 벤또

흰 배경 + 6액센트 카드 + 형광펜 적극 + 헤드 900 / 본문 300.

---

## 정체성

- 분석·KPI·캠페인 복기·기능 요약 등 한 장 압축에 최적
- 흰 캔버스에 6액센트 카드를 모자이크
- 형광펜으로 핵심 단어 강조
- 회색 0%

---

## 토큰

```css
.tone-light-bento {
  background: #ffffff;
  color: #000000;
  font-family: "Pretendard Variable", Pretendard, -apple-system, sans-serif;
}

.tone-light-bento h1 { font-weight: 900; font-size: clamp(32px, 5vw, 56px); }
.tone-light-bento h2 { font-weight: 900; font-size: clamp(20px, 3vw, 32px); }
.tone-light-bento p  { font-weight: 300; font-size: clamp(15px, 1.6vw, 18px); line-height: 1.65; }

.tone-light-bento .grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 12px;
}

@media (max-width: 1024px) { .tone-light-bento .grid { grid-template-columns: repeat(2, 1fr); } }
@media (max-width: 640px)  { .tone-light-bento .grid { grid-template-columns: 1fr; } }
```

---

## 카드 6종

```html
<div class="card-white">  <!-- 흰 카드 + 검정 글자 -->
<div class="card-yellow"> <!-- 옐로우 카드 + 검정 글자 -->
<div class="card-mint">   <!-- 민트 카드 + 검정 글자 -->
<div class="card-pink">   <!-- 핑크 카드 + 검정 글자 -->
<div class="card-blue">   <!-- 블루 카드 + 흰 글자 -->
<div class="card-coral">  <!-- 코랄 카드 + 흰 글자 -->
<div class="card-purple"> <!-- 보라 카드 + 흰 글자 -->
```

---

## 형광펜 패턴

```html
<h2>처음부터 <span class="hi-mint">간편하고</span>, 계속해서 <span class="hi-mint">간편한</span> IT.</h2>
```

페이지당 1~3개 단어. 동일 섹션 = 동일 색.

---

## 벤또 패턴 A~E

→ `bento-patterns.md` 참조.

---

## 자가검증

- 배경 #ffffff 인지
- 본문 색 #000000 인지 (회색 ✗)
- 형광펜 1+ 사용
- 헤드 weight 900
- 본문 weight 300
- 12 하한
