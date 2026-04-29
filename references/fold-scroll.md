# fold-scroll.md — 접기/펴기 스크롤 보정 SSOT

`<details class="fold">` 토글 시 viewport 점프 방지. **A 방안(`scrollBy(delta)`) 채택**.

## 0. 4안 비교

| 방안 | 평가 |
|---|---|
| **A. `scrollBy(delta)`** | **✅ 채택** |
| B. `scroll-margin + :target` | ✗ 토글은 target 변경이 아님 |
| C. `IntersectionObserver` | ✗ 과한 오버헤드 |
| D. `overflow-anchor` 단독 | ✗ summary 토글에 불완전 |

**A 외 단독 사용 = FAIL.** D는 A와 병행 보조용.

## 1. A 구현 (verbatim)

```html
<details class="fold">
  <summary>접기/펴기 제목</summary>
  <div class="fold-body">...</div>
</details>

<script>
(function () {
  document.querySelectorAll('details.fold > summary').forEach(function (sum) {
    sum.addEventListener('click', function () {
      var midY = window.innerHeight / 2;
      var anchors = document.querySelectorAll('details, summary, section');
      var anchor = null, minDist = Infinity;
      anchors.forEach(function (el) {
        var r = el.getBoundingClientRect();
        var dist = Math.abs((r.top + r.height / 2) - midY);
        if (dist < minDist) { minDist = dist; anchor = el; }
      });
      if (!anchor) return;
      var beforeTop = anchor.getBoundingClientRect().top;
      requestAnimationFrame(function () {
        requestAnimationFrame(function () {
          var afterTop = anchor.getBoundingClientRect().top;
          var delta = afterTop - beforeTop;
          if (Math.abs(delta) > 1) window.scrollBy(0, delta);
        });
      });
    });
  });
})();
</script>

<style>
details.fold { overflow-anchor: auto; }
</style>
```

## 2. 동작 원리

1. 사용자가 클릭한 details 자체가 아니라 **viewport 중앙 가까운 요소** 기준으로 보정 (시선 유지)
2. `requestAnimationFrame` 2회 후 측정 → 토글 reflow 완료 보장
3. delta 1px 이하 = 무시 (jitter 방지)

## 3. 적용 범위

- 모든 `<details class="fold">` 토글에 자동 적용
- 비-`.fold` details는 보정 안 함
- 단일 페이지 `<details>` 다수일 때 효과적

## Gotchas

| 함정 | 대응 |
|---|---|
| `scrollBy(0, 0)` 무의미 호출 | delta 1px 이하 무시 |
| 토글 reflow 미완료 시 측정 | rAF 2회 후 측정 |
| 클릭한 details 자체를 앵커로 | viewport 중앙 가까운 요소 우선 |
| B·C·D 단독 사용 | FAIL. A 필수 |
| iframe 내부 details | iframe 별도 스크립트 주입 |
