# tone-dark-scroll.md — 밤 모드 큰글자 스크롤

검정 배경 + 거대 헤드(900) + 본문 300 + 형광펜 적극.

---

## 정체성

- 제품 압축·매니페스토 정점·키노트 헤드라인
- 다크 위 거대 흰 타이포
- 형광펜 = 옐로우·핑크·보라 (밝은 대비)

---

## 토큰

```css
.tone-dark-scroll {
  background: #000000;
  color: #ffffff;
  font-family: "Pretendard Variable", Pretendard, -apple-system, sans-serif;
}

.tone-dark-scroll section {
  min-height: 100vh;
  padding: clamp(40px, 10vh, 120px) clamp(20px, 5vw, 80px);
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.tone-dark-scroll .cover {
  font-size: clamp(48px, 8vw, 96px);
  font-weight: 900;
  line-height: 1.05;
  letter-spacing: -0.03em;
  word-break: keep-all;
  color: #fff;
}

.tone-dark-scroll p {
  font-size: clamp(15px, 1.6vw, 18px);
  font-weight: 300;
  line-height: 1.65;
  max-width: 60ch;
  color: #fff;
}
```

---

## 섹션 패턴

라이트 스크롤과 동일 5종(Hero·Promise·Twist·Narrative·Echo). 컬러만 반전.

---

## 형광펜 패턴

```html
<section>
  <h2>가벼운 <span class="hi-yellow">혁신</span>이<br>모든 것을 <span class="hi-purple">바꾼다</span>.</h2>
</section>
```

---

## 자가검증

- 배경 #000000
- 거대 헤드 weight 900
- 본문 weight 300
- 텍스트 #ffffff (검정 ✗·회색 ✗)
- 형광펜 1+
