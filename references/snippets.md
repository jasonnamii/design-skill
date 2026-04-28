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

### 한글 줄바꿈 자연화 (C8 R8·R12·R13·R14)

```css
/* 기본 — 한글 박스/본문 전체 (R8) */
.text-ko, .box, .card, p, .body {
  word-break: keep-all;             /* R8 — 어절 단위 끊기 */
  overflow-wrap: break-word;
  text-wrap: pretty;                /* R12 — 마지막 줄 고아 단어 방지 */
  line-height: 1.7;                 /* 한글 가독성 */
}

/* 짧은 헤드라인 (2~4줄) — 줄 길이 균등화 (R13) */
.headline, h1, h2, .title {
  text-wrap: balance;
  word-break: keep-all;
  overflow-wrap: break-word;
  line-height: 1.2;
}

/* 어절 단위 nowrap 보호 (R14) — 끊기면 어색한 동사구·서술절 */
.nowrap { white-space: nowrap; }
```

**사용 패턴:**
```html
<p class="body">
  포트폴리오(실력) 위에 협업이력·평판·관계 <span class="nowrap">데이터를 쌓는다.</span>
</p>
<p class="body">
  프로필 생성 즉시 노출. <span class="nowrap">기다리는 게 아니라</span> <span class="nowrap">기회가 찾아오는 구조.</span>
</p>
```

상세 스니펫은 포맷·톤 스포크 각각 참조.


## 접기/펴기 스크롤 보정 (A — `scrollBy(delta)` 채택)

**원칙:** 접기/펴기 토글 시 viewport 점프 방지. 4안 비교 후 A 채택 (B·C·D 탈락).

| 방안 | 설명 | 평가 |
|---|---|---|
| **A. `scrollBy(delta)`** | 클릭 직후 viewport 중심에 가장 가까운 요소 좌표 캡처. 토글 후 같은 요소 좌표 측정. 차이만큼 보정 | ✅ 채택. 가장 신뢰성 있음 |
| B. `scroll-margin + :target` | CSS만으로 처리 | ✗ 토글은 target 변경이 아님 |
| C. `IntersectionObserver` 기반 | 보이는 요소 추적 | 과한 오버헤드 |
| D. `overflow-anchor` 단독 | 브라우저 자체 앵커링 | summary 토글에 불완전 |

**A 구현:**

```html
<details class="fold">
  <summary>접기/펴기 제목</summary>
  <div class="fold-body">...</div>
</details>

<script>
(function () {
  document.querySelectorAll('details.fold > summary').forEach(function (sum) {
    sum.addEventListener('click', function () {
      var midY = window.innerHeight / 2;
      var anchors = document.querySelectorAll('details, summary, section');
      var anchor = null, minDist = Infinity;
      anchors.forEach(function (el) {
        var r = el.getBoundingClientRect();
        var dist = Math.abs((r.top + r.height / 2) - midY);
        if (dist < minDist) { minDist = dist; anchor = el; }
      });
      if (!anchor) return;
      var beforeTop = anchor.getBoundingClientRect().top;
      requestAnimationFrame(function () {
        requestAnimationFrame(function () {
          var afterTop = anchor.getBoundingClientRect().top;
          var delta = afterTop - beforeTop;
          if (Math.abs(delta) > 1) window.scrollBy(0, delta);
        });
      });
    });
  });
})();
</script>

<style>
details.fold { overflow-anchor: auto; }  /* 보조 — A와 병행 */
</style>
```

**규칙:**
- 모든 `<details class="fold">` 토글에 자동 적용
- viewport 중앙 가까운 요소 기준 보정 (사용자 시선 유지)
- `requestAnimationFrame` 2회 후 측정 (reflow 완료 보장)
- delta 1px 이하 무시 (jitter 방지)
