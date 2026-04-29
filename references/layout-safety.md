# Layout Safety — HTML 벤토·그리드 붕괴 방지 상세

벤토 그리드 설계 시 **필수 체크리스트 + 실전 CSS 템플릿 + 증상→원인 디버그 테이블**. 모바일·태블릿 붕괴 0건을 목표.

---

## 1. 증상 → 원인 역추적

| 증상 (육안) | 첫 의심 원인 | 검증 방법 |
|-------------|------------|----------|
| 한글 세로 1글자씩 떨어짐 | `word-break: break-word`·`break-all` 적용 | DevTools → 해당 요소 `word-break` 확인 |
| 카드가 화면 밖 잘림 | base `grid-column: span N` @media 미리셋 | grep `grid-column:\s*span` → @media 리셋 커버 확인 |
| 전체 횡스크롤 발생 | ①img/table max-width 미설정 ②고정 min-width ③패딩 누적 | `document.scrollWidth > innerWidth` 요소 찾기 |
| 카드 안 텍스트 튀어나옴 | flex/grid 자식 `min-width:auto` 기본값 | DevTools → `min-width` 확인 |
| 모바일에서 4열 유지 | @media에서 일부 컴포넌트 span 리셋 누락 | base span 선언 전수 열거 후 @media 커버 확인 |
| 다크카드 내용 비어 보임 | `min-height` 고정 + 콘텐츠 미주입 | DevTools → 자식 노드 존재 확인 |
| 태블릿 2열에서 1열 일부 카드 튀어나옴 | @media 1024px에서 특정 span 리셋 빠짐 | 1024px 구간 선택자 전수 대조 |
| **진블루/다크 박스 안 글자 안 읽힘** | inline `style="color:#424245"` + `.dark`/`.hot` 조합 → 역매핑 무력화 | `grep -n 'style="[^"]*color:' *.html` → 전수 제거 |
| **다크 박스 캡션이 배경과 뭉개짐** | `--muted` 단일 변수 또는 다크 역매핑 CSS 누락 | `:root { --label-caption }` + `.dark { --label-caption:#d1d1d6 }` 존재 확인 |

---

## 2. 실전 CSS 템플릿 (벤토 base)

```css
/* === RESET === */
*, *::before, *::after { box-sizing: border-box; }
html, body { margin: 0; padding: 0; }
img, svg, video, iframe { max-width: 100%; height: auto; display: block; }
table { table-layout: fixed; width: 100%; border-collapse: collapse; }

/* === 한글 기본 === */
body {
  word-break: keep-all;
  overflow-wrap: break-word;
  line-break: strict;
}

/* === 그리드 === */
.grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 12px;
}
.grid > * { min-width: 0; }   /* 🔴 필수 — 자식 수축 허용 */

/* span 유틸 */
.col-1 { grid-column: span 1; }
.col-2 { grid-column: span 2; }
.col-3 { grid-column: span 3; }
.col-4 { grid-column: span 4; }

/* 명명 컴포넌트 span */
.hero         { grid-column: span 2; }
.section-head { grid-column: span 4; }
.closing      { grid-column: span 4; }
.think        { grid-column: span 2; }
.elev         { grid-column: span 3; }

/* === 색상 3변수 (라이트 기본) === */
:root {
  --label-info:    #1d1d1f;
  --label-caption: #000;  /* 회색 추방 (라이트 모드) */
  --label-deco:    #000;  /* 회색 추방 (라이트 모드) */
}
body { color: var(--label-info); }
.caption, .case, .xs.info { color: var(--label-caption); }
.deco, .date, .tag, .num  { color: var(--label-deco); }

/* === 카드 === */
.card {
  background: #fff;
  border-radius: 20px;
  padding: 28px 30px;
  min-width: 0;                /* 🔴 grid 자식 */
  overflow: hidden;            /* 내부 텍스트 이탈 방지 */
}
.card.dark { background: #002147; color: var(--label-info); }

/* === 🔴 다크 컨테이너 3변수 역매핑 === */
.dark, .key, .hot, .now, .region.hot, .think.dark, .card.dark, [class*="-dark"] {
  --label-info:    #fff;
  --label-caption: #fff;    /* #424245·#6e6e73 다크배경 FAIL */
  --label-deco:    #000;  /* 회색 추방 (라이트 모드) */
  color: var(--label-info);
}
.dark .caption, .dark .case, .hot .caption, .hot .case,
.think.dark .case { color: var(--label-caption); }
.dark .deco, .dark .date, .dark .tag, .dark .num,
.hot .deco, .hot .date, .hot .num { color: var(--label-deco); }

/* === @media 1024px === */
@media (max-width: 1024px) {
  .grid { grid-template-columns: repeat(2, 1fr); gap: 10px; }
  /* 🔴 base span 박힌 모든 선택자 전수 리셋 */
  .col-3, .col-4,
  .hero, .section-head, .closing, .think, .elev
  { grid-column: span 2; }
}

/* === @media 640px === */
@media (max-width: 640px) {
  .grid { grid-template-columns: 1fr; gap: 10px; }
  .col-1, .col-2, .col-3, .col-4,
  .hero, .section-head, .closing, .think, .elev
  { grid-column: span 1; }
  .card { padding: 20px 22px; }
}
```

