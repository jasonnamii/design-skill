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

**weight 대비 C2:** 제목wght − 본문wght ≥ 300 (예: 950 + 300).

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
| 1 정보 | `#1d1d1f` | `#fff` |
| 2 캡션 | `#424245` | `#d1d1d6` |
| 3 장식 | `#86868b` | `#86868b` |

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
