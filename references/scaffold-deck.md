# scaffold-deck.md — HTML 슬라이드 발표 가이드

`assets/deck-stage.js` 웹컴포넌트 사용법.

---

## 정체성

- HTML로 키노트/PPT급 슬라이드 발표 제작
- 1920×1080 디자인 기준 + 자동 스케일 + 키보드 네비
- Print → Save as PDF로 1슬라이드 1페이지 PDF 출력
- 8조 헌법 100% 적용

---

## 기능

`deck-stage.js`가 제공하는 것:
- ←/→ · PgUp/PgDn · Space · Home/End · 숫자키 네비게이션
- R 키로 첫 슬라이드 리셋
- 우하단 슬라이드 카운터 + 단축키 힌트 (idle 시 페이드)
- localStorage에 현재 인덱스 저장 (refresh 후 복원)
- @media print = 슬라이드별 1페이지 PDF
- 1920×1080 → 뷰포트 자동 스케일 + 레터박스
- `slidechange` 커스텀 이벤트 (index·reason 포함)

---

## 사용법

```html
<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>발표 제목</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.css">
  <style>
    /* 슬라이드 공통 — H 헌법 */
    section.slide {
      background: #000; color: #fff;
      font-family: "Pretendard Variable", Pretendard, -apple-system, sans-serif;
      padding: 80px 120px;
      display: flex; flex-direction: column; justify-content: center;
    }
    section.slide.light { background: #fff; color: #000; }
    h1.title { font-size: 140px; font-weight: 900; letter-spacing: -0.04em; line-height: 0.95; }
    h2.section { font-size: 64px; font-weight: 900; letter-spacing: -0.03em; }
    p.body { font-size: 32px; font-weight: 300; line-height: 1.5; }
    .hi-mint { background: linear-gradient(transparent 60%, rgba(93,202,165,0.5) 60%); padding: 0 4px; }
  </style>
</head>
<body>
  <deck-stage width="1920" height="1080">
    <section class="slide" data-label="Title">
      <h1 class="title">한 줄로<br>전부.</h1>
    </section>

    <section class="slide light" data-label="Promise">
      <h2 class="section">가장 무거운 글자가<br><span class="hi-mint">가장 가벼운</span> 글자를 만난다.</h2>
    </section>

    <section class="slide" data-label="Closing">
      <h1 class="title">Think<br>Output.</h1>
    </section>
  </deck-stage>

  <script src="assets/deck-stage.js"></script>
</body>
</html>
```

---

## 7슬라이드 베이스 (권장)

1. **Title** — 거대 타이틀 1줄
2. **Section** — 섹션 구분 + 라벨
3. **Quote** — 인용 (보라 형광펜)
4. **Think** — Think [Word] 패턴
5. **Compare** — Before/After 비교
6. **Bento** — 4-col 그리드 한 장
7. **Closing** — 마침 1줄

---

## PDF 출력

브라우저 → Print (Cmd/Ctrl+P) → "PDF로 저장"
- @media print 룰이 자동 적용
- 1슬라이드 = 1페이지 (1920×1080 비율 유지)
- 컬러 출력 옵션 ON 권장

---

## 자가검증

- 모든 슬라이드 배경 = 검 또는 흰 (H1)
- 회색 0% (H4)
- 헤드 weight 900 (H5)
- 본문 weight 300 (H6)
- 형광펜 페이지 평균 1+ (H3)
- 1920×1080 캔버스에 맞게 콘텐츠 배치 (overflow ✗)

---

## 라이선스

원본: `_source/jasonnamii/apple-design-style` (Apple Keynote Design System).
deck-stage.js는 원본 그대로 흡수, MIT 호환.
