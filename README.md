# design-skill

> 🇰🇷 [한국어 README](./README.ko.md)

**Apple-inspired design engine: 4-layer content→design auto-mapping with 6 formats, 5 tones, and 18 patterns.**

## Prerequisites

- **Claude Cowork or Claude Code** environment

## Goal

design-skill eliminates ad-hoc styling decisions by encoding Apple-grade design principles into a deterministic pipeline. Content enters, and the engine auto-detects tone, assigns section roles, selects block patterns, then applies element-level point design — all governed by 4 axioms and 7 immutable core rules. The result: consistent, professional output across every format without manual design work.

## When & How to Use

Invoke whenever you need polished visual output — documents, presentations, dashboards, web pages, or Obsidian notes. The engine activates on creation requests ("만들어줘", "이쁘게", "디자인해줘") and cascades into format-specific skills (pptx, docx, xlsx, pdf, html-div-style). Best used at creation time rather than as post-processing.

## Use Cases

| Scenario | Prompt | What Happens |
|---|---|---|
| Report needs professional polish | `"깔끔하게 만들어줘"` | Tone auto-detect→section roles→block pattern selection→format-specific output |
| Presentation deck | `"이쁘니 해줘"` | 4-layer engine maps content to slides with typography ratios, 3-color system, whitespace rules |
| Obsidian knowledge base | `"디자인 적용해줘"` | md visual grammar (protocol-pretty) applies hierarchy, rhythm, and whitespace within Obsidian constraints |
| Data-heavy dashboard | `"디자인해줘"` | pro-grid tone→comparison/evidence patterns→clean-info styling with ≤55% content density |

## Architecture

### 4 Axioms
- **X1 Cognitive Finiteness** — limit information per view
- **X2 Hierarchy Efficiency** — visual weight guides reading order
- **X3 Rhythm Principle** — alternating density prevents fatigue
- **X4 Whitespace Amplification** — empty space amplifies adjacent content

### 7 Core Rules (immutable)
Typography ratio (4:2.3:1.5:1), font weight contrast (≥300), 3-color system, whitespace philosophy (≤55% content), alignment dichotomy, text-image separation, no-repeat rhythm.

### 4-Layer Engine
1. **Tone auto-detection** — dark-cinema · warm-human · clean-info · pro-grid · story-dark
2. **Section roles** — hero · feature intro · evidence · comparison · CTA · closing · appendix
3. **Block patterns** — 18 content-driven patterns (S1–S18) mapped by content type
4. **Element-level point design** — micro-level typography, spacing, and accent decisions

### 6 Output Formats
Each format has a dedicated reference file with format-specific rules:

| Format | Reference | Cascade Target |
|---|---|---|
| HTML | `format-html.md` | standalone or html-div-style |
| Markdown | `format-md.md` | Obsidian via protocol-pretty |
| PPTX | `format-pptx.md` | pptx skill |
| DOCX | `format-docx.md` | docx skill |
| XLSX | `format-xlsx.md` | xlsx skill |
| PDF | `format-pdf.md` | pdf skill |

### 5 Tone Presets
`tone-dark-cinema` · `tone-warm-human` · `tone-clean-info` · `tone-pro-grid` · `tone-story-dark`

## Works With

- **[deliverable-engine](https://github.com/jasonnamii/deliverable-engine)** — document structure and quality; design-skill adds visual layer
- **[html-div-style](https://github.com/jasonnamii/html-div-style)** — Obsidian-safe HTML div wrapper; design-skill provides the design logic
- **[ui-action-designer](https://github.com/jasonnamii/ui-action-designer)** — UI/UX design system; design-skill handles visual styling
- **[pptx](https://github.com/jasonnamii/pptx)** / **[docx](https://github.com/jasonnamii/docx)** / **[xlsx](https://github.com/jasonnamii/xlsx)** / **[pdf](https://github.com/jasonnamii/pdf)** — format-specific output skills

## Installation

```bash
git clone https://github.com/jasonnamii/design-skill.git ~/.claude/skills/design-skill
```

## Update

```bash
cd ~/.claude/skills/design-skill && git pull
```

Skills placed in `~/.claude/skills/` are automatically available in Claude Code and Cowork sessions.

## Part of Cowork Skills

This is one of 25+ custom skills. See the full catalog: [github.com/jasonnamii/cowork-skills](https://github.com/jasonnamii/cowork-skills)

## License

MIT License — feel free to use, modify, and share.
