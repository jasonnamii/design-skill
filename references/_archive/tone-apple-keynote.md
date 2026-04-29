# Tone: apple-keynote

Apple Keynote 발표 슬라이드 감성. iPhone·Mac·iPad·Apple Watch·iOS 페이지 패턴 흡수한 7번째 톤.

**소스 앵커:** Apple Keynote 발표 슬라이드 8장(iPhone 16e·15 Pro·iPadOS·iPhone 17·AirPods Pro·Apple Watch S9/S11·iOS).

**호출 어휘:** 애플벤토·apple-keynote·키노트벤또·키노트스타일·애플박스·애플벤또·애플벤토·벤또·벤토·bento·Think패턴·Oxford Blue·블랙화이트·반응형애플·텍스트벤또·마케팅벤또·분석벤또·KPI벤또·카드벤또.

---

## §0. 핵심 차별점 (3줄)

1. **벤또 그리드** — 비대칭 면적 + 텍스트多 셀 + 빅넘버 + 이미지 슬롯 + 포인트 컬러 조합 압축 시스템
2. **극단 weight 대비** — Black 950 (제목·빅넘버) + Light 300 (본문). 중간 weight 장식 전용
3. **블랙·화이트 + Oxford Blue 액센트** — 컬러 금지·1액센트 ≤20%·캔디 A/파스텔 카드 배경 5종

## §1. 톤 시그니처

| 항목 | 값 |
|---|---|
| 배경 주조 | 라이트(`#f5f5f7`·`#fff`) 80% / 다크(`#000`·`#1d1d1f`) 20% 또는 역전 |
| 액센트 | Oxford Blue `#002147` (1액센트, ≤20% 면적) |
| 카드 배경 | 라이트 = 캔디 A 5색 · 다크 = 파스텔 5색 (→ `color-system.md` §3) |
| 폰트 | Pretendard 전용 |
| L1 크기 | XL 80px (히어로) / L 48px (섹션) |
| L1 wght | **950 (Black)** |
| 본문 wght | 300 (Light) |
| 여백 | 데스크탑 80~120px / 모바일 20~32px |
| 라우팅 신호 | "애플벤또"·"키노트"·"Think"·"애플 디자인"·"마케팅 분석 한장 압축"·"KPI 대시보드"·"캠페인 복기" |

## §2. 톤 진입 시 발동 자산

| 자산 | 파일 | 역할 |
|---|---|---|
| 벤또 패턴북 | `→ bento-patterns.md` | 비대칭 그리드 5종 + 텍스트多 셀 8유형 + §A~F 6템플릿 |
| HTML 벤또 | `→ mode-html-bento.md` | 벤또 풀스펙·반응형 안전 |
| HTML 풀페이지 스크롤 | `→ mode-html-scroll.md` | Apple 스크롤 페이지 풀스펙 |
| 레이아웃 디버그 | `→ layout-safety.md` | HTML 레이아웃 11대 디버그 |
| 컬러 시스템 | `→ color-system.md` | 카드 배경 5색·페르소나 색·R1~R5 |
| 한글 타이포 | `→ korean-typography.md` | R8+R12+R13+R14 |
| 접기/펴기 | `→ fold-scroll.md` | A 방안 |

## §3. C3 예외 명시 (자가모순 해소)

`apple-keynote` 톤은 **C3 "유채색 1색" 룰을 오버라이드**:

| 톤 | 카드 배경 정책 |
|---|---|
| 기본 5톤 | CTA 1색. 카드 배경 컬러 ✗ |
| `young-playful` | 형광펜 5색 + 블록배경 5색 |
| **`apple-keynote`** | **캔디 A 5색 (라이트) 또는 파스텔 5색 (다크) 카드 배경 허용** |

오버라이드 범위: 카드 배경 컬러만. **본문 텍스트 컬러 다채색 ✗** (R3 강제).

## §4. 콘텐츠 유형 → 패턴 라우팅

| 콘텐츠 유형 | 추천 패턴 | bento-patterns 섹션 |
|---|---|---|
| 마케팅 분석 결과 | KPI 대시보드 + 인사이트 카드 | §A 마케팅 분석 |
| 캠페인 복기 | 빅넘버 + 학습포인트 + 이미지 | §B 캠페인 복기 |
| 기능·제품 요약 | 키노트 벤또 (이미지+라벨) | §C 기능 요약 |
| 주간·월간 리뷰 | 핵심지표 + 시그널 + 액션 | §D 주기 리뷰 |
| 매뉴얼·플레이북 | 텍스트多 카드 | §E 텍스트多 |
| 진단·전략 보고 | 분석 카드 + 결론 + 근거 | §F 보고서형 |

## §5. 텍스트 밀도 분기 (셀당 자수)

