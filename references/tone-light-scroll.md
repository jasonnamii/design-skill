# tone-light-scroll.md — 낮 모드 큰글자 스크롤

흰 배경 + 거대 헤드(900) + 본문 300 + 형광펜 적극.

---

## 정체성

- 제품 소개·매니페스토·서사형 압축
- 한 섹션 = 한 화면 = 한 메시지
- 큰글자(XL) ↔ 작은 본문(S)의 극단 대비
- 카드 거의 없음 (있다면 흰 또는 1액센트)

---

## 토큰

```css
.tone-light-scroll {
  background: #ffffff;
  color: #000000;
  font-family: "Pretendard Variable", Pretendard, -apple-system, sans-serif;
}

.tone-light-scroll section {
  min-height: 100vh;
  padding: clamp(40px, 10vh, 120px) clamp(20px, 5vw, 80px);
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.tone-light-scroll .cover {
  font-size: clamp(48px, 8vw, 96px);
  font-weight: 900;
  line-height: 1.05;
  letter-spacing: -0.03em;
  word-break: keep-all;
}

.tone-light-scroll p {
  font-size: clamp(15px, 1.6vw, 18px);
  font-weight: 300;
  line-height: 1.65;
  max-width: 60ch;
}
```

---

## 섹션 패턴 (5종)

```
1. Hero   = 표지 1줄 (XL 900) + 짧은 카피 (S 300)
2. Promise = 약속 1줄 (L 900) + 형광펜
3. Twist   = 반전 1줄 (L 900)
4. Narrative = 본문 카피 (S 300) + 형광펜 1~2개
5. Echo    = 메시지 메아리 (M 900)
```

---

## 형광펜 패턴

```html
<section>
  <h2>한 번의 결정이<br><span class="hi-mint">모든 것</span>을 바꾼다.</h2>
</section>
```

권장 = 민트·옐로우 (낮 위 가독).

---

## 자가검증

- 배경 #ffffff 인지
- 거대 헤드 weight 900
- 본문 weight 300
- 형광펜 1+ 사용
- 한 섹션 = 한 메시지 (G6 ≤2)
