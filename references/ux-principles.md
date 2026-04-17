# UX Principles — 공통 허브

5개 UX 스킬(ui-action-designer·app-architect·design-skill·copywriting-engine·html-div-style)이 참조하는 단일 허브. **풀텍스트는 여기에만**, 스포크는 `@ref: _shared/ux-principles.md#N` 포인터만 유지.

---

## §A. Nielsen 10 Heuristics (1994, 업데이트 유지)

| # | 코드 | 원칙 | 1줄 정의 | 스킬 검사 포인트 |
|---|------|------|---------|----------------|
| N1 | VISIBILITY | 시스템 상태 가시화 | 사용자는 항상 시스템이 뭘 하는지 알아야 한다 | 로딩·진행률·피드백 UI |
| N2 | MATCH_REAL | 실세계 매칭 | 시스템 용어가 아닌 사용자 언어·은유 | 카피·아이콘·메타포 |
| N3 | CONTROL | 사용자 제어·자유 | 되돌리기·취소·탈출구 필수 | Cancel·Undo·Exit |
| N4 | CONSISTENCY | 일관성·표준 | 같은 것은 같게, 플랫폼 표준 준수 | 토큰·패턴·용어 일관 |
| N5 | ERR_PREV | 오류 예방 | 오류를 내기 전에 막는다 (확인·제약·기본값) | 확인 다이얼로그·입력 제약 |
| N6 | RECOGNITION | 재인 > 회상 | 기억하게 하지 말고 보여줘라 | 메뉴·힌트·최근사용 |
| N7 | FLEXIBILITY | 유연성·효율 | 초보·전문가 동시지원(단축키·커스텀) | 숏컷·가속기 |
| N8 | MINIMAL | 미니멀 미학 | 불필요 정보는 주 정보의 가시성 약화 | 3색·여백·계층 |
| N9 | ERR_REC | 오류 회복 | 오류 발생시 진단·해법을 명확히 | 에러 메시지 3요소(원인·영향·해법) |
| N10 | HELP | 도움말 | 필요할 때 즉시 닿을 수 있게 | 툴팁·FAQ·온보딩 |

---

## §B. Norman 5 Elements (Design of Everyday Things)

| # | 코드 | 요소 | 정의 | 적용 |
|---|------|------|------|------|
| D1 | AFFORDANCE | 행동 가능성 | 이 요소로 뭘 할 수 있는지 시사 | 버튼은 눌러보이게·링크는 밑줄 |
| D2 | SIGNIFIER | 신호·표식 | 어디서·언제·어떻게 할지 명시 | 아이콘·라벨·위치 |
| D3 | FEEDBACK | 피드백 | 행동 직후 결과를 알린다 | 클릭 → 상태변화·토스트·애니 |
| D4 | MAPPING | 매핑 | 컨트롤과 결과의 공간적·논리적 대응 | 볼륨슬라이더=위아래·좌우 |
| D5 | CONSTRAINTS | 제약 | 잘못할 수 없게 막는다 | 비활성화·필수입력·범위제한 |

---

## §C. 스킬별 적용 가이드 (어느 원리를 어디에)

| 스킬 | 적용 원리(코어) | 적용 시점 | 검사 도구 |
|------|---------------|----------|----------|
| ui-action-designer | N1~N10 전체 + D1~D5 | SHE 필터 직후 `UX_GATE` | 10+5 체크리스트 |
| app-architect | N2·N4·N6 + D1·D3 | 와이어프레임 산출 직전 | 5원칙 체크 |
| design-skill | N4·N6·N8 (공리 X1·X2 매핑) | CORE 7 검증 시 병행 | CORE-UX 매핑표 |
| copywriting-engine | N2·N5·N9·N10 | 카피 생산 후 QC | 4원칙 마이크로카피 체크 |
| html-div-style | N4·N6·N8 | 14규칙 검증 시 주석 | 3원칙 연결 주석 |

---

## §D. 충돌 해결 (스킬 연합 시)

**원칙:** 허브는 **참조용 풀텍스트**. 스포크 로직을 덮어쓰지 않는다.

