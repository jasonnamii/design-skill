# Gotchas Extended — 포맷·프로토콜별 세부 함정

허브(SKILL.md Gotchas)의 확장. 포맷·스포크별 세부 함정을 모아둠. 핵심 5개는 허브에 유지.

---

## 포맷별 함정

- **md에서 타이포 비율 한계:** md는 H1/H2/H3 렌더링 크기를 제어 못함(뷰어 의존). C1은 "위계 4단계 유지"로만 번역.
- **XLSX 여백:** C4를 XLSX에 적용하면 데이터가 너무 적어진다. 행높이 ×1.2, 열너비 ×1.3으로 번역.
- **spoke 간 배경색 충돌:** format spoke의 기본 배경 순서와 tone spoke가 다를 수 있다. 라우팅의 "충돌 시 우선순위" (tone > format)를 따른다.

---

## 프로토콜별 함정

- **이쁘니 직접수행 금지:** "마크다운 정리 정도는 직접 하면 된다"고 판단하는 패턴. 이쁘니는 L1~L5 강약매핑+볼드 과용 체크+diff QC를 포함하는 5단계 프로토콜. `protocol-pretty.md` 로드 없이 직접 수행 = FAIL.
- **md 콜아웃과 format-md 충돌:** `format-md.md`의 타이포/여백 규칙은 CORE를 md로 번역한 것. 콜아웃 체계는 `protocol-pretty.md`가 SSOT — `format-md.md`가 아님.
- **AXIOM_UX_MAPPING 미참조:** CORE 위반 수정 후 대응 UX 원리 미점검 → 같은 원인 재발. `references/ux-principles.md#G_AXIOM_MAPPING` 표로 1회 교차검증.
