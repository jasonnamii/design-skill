# Format: HTML

**시각 전환 의무(C9):** 콘텐츠에 수치비교·시간축·프로세스·순환·2축분류·핵심수치·비율·퍼널 신호가 있으면 시각요소로 전환(표·문장만 ✗). 상세·템플릿 → `visualization-html.md`.

## 폰트

Pretendard Variable CDN: `https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable.min.css`

| 레벨 | size | wght | letter-spacing | line-height | color (light bg) | color (dark bg) |
|------|------|------|---------------|-------------|-----------------|----------------|
| L1 | clamp(48px, 6vw, 72px) | 800-900 | -2px | 1.1 | #1d1d1f | #f5f5f7 |
| L2 | clamp(28px, 4vw, 40px) | 600-700 | -1px | 1.2 | #1d1d1f | #f5f5f7 |
| L3 | clamp(18px, 2.5vw, 24px) | 400-500 | 0 | 1.4 | #1d1d1f | #ccc |
| L4 | clamp(14px, 1.5vw, 17px) | 400 | 0 | 1.7 | #6e6e73 | #86868b |
| XS | 12px | 400-600 | 0 | 1.4 | #86868b | #666 |

## 레이아웃

```css
section { padding: 80px 0; }  /* 최소. 히어로/클로징은 120px+ */
.content { max-width: 980px; margin: 0 auto; padding: 0 20px; }
```

그리드: CSS Grid, max 3col, gap 20px.
좌우분할: `grid-template-columns: 45% 55%` or `40% 60%`. 다음 섹션 미러.

## 배경 전환

기본 순서: `#fff` → `#f5f5f7` → `#fff` → `#000` → `#fff`
**톤 spoke가 다른 배경 순서를 지정하면 톤 우선** (SKILL.md 라우팅 "충돌 시 우선순위" 참조).
다크 section 내 모든 텍스트 color 재지정 필수.

## CTA

```html
<a href="#" style="color: var(--cta-color, #0066cc); text-decoration: none;">
  자세히 알아보기 <span style="font-size: 1.2em;">›</span>
</a>
```

필 버튼 (최종 전환점):
```html
<a href="#" style="background: var(--cta-color, #0066cc); color: #fff; padding: 12px 24px; border-radius: 980px; text-decoration: none; font-weight: 600;">
  시작하기
</a>
```

## 애니메이션 (선택)

IntersectionObserver fade-in: `opacity 0→1, translateY(30px→0), transition 0.6s ease`

## 이미지

`object-fit: cover`. 전폭: width 100%, border-radius 0. 카드형: border-radius 16px.
텍스트와 항상 영역 분리 (C6).

## 체크리스트

- [ ] Pretendard CDN import
- [ ] 배경색 교대 적용
- [ ] CTA 컬러 CSS 변수 사용
- [ ] 다크 섹션 텍스트 color 재지정
- [ ] max-width 980px 콘텐츠 영역

## HTML Speed Protocol — 코워크 운용 규칙

코워크에서 HTML 생성 속도를 최대화하는 5대 규칙. 기술 구현이 아닌 **요청·응답 왕복 최소화**가 목적.

| # | 규칙 | 이유 | 위반 시 |
|---|------|------|---------|
| SP1 | **단일 파일 강제** — HTML/CSS/JS 1파일. Tailwind CDN. npm install·빌드 도구 금지 | 파일 분리·설치 = 불필요 I/O 시간 | 분리 요청 없으면 항상 단일 |
| SP2 | **첫 턴 완성** — 구조·콘텐츠·스타일·인터랙션을 1회 응답으로 완성. 점진적 빌드업 금지 | 왕복이 가장 큰 시간 비용 | 미완성 출력 → 자체 완성 후 제출 |
| SP3 | **부분 수정 = Edit** — 완성 후 수정은 전체 재작성 ✗ → 해당 블록만 Edit(str_replace) | 토큰·시간 절약 | 전체 재작성은 형 명시 요청 시만 |
| SP4 | **디자인 스킬 선로딩** — HTML 생성 시 이 format-html.md + tone spoke를 첫 턴에 로드. "이쁘게 다시" = 2배 비용 | 사후 디자인 적용 = 전면 재작업 | 이미 SKILL.md §4 워크플로우에서 강제 |
| SP5 | **레퍼런스 첫 턴 투입** — 원하는 스타일(URL·스크린샷·키워드)을 첫 메시지에 포함 | 톤 맞추기 왕복 제거 | 레퍼런스 없으면 톤 자동추론 진행 |

**적용 시점:** 코워크 세션에서 HTML 산출물 생성 시 자동 적용. 코워크 외 환경에서는 참고용.
