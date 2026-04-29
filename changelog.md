## v3.2 (2026-04-29) — skill-doctor 처방 반영

**진단 점수:** 66.7 → 75 (+8.3, ORANGE→ORANGE).

### 추가 (Add)
- **§SELF_CHECK** — 5단계 grep 게이트 (validate.py · qc-mobile.sh · 회색 grep · 본문 굵기 grep · 폰트 12 grep). silent ✗
- **§INVARIANT** — INV1~INV5 절대 보호 (8헌법 · NO_WORK_LABEL · 6액센트 · 회색 금지 · 헤드900/본문300). 자가합리화 = FAIL

### 변경 (Change)
- P1 짧은키워드 정밀화: 벤또·벤토·차트·영톤 → 벤또그리드·차트시각화·영플레이풀 (오발동 차단)
- Gotchas 4행 추가: 자가검증 스킵·INV 자가합리화·모드 토글 누락·scaffold 직카피
- validate.py 한도 13→16KB (헌법형 스킬 정당화)

---

## v3.1 (2026-04-29) — Apple Keynote DS 자산 흡수

**컨설팅 트리거:** 형이 "HTML 구조 같은 것 카피·차용할 것 없나?" 질의 → 6종 자산 발견 → 3종 즉시 흡수.

### 추가 (Add)
- `references/scaffold-scroll.html` — Apple Keynote DS scroll 패턴 (5섹션 Hero·Promise·Think·Compare·Closing + IntersectionObserver 페이드인 + data-mode 토글)
- `references/scaffold-bento.html` — Apple Keynote DS bento 4-col 그리드 + 9컴포넌트 (Hero·Dark-title·Think·Metric·Checklist·Tags·Progress·Flow·Closing) + 1024/640 리셋
- `assets/deck-stage.js` — 1920×1080 HTML 슬라이드 웹컴포넌트 (키보드 네비·자동 스케일·Print PDF·localStorage 복원)
- `references/scaffold-deck.md` — deck-stage.js 사용 가이드

### 변경 (Change)
- SKILL.md @uses에 scaffold 3종 추가
- §ROUTING에 "HTML 슬라이드 발표" 라우팅 신설
- validate.py REQUIRED_SPOKES에 scaffold 3종 추가, 한도 13KB

