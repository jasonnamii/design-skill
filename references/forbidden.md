# forbidden.md — design-skill 금칙 (4블록 인덱스)

6포맷 공통 + 포맷별 금지. **CORE 9규칙·GUARD 8규칙이 상위**. 이 파일은 금칙 체크리스트 통합본.

> 공통 금칙: `VAULT/_skills research/html-skill-refactor/spine.md §공통 금칙`
> 축2 옵시디언: `VAULT/_skills research/html-skill-refactor/axis2-obsidian-rendering.md`
> 축3 브라우저: `VAULT/_skills research/html-skill-refactor/axis3-browser-email.md`
> 축4 PPTX/PDF: `VAULT/_skills research/html-skill-refactor/axis4-pptx-pdf-conversion.md`

---

## CORE FAIL (위반 불가)

| # | 금지 | 결과 |
|---|---|---|
| C1 | 타이포 비율 4:2.3:1.5:1 ±10% 이탈 | FAIL |
| C2 | 제목·본문 weight 차이 <300 | FAIL |
| C3 | 유채색 2개+ | FAIL |
| C5 | 본문 중앙정렬 (md 외) | FAIL |
| C6 | 이미지-텍스트 오버레이 | FAIL |
| C8 | 반응형 위반 (고정 px·viewport 누락·터치 <44·≤640 다열·횡스크롤) | FAIL |
| C9 | HTML 시각소스 2+ & 시각요소 0 | FAIL |

상세: `→ SKILL.md §1. CORE` · `→ core-rules.md`.

## GUARD 경고

| # | 초과 시 |
|---|---|
| G1 | 이미지 비율 4+ → 경고 |
| G2 | CTA 섹션당 3+ → FAIL |
| G3 | 인용 ≤L3 → 경고 |
| G4 | 테이블 7열+ → 분할 |
| G5 | 폰트 단계 5+ → FAIL |
| G6 | S7 감성선언 3+ → 경고 |
| G7 | S9 형광펜 블록당 3+ → 경고 |
| G8 | S14 그래디언트 2+ → FAIL |

## 전역 금지 (모든 포맷)

| 금지 | 이유 |
|---|---|
| `position: fixed` | PDF/PPTX 무시·옵시디언 붕괴 |
| viewport 단위 단독 (`vw`/`vh`) | PPTX 무의미 |
| `<script>` | 옵시디언·PPTX·PDF 차단 |
| `<style>` / `<link>` / class | 옵시디언 미지원 |

## HTML 반응형 11대 (C8 상세)

| # | 원인 | 처방 |
|---|---|---|
| R1 | 암시적 그리드 트랙 span 리셋 누락 | @media에서 전수 리셋 |
| R1a | 데스크탑-먼저 설계 관성 | mobile-first 375px 선설계 |
| R2 | CSS 특이도 역전 | @media ≥ base |
| R3 | flex 자식 `min-width:auto` | `min-width: 0` |
| R4a | 한글 `break-word`·`break-all` | `word-break: keep-all; overflow-wrap: break-word` |
| R4b | 영문·URL·mono | 영문 컨테이너만 `anywhere` |
| R5 | `white-space: nowrap` + 긴 텍스트 | 장식 외 금지 |
| R6 | img·table·iframe max-width 누락 | `max-width:100%; height:auto` |
| R7 | 패딩+폰트 고정px 누적 | 모바일 20~24 + clamp |
| R8 | **`repeat(N, 1fr)` 단독 (치명)** | **`repeat(N, minmax(0, 1fr))`** + `min-width:0; overflow:hidden` |
| R9 | **inline `style="font-size:clamp"` (치명)** | 클래스 경유만 |
| R10 | 히어로 `<br>` 강제 개행 | 자연 wrap + `keep-all` |
| R11 | clamp 하한 모바일 미역산 | 히어로 ≥40·섹션 ≥26 (375px 실측) |

상세: `→ responsive.md`.

## HTML 색상 금지 (C9 cascading)

