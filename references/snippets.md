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
  --label-info:    #1d1d1f;
  --label-caption: #424245;
  --label-deco:    #86868b;
}

.dark, .key, .hot, [style*="background:#002147"] {
  --label-info:    #fff;
  --label-caption: #d1d1d6;
  --label-deco:    #86868b;
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
