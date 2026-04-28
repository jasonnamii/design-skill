# tokens.md — design-skill 공통 토큰 (4블록 인덱스)

허브형. 6포맷×6톤 전부 대응하는 공통 토큰 **인덱스**. 풀스펙은 기존 스포크에 유지.

> 공통 스파인: `VAULT/_skills research/html-skill-refactor/spine.md §공통 토큰`
> 축1 디테일: `VAULT/_skills research/html-skill-refactor/axis1-css-tokens.md`

---

## 타이포 — CORE §C1 비율

| Layer | 비율 | 근거 |
|---|---|---|
| L1 | 4 | 제목 |
| L2 | 2.3 | 섹션 |
| L3 | 1.5 | 본문 강조 |
| L4 | 1 | 본문 |

허용 ±10%. 위반=FAIL. 상세: `→ core-rules.md` §L1~L4 px값.

**weight 대비 C2:** 제목wght − 본문wght ≥ 600 (기본: Black 900 ↔ Light 300). 카드/박스 제목은 무조건 wght 900.

**HTML clamp 기본값:** `→ responsive.md §clamp 스케일`.

## 색 — CORE §C3 3색 시스템

| 역할 | 기본 | 대체(등록) |
|---|---|---|
| 배경 | 흰 / 검 / 밝은그레이 | — |
| CTA | `#0066cc` | Oxford Blue `#002147` |
| 그래디언트 | 요청 시만 | G8 1회 한정 |

유채색 2개+ = FAIL. young-playful 톤은 팔레트 예외(`→ tone-young-playful.md`).

**다크 컨테이너 매핑** (apple-box-design 공유):

| Tier | 라이트 | 다크 |
|---|---|---|
| 1 정보 | `#000` | `#fff` (검정 배경 예외) |
| 2 캡션 | `#000` (회색 추방) | `#fff` (검정 배경 예외) |
| 3 장식 | `#000` (회색 추방) | `#fff` (검정 배경 예외) |

**원칙:** 라이트 배경=항상 검정. 흰글자=검정 배경에서만 예외. 회색·중간 회색 글자 전면 금지. 위계는 weight·크기로만 만든다 (wght 900 ↔ 300 대비).



## 컬러풀 카드 팔레트 (배경 모드별 분기)

**원칙:** 라이트 배경에서 파스텔은 칙칙하다. 캔디로 강하게. 다크 배경에서 캔디는 시끄럽다. 파스텔로 부드럽게.

### 라이트 모드 (흰 배경) — 캔디 A (강한 캔디)

| 이름 | HEX | 용도 |
|---|---|---|
| Pink | `#FF4D8F` | 카드 배경·강조 |
| Yellow | `#FFCB05` | 카드 배경·하이라이트 |
| Lime | `#4DD964` | 카드 배경·성공 |
| Cyan | `#3DB3FF` | 카드 배경·정보 |
| Violet | `#A855F7` | 카드 배경·신규 |

**규칙:** 카드/박스 배경에 컬러 사용 시 위 5색 중 선택. 카드 안 텍스트는 항상 `#000` (검정). 흰글자 ✗.

### 다크 모드 (검정 배경) — 파스텔 (현재 유지)

| 이름 | HEX | 용도 |
|---|---|---|
| Mint Green | `#a8e6cf` | 카드 배경·성공 |
| Soft Purple | `#d4b8ff` | 카드 배경·신규 |
| Vivid Pink | `#ff6482` | 카드 배경·주목 |
| Sky Blue | `#64d2ff` | 카드 배경·정보 |
| Warm Yellow | `#ffd60a` | 카드 배경·CTA |

**규칙:** 검정 배경 위 카드. 카드 안 텍스트는 `#000` (검정). 검정 배경 자체 위에 직접 글자=흰글자 예외 OK.

### 컬러 본문 텍스트 (강조용)

본문 안에 빨강·파랑·초록 강조 텍스트 = 그대로 유지. 회색만 금지.

### 형광펜 하이라이트

배경에 형광펜 컬러 + 텍스트 검정. 흰글자 ✗.

## 간격·radius

| 용도 | 값 |
|---|---|
| 카드 padding 데스크탑 | 40 / 64 / 80 / 120 |
| 카드 padding 모바일 | 20 / 24 / 32 |
| gap | 16 / 24 / 32 / 48 |
| radius | 0 / 4 / 8 / 12 / 16 / 24 |

## 브레이크포인트 — CORE §C8

| 단계 | 범위 |
|---|---|
| 모바일 | ≤640px |
| 태블릿 | 641~1024px |
| 데스크탑 | ≥1025px |

터치 타겟 ≥44×44px. 상세: `→ responsive.md`.

## 포맷별 토큰 매핑

| 역할 | HTML | MD | PPTX | DOCX | XLSX | PDF |
|---|---|---|---|---|---|---|
| 타이포 비율 | clamp | 기본폰트 | pt 고정 | pt 고정 | pt | pt |
| 색 | CSS var | 기본 | theme | theme | theme | rgb 0-1 |
| 여백 | clamp | 빈줄 | slide mask | margin | row/col | margin |

풀 매핑: `→ format-{html·md·pptx·docx·xlsx·pdf}.md`.

## 금지 토큰

| 토큰 | 이유 |
|---|---|
| `position: fixed` | 전 포맷 불안정 |
| 고정 px 히어로 | C8 모바일 붕괴 |
| `repeat(N, 1fr)` 단독 | grid item 오버플로우 |
| inline `style="color:…"` | 다크 역매핑 무력화 |
| 유채색 2+ | C3 위반 |

상세: `→ forbidden.md`.
