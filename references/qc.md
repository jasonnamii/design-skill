# qc.md — design-skill 품질 체크 (4블록 인덱스)

허브형 QC. CORE 9 + GUARD 8 + 6계층 스코어카드 + 포맷별 체크.
합격선 ≥80 AND Layer 1-4 ≥85% (+ CORE 전수 PASS 필수).

> 공통 QC: `VAULT/_skills research/html-skill-refactor/spine.md §공통 QC`
> 축5 상세: `VAULT/_skills research/html-skill-refactor/axis5-qc-checklist.md`

---

## 6계층 스코어카드

| Layer | 항목 | 배점 | 자동화 |
|---|---|---|---|
| 1 Syntax | HTML·MD·문서 객체 유효성 | 8 | 100% |
| 2 A11y | 대비·구조·시맨틱·터치 | 20 | 70% |
| 3 Perf | 경량·리소스·clamp | 20 | 100% |
| 4 Semantic | 태그·역할 정합 | 15 | 50% |
| 5 Design | CORE+GUARD+톤 일관 | 25 | 40% |
| 6 Brand | 3색·타이포·톤 fidelity | 12 | 10% |

---

## CORE 9 전수 (하나라도 FAIL = 산출 중단)

- [ ] C1 타이포 비율 4:2.3:1.5:1 ±10%
- [ ] C2 weight 차이 ≥300
- [ ] C3 유채색 1색 (young-playful 예외)
- [ ] C4 여백 ≤55%
- [ ] C5 본문 좌정렬 (md 면제)
- [ ] C6 이미지-텍스트 분리
- [ ] C7 레이아웃 3연속 동일 없음
- [ ] C8 반응형 (HTML·웹MD) — R1~R11 전수
- [ ] C9 HTML 시각소스→시각요소 전환

## GUARD 8

- [ ] G1 이미지 비율 ≤3종
- [ ] G2 CTA 섹션당 ≤2
- [ ] G3 인용 ≥L2
- [ ] G4 테이블 ≤6열
- [ ] G5 폰트 단계 ≤4
- [ ] G6 S7 감성선언 ≤2
- [ ] G7 S9 형광펜 블록당 ≤2
- [ ] G8 S14 그래디언트 ≤1

---

## HTML 전용

### 반응형 (C8 R1~R11)

- [ ] viewport 메타
- [ ] clamp 반응형 (고정 px 금지)
- [ ] 모바일 ≤640px 1열
- [ ] 터치 타겟 ≥44px
- [ ] 5폭 실측(360·390·480·640·768·1024) 횡스크롤 0
- [ ] R1 암시적 span 리셋
- [ ] R1a mobile-first 선설계
- [ ] R4a 한글 `keep-all; overflow-wrap: break-word`
- [ ] R8 `repeat(N, minmax(0, 1fr))` 사용
- [ ] R9 인라인 `font-size:clamp` 0건
- [ ] R10 히어로 `<br>` 0건
- [ ] R11 히어로 ≥40px·섹션 ≥26px (375px 실측)

### 시각 전환 (C9)

- [ ] 수치 비교 → 차트/빅넘버
- [ ] 프로세스 → 플로우
- [ ] 시간축 → 타임라인
- [ ] 관계 → 다이어그램
- [ ] 2축 → 매트릭스

### HTML 색상

- [ ] inline `style="color:"` 0건
- [ ] 다크 배경 4색만 (`#fff·#d1d1d6·#86868b·#3a3a3c`)
- [ ] CSS 변수 3분리 (`--label-info·-caption·-deco`)

### 자동 QC 게이트

```bash
bash scripts/qc-mobile.sh output.html
grep -n 'style="[^"]*color:' *.html
grep -n 'style="[^"]*font-size:[^"]*clamp' *.html
grep -E 'repeat\([0-9]+, *1fr\)' *.html
```

## Markdown (이쁘니)

- [ ] 헤딩 위계
- [ ] 콜아웃 문맥 맞춤
- [ ] 테이블 ≤6열
- [ ] 수평선 리듬
- [ ] 볼드·이탤릭 과용 없음

상세: `→ protocol-pretty.md §QC ①~⑧`.

## PPTX

- [ ] 마스터 슬라이드 사용
- [ ] 폰트 pt 고정
- [ ] 복잡 그라디언트·애니메이션 없음
- [ ] 변환 후 캡처 대조

## DOCX / XLSX / PDF

- [ ] DOCX: heading 위계·기본 여백·테마
- [ ] XLSX: 행 높이 1.2·열 너비 1.3 여백(C4 조정)
- [ ] PDF: 임베딩 폰트·정적 콘텐츠

---

## 합격 판정

- CORE 9 전수 PASS **AND** GUARD FAIL 없음 (G2·G5·G8은 FAIL 등급)
- Total ≥80 AND Layer 1~4 ≥85%
- HTML: 자동 QC 게이트 통과 + 5폭 실측 0

## 불합격 처방

| 실패 | 포인터 |
|---|---|
| CORE C8 반응형 | → forbidden §HTML 반응형 11대 · responsive.md |
| CORE C9 시각 전환 | → visualization-html.md |
| CORE C1/C2 타이포 | → core-rules.md |
| CORE C3 색 | → tokens.md §색 · tone-*.md 팔레트 |
| Markdown QC | → protocol-pretty.md |
| PPTX 변환 | → forbidden §PPTX 변환 금지 · format-pptx.md |