| 자수 | 분기 | 처리 |
|---|---|---|
| ≤80자 | 표준 벤또 | 헤드라인 1줄 + 짧은 캡션 |
| 81~240자 | 본문 카드형 | S 16px wght 400, line-height 1.7 |
| 240~400자 | 텍스트多 Type 1·4·7 | 헤드라인 + 본문 단락 |
| 401~700자 | 텍스트多 Type 1 + 부제 | 헤드라인 + 부제 + 본문 |
| 701자+ | **셀 분리 필수** | 1개 → 2~3개 카드로 쪼개기 |

상세: `→ bento-patterns.md §2 텍스트多 셀 8유형`.

## §6. Think 패턴 (히어로 블록)

```
Think [핵심단어].
→ 서술 1줄 (light, caption)
→ 강조 1줄 (Black, accent)
→ 플로우 (mono, dim)
→ 결론 1줄
```

```html
<div class="think dark">
  <h2 class="think-word">Think Output.</h2>
  <p class="caption">과정은 기록된다.</p>
  <p class="accent">결과가 말한다.</p>
  <p class="flow">계획 → 실행 → 검증 → 증거</p>
  <p class="conclude">그래서 만든다.</p>
</div>

<style>
.think { padding: clamp(40px, 8vw, 120px); border-radius: 24px; }
.think.dark { background: #1d1d1f; color: #fff; }
.think-word {
  font-size: clamp(48px, 8vw, 80px);
  font-weight: 950;
  letter-spacing: -0.02em;
  line-height: 1.05;
  margin-bottom: 16px;
}
.think .caption { font-weight: 300; opacity: 0.7; }
.think .accent { font-weight: 900; font-size: clamp(20px, 2.5vw, 28px); }
.think .flow { font-family: monospace; opacity: 0.5; letter-spacing: 0.05em; }
.think .conclude { font-weight: 300; margin-top: 24px; }
</style>
```

**적용:** 히어로 섹션·매니페스토·강력한 결론. 1문서 1회 권장.

## §7. 워크플로우

```
1. 콘텐츠 수신 → 콘텐츠 유형 판정 (§4)
2. 텍스트 밀도 측정 (§5)
3. 패턴 선택 (bento-patterns §A~F + 비대칭 그리드 1~5)
4. 텍스트多 셀 Type 1~8 매핑
5. Think 패턴 여부 판단
6. 색 결정 — Oxford Blue + 카드 배경 캔디/파스텔 (§3)
7. HTML 벤또 또는 스크롤 모드 선택 (§2)
8. 한글 줄바꿈 (`→ korean-typography.md`)
9. 레이아웃 11대 (`→ layout-safety.md`)
10. 6계층 스코어카드 (`→ qc.md`)
```

## §8. 4층 엔진 매핑

| Layer | 이 톤 |
|---|---|
| L1 톤 | apple-keynote |
| L2 섹션 | 히어로(Think)·기능(벤또)·증거(빅넘버)·비교(2분할)·CTA·클로징 |
| L3 블록 | 벤또 패턴 A~E (비대칭 그리드 5종) |
| L4 요소 | 빅넘버·라벨 셀·이미지 슬롯·텍스트多 Type 1~8 |

## §9. 핵심 제약

| 원인 | 금칙 | 처방 |
|---|---|---|
| 컬러 다채색 | 블랙·화이트·Oxford Blue 외 컬러 본문 ✗ | R3 강제 |
| 카드 흰글자 | 캔디·파스텔 위 흰글자 ✗ | 항상 검정 |
| 4×N 균등 그리드 | Apple 벤또 = 비대칭 | `grid-template-areas` |
| 텍스트多 line-height < 1.65 | 가독성 저하 | 1.65 강제 |
| 텍스트多 padding 부족 | 답답 | `clamp(28px, 4vw, 40px)` |
| 히어로 `<br>` 강제 개행 | 모바일 깨짐 | 자연 wrap |
| 1문서 다중 액센트 | 위계 붕괴 | 1액센트 ≤20% |

## §10. Gotchas

| 함정 | 대응 |
|---|---|
| 벤또를 4×N 균등 강제 | `grid-template-areas` + `span N` |
| 텍스트多에 XS·muted | 본문 S 16·wght 400·`var(--label-info)` |
| 캔디 A를 다크에 | 시끄러움. 다크는 파스텔 |
| 파스텔을 라이트에 | 칙칙. 라이트는 캔디 A |
| Think 다회 사용 | 1문서 1회. 다회 시 효과 소멸 |
| 카드 제목 wght < 900 | 무조건 가장 굵게 |
| Oxford Blue >20% | 액센트 의미 소실 |
| 명시 span 리셋 누락 | @media 1024·640 전수 리셋 |
| PPTX 변환 시 복잡 효과 | 단색·2-stop·flex 2단·정적 |