---

## 3. 한글 줄바꿈 결정 트리

| 콘텐츠 유형 | word-break | overflow-wrap | line-break | 비고 |
|-----------|------------|---------------|------------|------|
| 한글 본문 | `keep-all` | `break-word` | `strict` | 어절 단위 줄바꿈 |
| 한글·영문 혼용 | `keep-all` | `break-word` | `strict` | 한글 우선 |
| 영문 URL·코드 | `normal` | `anywhere` | — | 단어 중간 쪼개기 허용 |
| mono·태그·뱃지 | `normal` | `normal` | — | `white-space: nowrap` + `max-width: 100%` + `text-overflow: ellipsis` |

**금지 조합:**
- ❌ 한글 + `word-break: break-all` → 매 글자 줄바꿈 (세로 낙하)
- ❌ 한글 + `word-break: break-word` → Safari/구브라우저 세로 낙하
- ❌ 한글 + `overflow-wrap: anywhere` 단독 → 글자 중간 쪼갬

---

## 4. 디버그 순서

1. **DevTools → Device Mode** (360·390·480·640·768·1024px)
2. 콘솔에서 `document.scrollWidth === window.innerWidth` 확인
3. `>` 이면 "가장 넓은 자식" 찾기:
   ```js
   [...document.querySelectorAll('*')]
     .filter(el => el.scrollWidth > el.clientWidth)
     .forEach(el => console.log(el, el.scrollWidth, el.clientWidth))
   ```
4. 범인 요소 역추적 → §1 증상표 매칭
5. 처방 적용 → 재실측

---

## 5. body overflow-x: hidden 금지 이유

임시방편으로 `body { overflow-x: hidden }` 넣으면 증상만 숨김. 실제로:
- 모바일에서 터치 스크롤이 일부 OS에서 먹통
- 붕괴 원인이 코드에 남아 다음 수정에서 재발
- 접근성 도구(스크린리더)가 잘린 콘텐츠 못 읽음

**원칙:** 증상을 숨기지 말고 원인을 고친다. overflow-x: hidden은 최후 임시수단이며 반드시 TODO 주석.

---

## 6. 체크리스트

- [ ] `* { box-sizing: border-box }` 적용
- [ ] `img,svg,video,iframe { max-width: 100% }`
- [ ] `body { word-break: keep-all; overflow-wrap: break-word }`
- [ ] `.grid > * { min-width: 0 }`
- [ ] base `grid-column: span N` 박힌 모든 선택자 grep → @media 1024·640 전수 리셋
- [ ] `white-space: nowrap` 요소에 `max-width: 100%; text-overflow: ellipsis`
- [ ] 360·390·480·640·768·1024px 실측 횡스크롤 0
- [ ] `body { overflow-x: hidden }` 없음
- [ ] 다크카드 내부 콘텐츠 실제 렌더 확인 (min-height만 있고 비지 않음)
- [ ] CSS 변수 3분리 선언 (`--label-info`·`--label-caption`·`--label-deco`)
- [ ] 다크 컨테이너(`.dark`·`.hot`·`.key`·`.now`·`.region.hot`·`.think.dark`) 전부 3변수 역매핑
- [ ] 다크 배경 Tier 2 = `#d1d1d6` (`#424245`·`#6e6e73` 다크 0건)
- [ ] inline `style="color:..."` 전수 0건 (`grep -n 'style="[^"]*color:' *.html`)