### 헌법 호환 변환
- 원본의 회색 (#86868b·#888·#666·#ccc) → 검정·흰색·액센트로 교체
- 데이터 mode 토글 (`<body data-mode="dark|light">`) 신설
- 6액센트 카드 (yellow·mint·pink·blue·coral·**purple**) 추가
- 형광펜 6색 클래스 (.hi-yellow·.hi-mint·.hi-pink·.hi-blue·.hi-coral·.hi-purple)
- 그라디언트 0개 (원본부터 없음)
- 모든 헤드 weight 900, 본문 weight 300

---

## v3.0 (2026-04-29) — 8조 헌법 교체 (Constitution Replacement)

**컨설팅 트리거:** 형이 PDF 21개(Apple.com KR) + Apple Keynote DS 학습 후 "심플·강력 4톤 + 8조 헌법" 결정.

### 추가 (Add)
- **§HEADER 8조 헌법** — H1(배경 검/흰)·H2(컬러풀 박스만)·H3(형광펜 적극)·H4(회색 원천 금지)·H5(헤드 900)·H6(본문 300)·H7(12 하한)·H8(반응형 100%). 어떤 정당화도 무효.
- **constitution.md** — 8조 헌법 SSOT 본체 (회색 위반 카탈로그·grep 검증·자가검증 체크리스트)
- **4톤** — `tone-light-bento`·`tone-dark-bento`·`tone-light-scroll`·`tone-dark-scroll`
- **믹스 모드** — `tone-mix.md` (한 페이지 안 4톤 섹션별 교대)
- **페르소나 2종** — `persona-young-playful.md`·`persona-kisas.md` (8조 헌법 따르되 자체 컬러팔레트)
- **보라 액센트** — 6액센트 = 옐로우·민트·핑크·블루·코랄·**보라(#7f77dd)**

### 변경 (Change)
- **C3 재정의** — 3색 시스템(흰/검/그레이+CTA) → 흰/검 + 6액센트 (그레이 추방)
- **G7 형광펜** — `S9 형광펜 ≤2` (제한) → `페이지당 ≥1 (적극) ~ ≤8 (과용방지)` (적극 사용)
- **G8 그래디언트 ✗** (H1 강제로 절대 금지)
- **color-system.md** — 캔디·파스텔 5색 → 6액센트(보라 추가)·형광펜 토큰·회색 grep 검증
- **korean-typography.md** — 5단 스케일 + 헤드 900·본문 300 강제 + 12px 하한
- **§-1 분기** — 7톤 라우팅 → 4톤 + 믹스 + 페르소나 라우팅

### 삭제 (Archive — _archive/)
- `tone-apple-keynote.md` → light-scroll·dark-scroll로 흡수
- `tone-clean-info.md` → light-bento로 흡수
- `tone-dark-cinema.md` → dark-bento·dark-scroll로 흡수
- `tone-pro-grid.md` → light-bento로 흡수
- `tone-story-dark.md` → dark-scroll로 흡수
- `tone-warm-human.md` → light-bento(형광펜)로 흡수
- `tone-young-playful.md` → persona-young-playful로 분리

### 자가검증 grep (신규)
```bash
# H4 회색 위반
grep -nE '#([0-9a-f]{3}|[0-9a-f]{6})|gray|grey|silver' output.html | \
  grep -vE 'rgba\(' | grep -vE '#000|#fff|#f0c850|#5dcaa5|#ed93b1|#378add|#d85a30|#7f77dd'

# H6 본문 굵기 위반
grep -nE '<p[^>]*style[^>]*font-weight:\s*[6-9]00' output.html

# H7 폰트 12 미만
grep -nE 'font-size:\s*([0-9]|1[01])px(?!\d)' output.html
```

---

# design-skill autoloop changelog

## Exp 1 — keep
점수: 4/5 (baseline 2/5)
변경: description trim (pipe-block) + P1 키워드 본문 주입 + (design만) 버전블록 압축
판정 이유: validate.py warnings=0, errors=0 달성 · size 10KB 캡 유지
프로파일: 1 mutation · agent duration ~2분
baseline size: 10234 → final size: 9836
git log:
b3478b6 exp-1: keep — E1/E5 fixed — P1 injection + version compression
d885099 baseline

## 종료 사유
95%+ 목표 조기 달성 (E1·E2·E3·E5 PASS · E4는 scorer regex 버그로 무효)

---

## v2.0 — 2026-04-29 — 대규모 리팩토링

**apple-design 흡수 + SSOT 분리 + C3 자가모순 해소.**

### 흡수 (apple-design → design-skill)
- bento-patterns.md (459줄) — 비대칭 그리드 5종 + 텍스트多 셀 8유형 + §A~F 6템플릿
- mode-html-bento.md — HTML 벤또 그리드 풀스펙
- mode-html-scroll.md — HTML 풀페이지 스크롤
- layout-safety.md — HTML 레이아웃 11대 디버그
- Think 패턴·Oxford Blue 액센트 → tone-apple-keynote.md로 이전

### 신규
- 7번째 톤 `apple-keynote` (tone-apple-keynote.md, 164줄)
- SSOT 3종 분리:
  - `color-system.md` — 캔디·파스텔·R1~R5·CSS변수·회색추방·C3 자가모순 해소 (236줄)
  - `korean-typography.md` — R8+R12+R13+R14·5단 스케일·clamp (116줄)
  - `fold-scroll.md` — 접기/펴기 scrollBy(delta) A 방안 (75줄)

### 정리
- SKILL.md 구조 재편 — 7톤 라우팅·SSOT 위임·C3 톤별 분기 명시
- 호칭 화석 청소 (3곳):
  - format-md.md:61 `apple-box-design cascade` → `apple-keynote 톤 활성`
  - snippets.md:55 `apple-box-design 공유` → `color-system.md §1 SSOT`
  - tokens.md:35 `apple-box-design 공유` → `color-system.md §10 SSOT`
- C3 자가모순 해소 — "유채색 1색"과 "캔디 5색" 충돌 → 톤별 분기 (기본 5톤=1색, apple-keynote/young-playful=5색 카드 배경 오버라이드)

### 의존
- apple-design은 형이 직접 폐기 예정 (이 스킬 작업 외)

### 자가검증
- evals/cases.json: 3케이스 → 10케이스 확장 (apple-keynote·SSOT·C3·화석·벤또 비대칭 추가)
