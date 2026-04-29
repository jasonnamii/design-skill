# MODE 1: HTML 스크롤 (풀페이지)

| 항목 | 값 |
|------|-----|
| 배경 | `#000` |
| 폰트 | `Pretendard Variable` wght 300,400,600,700,950. CDN: jsdelivr pretendardvariable.min.css |
| 섹션 | `min-height: 100vh`, flex-center |
| 제목 | XL `clamp(64px, 8vw, 80px)` wght 950, `letter-spacing: -3px` |
| 서브제목 | L `clamp(36px, 5vw, 48px)` wght 700 |
| 본문 | M `clamp(22px, 3vw, 28px)` wght 300, color `#d1d1d6` (ccc 대비 상향) |
| 보조 | S `clamp(16px,1.6vw,18px)` wght 400, color `#b0b0b0` (캡션급 하한 16px) |
| 라벨 | XS `13px` wght 500, color `#8e8e93` (666 대비 상향) |
| 강조 | 동일 사이즈 + wght 600, color `#fff` |
| 플로우 | S mono계열, color `#666`, span내 `#fff` |
| 구분선 | `border-top: 1px solid #1a1a1a` |
| 애니메이션 | `IntersectionObserver` fade-in, `translateY(30px)` |
| 히어로 | 96-140pt, 센터, 하위 서브텍스트 `#888` |
| 클로징 | Before/After 대비 + 최종 문장 950 Black |

## 체크리스트

- [ ] HTML: Pretendard Variable CDN import 확인 (jsdelivr)
- [ ] IntersectionObserver 애니메이션 동작 확인
- [ ] clamp 반응형 사이즈 적용
- [ ] XS 13px 하한, S 16px 하한 (가독성 확보)
- [ ] 다크 배경 보조텍스트 `#b0b0b0` 이상 (`#888`·`#666` 금지)