| 충돌 유형 | 해소 |
|----------|------|
| ui-action-designer + design-skill 동시호출 | 허브 1회만 로드. 중복 해석 금지 |
| UX 원리 ↔ 기존 스킬 프로토콜 | **기존 프로토콜 우선** + UX 원리를 보조 검증 레이어로만 |
| UX 원리끼리 충돌 (예: N7 유연성 ↔ N8 미니멀) | 사용 맥락에서 승부 — 초보 UX=N8 우선, 전문가 UX=N7 우선 |
| UP의 M7.SKILL_PRECEDENCE | UP SAFE_RULES 절대 우선. 허브는 하위 |

---

## §E. 스포크 참조 포맷 (표준)

각 스킬 SKILL.md에서 허브를 참조할 때 다음 포맷 사용:

```
@ref: _shared/ux-principles.md#{섹션}
```

예:
- `@ref: _shared/ux-principles.md#A` (Nielsen 10 전체)
- `@ref: _shared/ux-principles.md#A-N5` (N5 ERR_PREV만)
- `@ref: _shared/ux-principles.md#B-D1` (D1 AFFORDANCE만)
- `@ref: _shared/ux-principles.md#C` (스킬별 가이드)

**로딩 규칙:** 스포크는 필요한 섹션만 참조. 전체 로드는 연합 검증 시(2스킬+ 동시)에만 1회.

---

## §F. 빠른 체크리스트 (30초 QC)

산출물 완료 직전 자문:

1. **N1 상태 가시화** — 지금 뭐가 일어나는지 보이는가?
2. **N2 실세계 매칭** — 사용자 언어로 말하는가?
3. **N3 탈출구** — 되돌릴 수 있는가?
4. **N5 오류 예방** — 실수 전에 막는가?
5. **N6 재인** — 외우지 않고 알아볼 수 있는가?
6. **N8 미니멀** — 필수만 남겼는가?
7. **N9 오류 회복** — 실수 후 회복 경로가 있는가?
8. **D1 어포던스** — 뭘 할 수 있는지 보이는가?
9. **D3 피드백** — 행동 후 응답이 있는가?
10. **D5 제약** — 잘못할 수 없게 막았는가?

7개+ PASS → 합격. 5개 이하 → 재설계.

---

## §G. AXIOM_UX_MAPPING — design-skill 공리 ↔ UX 원리 매핑

design-skill의 §0 공리(X1~X4)와 이 허브의 Nielsen 10·Norman 5 간 매핑. design-skill 발동 시 CORE 위반 판정과 함께 UX 원리 점검에 사용.

공리는 디자인 판단의 **내부 근거**, UX 원리는 **사용자 경험 검증**. 서로 보강 관계 — 충돌시 공리 우선(스킬 본질).

| 공리 | 연결 UX 원리 | 해석 | CORE 연결 |
|------|-------------|------|----------|
| X1 인지 유한성 | N8 MINIMAL · N6 RECOGNITION | 인지부하↓ = 미니멀+재인 | C3·C4·C6 |
| X2 위계 효율 | N4 CONSISTENCY · D4 MAPPING | 위계=일관 대응의 시각화 | C1·C2·C5 |
| X3 리듬 원리 | N4 CONSISTENCY · D3 FEEDBACK | 반복=예측(일관), 변화=피드백 | C5·C7 |
| X4 여백 증폭 | N8 MINIMAL | 여백이 주 정보 가시성 증폭 | C4 |

**사용법:** design-skill §4 워크플로우 step 7(QC)에서 CORE 위반 판정 후 UX 원리도 함께 점검 — 예: C4 여백 위반 = 동시에 N8 MINIMAL 위반. 수정시 두 관점 모두 해소.

**충돌:** UX 원리가 CORE 수치와 충돌(예: N7 FLEXIBILITY ↔ C3 3색 제한) → **CORE 우선**(스킬 정체성). UX 원리는 CORE 내에서만 조정 근거로 쓴다.

---

## Version

v1.1 — 2026-04-17 — §G AXIOM_UX_MAPPING 통합 (design-skill P0-② 처방)
v1.0 — 2026-04-16 — 초기 허브 생성 (5개 UX 스킬 공통 참조)
