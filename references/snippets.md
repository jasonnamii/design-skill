# snippets.md — design-skill 스니펫 인덱스

허브형 스킬 특성상 **스니펫은 포맷·톤별로 분산**. 이 파일은 **인덱스**만 담당. 풀스펙은 기존 20개 스포크에 유지.

---

## 포맷별 스니펫

| 포맷 | 스포크 | 포함 |
|---|---|---|
| HTML | `format-html.md` + `visualization-html.md` | 섹션 구조·차트·빅넘버·플로우·타임라인·매트릭스 |
| MD | `format-md.md` + `protocol-pretty.md` | 콜아웃·테이블·수평선·헤딩 위계·이쁘니 문법 |
| PPTX | `format-pptx.md` | 마스터 슬라이드·폰트 pt·레이아웃 압축 |
| DOCX | `format-docx.md` | heading 스타일·여백·테마 |
| XLSX | `format-xlsx.md` | 행 높이·열 너비·셀 스타일 |
| PDF | `format-pdf.md` | 임베딩·정적 레이아웃 |

## 톤별 스니펫 (L1 6톤)

| 톤 | 스포크 | 컨텍스트 |
|---|---|---|
| dark-cinema | `tone-dark-cinema.md` | 무게감·권위 |
| warm-human | `tone-warm-human.md` | 따뜻함·인간성 |
| clean-info | `tone-clean-info.md` | 미니멀·정보성 |
| pro-grid | `tone-pro-grid.md` | 구조적·분석 |
| story-dark | `tone-story-dark.md` | 서사·극적 |
| young-playful | `tone-young-playful.md` | K-12 Apple·키사스 디폴트 |

## 엔진·프로토콜

| 파일 | 역할 |
|---|---|
| `engine-4layer.md` | L1~L4 4층 엔진 풀매칭표·충돌 해결 |
| `protocol-pretty.md` | MD 이쁘니 SSOT |
| `visualization-html.md` | C9 시각 전환 (수치→차트·프로세스→플로우 등) |
| `responsive.md` | C8 반응형 상세 (R1~R11) |
| `ux-principles.md` | Nielsen 10 + Norman 5 + G_AXIOM_MAPPING |
| `special-features.md` | S9 형광펜·S14 그래디언트·S15·S16 특수 패턴 |
| `core-rules.md` | CORE 9규칙 상세 |
| `gotchas-extended.md` | 함정 상세 |

## 로딩 규칙 (작업당 최대 3스포크)

| 작업 | 로드 |
|---|---|
| MD 생성 | `format-md.md` + `tone-*.md` + `protocol-pretty.md` |
| HTML 생성 | `format-html.md` + `tone-*.md` + `visualization-html.md` |
| PPTX 생성 | `format-pptx.md` + `tone-*.md` |
| §2 진입 | + `engine-4layer.md` (1회) |
| S9·S14~S16 매칭 | + `special-features.md` |
| CORE FAIL 재검 | + `ux-principles.md` |

## 공통 프리미티브 (허브 레벨)

### 색상 변수 3분리 (apple-box-design 공유)

```css
:root {
  /* 라이트 모드: 모든 텍스트 검정 (회색 추방) */
  --label-info:    #000;
  --label-caption: #000;
  --label-deco:    #000;
}

/* 검정 배경에서만 흰글자 예외 */
.dark, [style*="background:#000"], [style*="background:#1d1d1f"], [style*="background:#002147"] {
  --label-info:    #fff;
  --label-caption: #fff;
  --label-deco:    #fff;
}

/* 컬러 카드 배경 위 = 항상 검정 글자 (흰글자 ✗) */
.card-pink, .card-yellow, .card-lime, .card-cyan, .card-violet,
.card-mint, .card-soft-purple, .card-vivid-pink, .card-sky, .card-warm-yellow {
  --label-info:    #000;
  --label-caption: #000;
  --label-deco:    #000;
}
```

### 카드 컬러 팔레트 (라이트=캔디 A, 다크=파스텔)

```css
/* 라이트 모드 캔디 A — 카드 배경 */
.card-pink   { background: #FF4D8F; color: #000; }
.card-yellow { background: #FFCB05; color: #000; }
.card-lime   { background: #4DD964; color: #000; }
.card-cyan   { background: #3DB3FF; color: #000; }
.card-violet { background: #A855F7; color: #000; }

/* 다크 모드 파스텔 — 카드 배경 */
.card-mint         { background: #a8e6cf; color: #000; }
.card-soft-purple  { background: #d4b8ff; color: #000; }
.card-vivid-pink   { background: #ff6482; color: #000; }
.card-sky          { background: #64d2ff; color: #000; }
.card-warm-yellow  { background: #ffd60a; color: #000; }

/* 카드 제목 wght 900 강제 (C2 weight 대비 600+) */
.card h2, .card h3, .card .title {
  font-weight: 900;
  color: #000;
}
.card p, .card .body, .card .caption {
  font-weight: 300;
  color: #000;
}
```

### 벤토 그리드 (C8 안전)

```css
.grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 24px;
}
.box {
  min-width: 0;
  overflow: hidden;
}
```

### 한글 줄바꿈 (C8 R4a)

```css
.text-ko {
  word-break: keep-all;
  overflow-wrap: break-word;
}
```

상세 스니펫은 포맷·톤 스포크 각각 참조.
