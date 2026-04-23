#!/usr/bin/env bash
# qc-mobile.sh — HTML 산출물 모바일 반응형 QC 정적 프리플라이트
# 용법: bash qc-mobile.sh <path/to/output.html>
# 목적: 헤드리스 렌더 없이 grep 기반 정적 검사로 R4b·R8·R9·R10·R11 위반 선검출
# 헤드리스 실행 QC는 별도(추후 playwright-based) — 이 스크립트는 LLM 산출 직후 1차 게이트

set -e

FILE="${1:-}"
if [ -z "$FILE" ] || [ ! -f "$FILE" ]; then
  echo "ERROR: HTML 파일 경로 필요"
  echo "용법: bash qc-mobile.sh <path/to/output.html>"
  exit 1
fi

echo "=== Mobile QC: $FILE ==="
FAIL=0

# R2: viewport 메타
if ! grep -qE 'name="viewport"' "$FILE"; then
  echo "❌ R2: viewport 메타 누락"
  FAIL=$((FAIL+1))
else
  echo "✓ R2: viewport 메타"
fi

# R4b: repeat(N, 1fr) 단독 사용 (minmax 없이)
HITS=$(grep -cE "repeat\([0-9]+, *1fr\)" "$FILE" 2>/dev/null | head -1 || echo "0")
HITS=${HITS:-0}
if [ "$HITS" -gt 0 ] 2>/dev/null; then
  echo "❌ R4b: repeat(N, 1fr) 단독 $HITS건 — minmax(0, 1fr)로 교체 필요"
  grep -nE "repeat\([0-9]+, *1fr\)" "$FILE" | head -5
  FAIL=$((FAIL+1))
else
  echo "✓ R4b: grid minmax(0, 1fr) 사용 또는 해당 없음"
fi

# R8: 한글 콘텐츠 + word-break:keep-all 여부
if LC_ALL=C grep -qE "[$(printf '\xea-\xed')]" "$FILE" 2>/dev/null; then
  if ! grep -qE "word-break: *keep-all" "$FILE"; then
    echo "❌ R8: 한글 콘텐츠 있으나 word-break:keep-all 미설정"
    FAIL=$((FAIL+1))
  else
    echo "✓ R8: word-break:keep-all"
  fi
fi

# R9: <br> 강제 줄바꿈 히어로·헤드라인 검출 (h1·h2·.spine·.closing-q 내부)
BR_HITS=$(grep -cE "<(h1|h2)[^>]*>[^<]*<br" "$FILE" 2>/dev/null || echo 0)
if [ "$BR_HITS" -gt 0 ]; then
  echo "⚠ R9: h1·h2 내부 <br> $BR_HITS건 — 자연 wrap 권장"
  grep -nE "<(h1|h2)[^>]*>[^<]*<br" "$FILE" | head -3
fi

# R10: 인라인 style에 font-size:clamp(
INLINE_CLAMP=$(grep -cE 'style="[^"]*font-size:[^"]*clamp' "$FILE" 2>/dev/null || echo 0)
if [ "$INLINE_CLAMP" -gt 0 ]; then
  echo "❌ R10: 인라인 font-size:clamp $INLINE_CLAMP건 — 미디어쿼리 덮어쓰기 불가"
  grep -nE 'style="[^"]*font-size:[^"]*clamp' "$FILE" | head -3
  FAIL=$((FAIL+1))
else
  echo "✓ R10: 인라인 clamp 없음"
fi

# R11: .box·.card 선언에 min-width:0 권장 (박스형 레이아웃 감지)
if grep -qE "\.(box|card|cell|tile)" "$FILE"; then
  if ! grep -qE "min-width: *0" "$FILE"; then
    echo "⚠ R11: 박스형 레이아웃 있으나 min-width:0 없음 — 오버플로우 위험"
  else
    echo "✓ R11: min-width:0 선언"
  fi
fi

# clamp 하한 모바일 역산 (히어로 추정 — 상한 64px+ 이고 하한 <40px 검출)
WEAK_HERO=$(grep -oE "clamp\([0-9]+px, *[0-9.]+vw, *(6[4-9]|[7-9][0-9]|1[0-9][0-9])px\)" "$FILE" | grep -E "clamp\((1[0-9]|2[0-9]|3[0-9])px," 2>/dev/null | wc -l | tr -d ' ')
if [ "$WEAK_HERO" -gt 0 ]; then
  echo "⚠ R1a: 히어로 추정 clamp 하한 <40px $WEAK_HERO건 — 모바일 존재감 약함"
  grep -nE "clamp\([0-9]+px, *[0-9.]+vw, *(6[4-9]|[7-9][0-9]|1[0-9][0-9])px\)" "$FILE" | grep -E "clamp\((1[0-9]|2[0-9]|3[0-9])px," | head -3
fi

echo ""
if [ "$FAIL" -eq 0 ]; then
  echo "✅ PASS (FAIL: 0)"
  exit 0
else
  echo "❌ FAIL ($FAIL개) — 수정 후 재실행"
  exit 1
fi
