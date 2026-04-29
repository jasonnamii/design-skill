# tone-dark-bento.md — 밤 모드 벤또

검정 배경 + 6액센트 카드 + 형광펜 적극 + 헤드 900 / 본문 300.

---

## 정체성

- 다크 무드·엔터프라이즈·매니페스토 한 장
- 검정 캔버스에 6액센트 카드를 모자이크
- 형광펜은 옐로우·핑크·보라 권장 (밝은 대비)

---

## 토큰

```css
.tone-dark-bento {
  background: #000000;
  color: #ffffff;
  font-family: "Pretendard Variable", Pretendard, -apple-system, sans-serif;
}

.tone-dark-bento h1 { font-weight: 900; font-size: clamp(32px, 5vw, 56px); color: #fff; }
.tone-dark-bento h2 { font-weight: 900; font-size: clamp(20px, 3vw, 32px); color: #fff; }
.tone-dark-bento p  { font-weight: 300; font-size: clamp(15px, 1.6vw, 18px); line-height: 1.65; color: #fff; }
```

---

## 카드 6종 (다크)

```html
<div class="card-black">  <!-- 검 카드 + 흰 글자 + 흰 보더 -->
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
<h2>가벼운 <span class="hi-yellow">혁신</span>으로<br><span class="hi-purple">새로운 가치</span>를 만든다.</h2>
```

다크 위 권장 = 옐로우·핑크·보라 (대비 높음).

---

## 자가검증

- 배경 #000000 인지
- 본문 색 #ffffff 인지 (검정 ✗·회색 ✗)
- 형광펜 1+ 사용
- 헤드 weight 900
- 본문 weight 300
- 12 하한
