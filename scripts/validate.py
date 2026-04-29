#!/usr/bin/env python3
"""design-skill v3.0 self-check validator.

Invariant guards — 스킬 본질 수치가 변조되었는지 자가 점검.
v3.0 — 8조 헌법 + 4톤 + 페르소나 2종.
사용: python scripts/validate.py [skill_dir]
반환: errors 목록 (JSON). 빈 리스트 = PASS.
"""

import json
import os
import re
import sys
from pathlib import Path


HUB_SIZE_LIMIT = 16_384  # 16KB (v3.2 SELF_CHECK·INVARIANT 추가로 상향)
INVARIANTS = {
    "constitution_count": (8, r"^\|\s*H[1-8]\s*\|"),  # §HEADER 8조 헌법 H1~H8
    "core_count": (9, r"^\|\s*C[1-9]\s*\|"),           # §1 CORE C1~C9
    "guard_count": (8, r"^\|\s*G[1-8]\s*\|"),          # §3 GUARD G1~G8
}

REQUIRED_SPOKES = [
    "constitution.md",
    "color-system.md",
    "korean-typography.md",
    "fold-scroll.md",
    "tokens.md",
    "snippets.md",
    "forbidden.md",
    "qc.md",
    "format-html.md", "format-md.md", "format-pptx.md",
    "format-docx.md", "format-xlsx.md", "format-pdf.md",
    "special-features.md",
    # v3.0 4톤 + 믹스
    "tone-light-bento.md",
    "tone-dark-bento.md",
    "tone-light-scroll.md",
    "tone-dark-scroll.md",
    "tone-mix.md",
    # v3.0 페르소나 2종
    "persona-young-playful.md",
    "persona-kisas.md",
    # 공통
    "bento-patterns.md",
    "mode-html-bento.md",
    "mode-html-scroll.md",
    "layout-safety.md",
    "protocol-pretty.md",
    "engine-4layer.md",
    "ux-principles.md",
    "core-rules.md",
    "gotchas-extended.md",
    "responsive.md",
    "visualization-html.md",
    # v3.1 Apple Keynote DS 흡수
    "scaffold-scroll.html",
    "scaffold-bento.html",
    "scaffold-deck.md",
]


def count_matching_rows(text: str, pattern: str) -> int:
    return len(re.findall(pattern, text, re.MULTILINE))


def validate(skill_dir: str) -> dict:
    errors = []
    warnings = []
    skill_path = Path(skill_dir).resolve()
    hub = skill_path / "SKILL.md"

    if not hub.exists():
        errors.append(f"SKILL.md not found at {hub}")
        return {"errors": errors, "warnings": warnings}

    size = hub.stat().st_size
    if size > HUB_SIZE_LIMIT:
        errors.append(
            f"hub_size={size}B exceeds limit {HUB_SIZE_LIMIT}B "
            f"(overhead: {size - HUB_SIZE_LIMIT}B)"
        )

    text = hub.read_text(encoding="utf-8")

    for name, (expected, pattern) in INVARIANTS.items():
        actual = count_matching_rows(text, pattern)
        if actual != expected:
            errors.append(
                f"{name}: expected={expected}, actual={actual}"
            )

    refs_dir = skill_path / "references"
    if not refs_dir.exists():
        errors.append(f"references/ directory missing")
    else:
        for spoke in REQUIRED_SPOKES:
            if not (refs_dir / spoke).exists():
                errors.append(f"spoke missing: references/{spoke}")

    evals = skill_path / "evals" / "cases.json"
    if not evals.exists():
        warnings.append("evals/cases.json missing (recommended)")

    fm_match = re.search(r'^"@uses":\s*\n((?:\s*-.*\n)+)', text, re.MULTILINE)
    if fm_match:
        uses_block = fm_match.group(1)
        used_files = set(re.findall(r'-\s*references/([^\s]+)', uses_block))
        required_set = set(REQUIRED_SPOKES)
        missing_in_uses = required_set - used_files
        if missing_in_uses:
            warnings.append(
                f"frontmatter @uses missing: {sorted(missing_in_uses)}"
            )

    status = "PASS" if not errors else "FAIL"
    return {
        "skill": "design-skill",
        "hub_size_bytes": size,
        "hub_size_limit": HUB_SIZE_LIMIT,
        "errors": errors,
        "warnings": warnings,
        "status": status,
    }


if __name__ == "__main__":
    skill_dir = sys.argv[1] if len(sys.argv) > 1 else "."
    result = validate(skill_dir)
    print(json.dumps(result, indent=2, ensure_ascii=False))
    sys.exit(0 if not result.get("errors") else 1)
