#!/usr/bin/env python3
"""design-skill self-check validator.

Invariant guards — 스킬 본질 수치가 변조되었는지 자가 점검.
사용: python scripts/validate.py [skill_dir]
반환: errors 목록 (JSON). 빈 리스트 = PASS.
"""

import json
import os
import re
import sys
from pathlib import Path


HUB_SIZE_LIMIT = 10_240  # 10KB
INVARIANTS = {
    "axiom_count": (4, r"^\|\s*X[1-4]\s*\|"),      # §0 공리 X1~X4
    "core_count": (7, r"^\|\s*C[1-7]\s*\|"),        # §1 CORE C1~C7
    "guard_count": (8, r"^\|\s*G[1-8]\s*\|"),       # §3 GUARD G1~G8
}

REQUIRED_SPOKES = [
    "format-html.md", "format-md.md", "format-pptx.md",
    "format-docx.md", "format-xlsx.md", "format-pdf.md",
    "special-features.md",
    "tone-dark-cinema.md", "tone-warm-human.md", "tone-clean-info.md",
    "tone-pro-grid.md", "tone-story-dark.md",
    "protocol-pretty.md",
    "engine-4layer.md",
    "ux-principles.md",
    "core-rules.md",
    "gotchas-extended.md",
]


def count_matching_rows(text: str, pattern: str) -> int:
    """Count lines matching a regex pattern (multiline)."""
    return len(re.findall(pattern, text, re.MULTILINE))


def validate(skill_dir: str) -> dict:
    errors = []
    warnings = []
    skill_path = Path(skill_dir).resolve()
    hub = skill_path / "SKILL.md"

    # 1. Hub existence + size
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

    # 2. Invariant counts (axiom·CORE·GUARD rows)
    for name, (expected, pattern) in INVARIANTS.items():
        actual = count_matching_rows(text, pattern)
        if actual != expected:
            errors.append(
                f"{name}: expected={expected}, actual={actual}"
            )

    # 3. Required spokes resolvable
    refs_dir = skill_path / "references"
    if not refs_dir.exists():
        errors.append(f"references/ directory missing")
    else:
        for spoke in REQUIRED_SPOKES:
            if not (refs_dir / spoke).exists():
                errors.append(f"spoke missing: references/{spoke}")

    # 4. evals/ presence (recommended)
    evals = skill_path / "evals" / "cases.json"
    if not evals.exists():
        warnings.append("evals/cases.json missing (regression baseline)")
    else:
        try:
            cases = json.loads(evals.read_text())
            if len(cases.get("cases", [])) < 3:
                warnings.append("evals/cases.json has <3 cases")
        except json.JSONDecodeError as e:
            errors.append(f"evals/cases.json parse error: {e}")

    # 5. Frontmatter @uses sanity (spoke paths referenced in hub)
    yaml_uses = re.findall(r"-\s+references/([a-z0-9\-]+\.md)", text)
    missing_in_frontmatter = set(REQUIRED_SPOKES) - set(yaml_uses)
    if missing_in_frontmatter:
        warnings.append(
            f"frontmatter @uses missing: {sorted(missing_in_frontmatter)}"
        )

    return {
        "skill": "design-skill",
        "hub_size_bytes": size,
        "hub_size_limit": HUB_SIZE_LIMIT,
        "errors": errors,
        "warnings": warnings,
        "status": "PASS" if not errors else "FAIL",
    }


if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
    result = validate(target)
    print(json.dumps(result, indent=2, ensure_ascii=False))
    sys.exit(0 if result["status"] == "PASS" else 1)
