#!/usr/bin/env python3
"""Validate the structural requirements and a few WCAG contrast pairs."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md", "README_KO.md", "AGENTS.md", "LICENSE",
    ".agents/skills/trafficure-inspired-ui/SKILL.md",
    ".claude/skills/trafficure-inspired-ui/SKILL.md",
    "theme/tokens.css", "theme/components.css",
    "examples/dashboard.html", "examples/preview.svg",
    "references/site-audit.md", "references/implementation-guide.md",
]

def luminance(color):
    color = color.lstrip("#")
    rgb = [int(color[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    linear = [c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4 for c in rgb]
    return sum(a * b for a, b in zip(linear, (0.2126, 0.7152, 0.0722)))

def ratio(a, b):
    light, dark = sorted((luminance(a), luminance(b)), reverse=True)
    return (light + .05) / (dark + .05)

def main():
    errors = [f"Missing {path}" for path in REQUIRED if not (ROOT / path).is_file()]
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    css = (ROOT / "theme/tokens.css").read_text(encoding="utf-8")
    colors = dict(re.findall(r"(--color-[\w-]+):\s*(#[0-9A-Fa-f]{6})", css))
    checks = [
        ("body", "--color-ink", "--color-canvas"),
        ("muted body", "--color-ink-muted", "--color-canvas"),
        ("CTA", "--color-surface", "--color-accent"),
        ("dark body", "--color-night-ink", "--color-night"),
        ("dark muted", "--color-night-muted", "--color-night"),
    ]
    for label, fg, bg in checks:
        if fg not in colors or bg not in colors:
            errors.append(f"Missing token {fg} / {bg}")
            continue
        value = ratio(colors[fg], colors[bg])
        print(f"{label}: {value:.2f}:1")
        if value < 4.5:
            errors.append(f"Contrast below 4.5:1 for {label}")
    skill = (ROOT / ".agents/skills/trafficure-inspired-ui/SKILL.md").read_text(encoding="utf-8")
    if not skill.startswith("---\nname: trafficure-inspired-ui"):
        errors.append("SKILL.md frontmatter is invalid")
    if "NOT official" not in skill and "not official" not in skill.lower():
        errors.append("Missing unofficial-design caveat")
    html = (ROOT / "examples/dashboard.html").read_text(encoding="utf-8")
    for text in ('SIMULATED · NOT LIVE', 'role="img"', 'aria-label="Map legend"', 'class="mobile-nav"'):
        if text not in html:
            errors.append(f"Missing demo feature: {text}")
    if errors:
        print("\n".join("ERROR: " + error for error in errors), file=sys.stderr)
        return 1
    print("VALIDATION PASSED — files, provenance, contrast checks")
    return 0

if __name__ == "__main__":
    sys.exit(main())