- **회색 텍스트 전면 금지** (`#424245·#6e6e73·#666·#888·#86868b·#999·gray·slate-*`) — 라이트 모드에서 회색 추방. 위계는 weight·크기로만
- **흰글자는 검정 배경 위에서만** — 컬러 카드 배경(캔디/파스텔) 위에 흰글자 ✗. 항상 검정 글자
- inline `style="color:…"` — specificity 1000이 모드 분기 무력화
- `--muted` 단일 변수 — 위계 3단 붕괴
- **라이트 모드 카드 배경 = 캔디 A 5색** (`#FF4D8F·#FFCB05·#4DD964·#3DB3FF·#A855F7`) 외 파스텔 사용 시 칙칙·힘 빠짐 → FAIL
- **다크 모드 카드 배경 = 파스텔 5색** (`#a8e6cf·#d4b8ff·#ff6482·#64d2ff·#ffd60a`) 유지

### 카드/박스 안 텍스트 색상

| 배경 | 텍스트 | 비고 |
|---|---|---|
| 흰색·밝은그레이 | `#000` | 회색 ✗ |
| 캔디 A (라이트 카드) | `#000` | 흰글자 ✗ |
| 파스텔 (다크 카드) | `#000` | 흰글자 ✗ |
| 검정·다크네이비 | `#fff` | 예외 1 — 검정 배경에서만 |
| 형광펜 (배경 컬러) | `#000` | 흰글자 ✗ |

본문 안 컬러 텍스트(빨강·파랑 강조) = 그대로 유지. 회색만 금지.

## HTML 줄바꿈 금지 (C8 R12·R13·R14)

| 금지 | 이유 | 대체 |
|---|---|---|
| 본문 `text-wrap: pretty` 누락 | 마지막 줄 고아(orphan) 단어로 어색 | `.body·.box·p`에 `text-wrap: pretty` |
| 헤드라인 `text-wrap: balance` 누락 | 어색한 단일 단어 줄 발생 | 짧은 헤드라인(2~4줄)에 `text-wrap: balance` |
| 동사구·서술절 어절 끊김 | "데이터를 / 쌓는다.", "기회가 / 찾아오는" 어색 | `<span class="nowrap">동사구</span>` 또는 `white-space:nowrap` |
| `<br>` 강제 줄바꿈 (히어로·헤드라인) | 폭 바뀌면 깨짐 | 자연 wrap + R8·R12·R13 조합 |
| `line-height: 1.4` 이하 (한글 본문) | 한글 가독성 저하 | `line-height: 1.7` 권장 |

상세: `→ responsive.md §R12·R13·R14` · `→ snippets.md §한글 줄바꿈 자연화`.

## 접기/펴기 스크롤 보정 (A 방안 강제)

`<details class="fold">` 토글 시 viewport 점프 방지.

| 방안 | 평가 |
|---|---|
| **A. `scrollBy(delta)`** | ✅ 채택. viewport 중앙 가까운 요소 좌표 캡처 → 토글 후 차이만큼 보정 |
| B. `scroll-margin + :target` | ✗ 토글은 target 변경이 아님 |
| C. `IntersectionObserver` | ✗ 과한 오버헤드 |
| D. `overflow-anchor` 단독 | ✗ summary 토글에 불완전 |

A 외 방안 단독 사용 = FAIL. 상세: `→ snippets.md §접기/펴기 스크롤 보정`.

## Markdown (이쁘니) 금지

`→ protocol-pretty.md §금지` 전수.

핵심: 본문 중앙정렬(C5) · 3연속 동일 레이아웃(C7) · 제목 wght 본문과 <300 차이(C2) · 이모지 불릿.

## 옵시디언 .md 금지 (div 사용 시)

14금칙 전수 = `→ html-div-style/references/forbidden.md §옵시디언 14금칙`.

## PPTX 변환 금지

| 금지 | 대체 |
|---|---|
| 복잡 그라디언트 | 단색·2-stop |
| backdrop-filter·glassmorphism | 불투명 |
| flex 중첩 3단+ | 2단 이내 또는 table |
| clamp 폰트 | pt 고정 |
| CSS 애니메이션 | 정적 |

## PDF 변환 금지

| 금지 | 대체 |
|---|---|
| 뷰포트 단위 | mm/pt |
| 웹폰트 CDN 의존 | 임베딩 |
| dynamic content | 정적만 |

## 자동 QC 게이트

```bash
bash scripts/qc-mobile.sh output.html    # C8 R 계열 grep 검출
grep -n 'style="[^"]*color:' *.html       # = 0
grep -n 'style="[^"]*font-size:[^"]*clamp' *.html  # = 0
grep -E 'repeat\([0-9]+, *1fr\)' *.html   # = 0
```

상세 체크: `→ qc.md`.
