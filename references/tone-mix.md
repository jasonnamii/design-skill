# tone-mix.md — 믹스 모드

원페이지 안에서 4톤(낮/밤 × 벤또/스크롤)을 섹션별로 섞음.

---

## 정체성

- 한 페이지 = 다층 서사
- 표지 다크 스크롤 → 본문 라이트 벤또 → 클로징 다크 스크롤 등
- 섹션별로 배경 모드 전환
- 단, 8조 헌법은 모든 섹션에서 동일 적용

---

## 패턴 3종

### 패턴 1 — 다크 인트로 + 라이트 본문 + 다크 클로징

```
Section 1 (dark-scroll)  : Hero 매니페스토 1줄
Section 2 (light-bento)  : 4-col 카드 12개 (KPI·기능)
Section 3 (light-bento)  : 비교 매트릭스 + 형광펜
Section 4 (dark-scroll)  : 클로징 1줄
```

### 패턴 2 — 라이트 인트로 + 다크 본문 + 라이트 클로징

(반전)

### 패턴 3 — 교대 (Alternating)

```
S1 dark-scroll  → S2 light-bento → S3 dark-bento → S4 light-scroll
```

배경 교대 = C7(반복금지) 자동 충족.

---

## 토큰

```css
.tone-mix section.dark   { background: #000; color: #fff; }
.tone-mix section.light  { background: #fff; color: #000; }
.tone-mix section { padding: clamp(40px, 10vh, 120px) clamp(20px, 5vw, 80px); }
```

---

## 전환 시 주의

- 인접 섹션 = 배경 다르게 (dark↔light)
- 형광펜 색은 톤 디폴트 따름 (낮=민트, 밤=옐로우)
- 헤드는 모든 섹션 weight 900
- 본문은 모든 섹션 weight 300

---

## 자가검증

- 섹션마다 배경 = 검정 또는 흰색 (H1)
- 회색 0% (H4)
- 모든 섹션 헤드 weight 900 (H5)
- 모든 섹션 본문 weight 300 (H6)
- 페이지 전체 형광펜 ≥3 (믹스는 더 많이 권장)
