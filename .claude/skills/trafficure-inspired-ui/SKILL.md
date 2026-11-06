---
name: trafficure-inspired-ui
description: Design original, accessible traffic intelligence, GIS, ITS, smart-city, and location analytics websites and dashboards, inspired by Lepton Software / TraffiCure's public information hierarchy. Map-first workflows, responsible KPI use, semantic status colors, responsive layouts.
---

# TraffiCure-inspired UI design skill

> Independent and unofficial. This skill is **not** Lepton Software's official brand guideline, copied CSS, or pixel-perfect UI. Colors and fonts below are **proposed** choices, not values verified by computed CSS inspection. Never imply Lepton affiliation or copy logos/illustrations/screenshots.

## When to use

Use for a geospatial product landing page, road-network operations room, traffic analytics dashboard, incident alerts, GIS reporting, location intelligence service, ITS performance monitoring, or urban mobility interface.

## Workflow

1. **Define the job to be done.** Ask what decision the operator/researcher must make and which evidence supports it. Choose marketing page, monitoring console, or hybrid.
2. **Use an original identity.** Product naming, logos and claims must be new. Use `theme/tokens.css` as an *optional proposed* semantic palette; retain user brand colors if provided.
3. **Organize the narrative.** Small eyebrow → short, decisive headline → value proposition → clear primary CTA → believable map/product preview → evidence-backed KPIs → use cases/capabilities → final CTA.
4. **Make maps the focal point.** Geographic network, corridor selection, congestion legend, incident markers, selected-link details, last-updated stamp. For real map tiles, preserve provider attribution and licensing.
5. **Ground every metric.** Always specify units, geography, measurement window, baseline and observed-vs-predicted status. Never present invented data as live.
6. **Use semantic severity.** Green/teal: normal or positive; amber: caution; coral/red: serious traffic disruption; blue: selection/information. Add labels/icons; color alone is insufficient.
7. **Create calm components.** KPI cards, network map, event queue, chips, evidence captions, filters, tables, buttons, and well-defined loading/empty/error/stale states.
8. **Implement responsive.** Test at desktop 1440px and 1024px, tablet 768px, mobile 390px. Stack map panels, collapse navigation and retain accessible alerts on mobile.
9. **Validate accessibility.** Use semantic headings/regions, keyboard focus, contrast ≥ 4.5:1 normal text, ≥ 3:1 large, reduced-motion support, visible labels/units, descriptive map fallback.
10. **Review provenance.** Distinguish *observed site organization* from *original interpretive implementation*. Cite sources when discussing TraffiCure facts; no unauthorized logos or copied site code.

## Visual system

- **Mood:** clean B2B geospatial intelligence, technical but legible; avoid excessive sci-fi neon and decorative fake metrics.
- **Composition:** light editorial landing surface with dark inset map/operations panel; clear type hierarchy; restrained section spacing and borders; one strong CTA per section.
- **Proposed palette (NOT official):** Ink `#101D2C`, night `#0A1626`, canvas `#F6F8FA`, accent teal `#0F766E`, info blue `#3276EA`, warn `#B45309`, danger `#CF384B`.
- **Proposed text:** Inter / Pretendard / Noto Sans KR / system UI. Use tabular numerals for KPIs.
- **Spacing:** 4px base scale; 12–16px common radii, 24px large radii; max content width 1220px.
- **Structure:** 12-column marketing grid; cards and operations panels reflow based on usable width.

## Suggested page structure

1. Header with restrained nav and primary `Request demo` CTA.
2. Headline/benefit hero with network preview.
3. Evidence metrics with units and provenance.
4. How it works in 3–4 numbered stages.
5. Persona or use-case sections (operator, planner, traffic police, asset manager).
6. Sample reporting section showing map, table, and time-window controls.
7. Final CTA / footer with privacy, disclaimer, and attribution.

## Dashboard component contract

- **Global toolbar:** geography, time zone, period, data freshness, dataset/source.
- **Map:** readable base/network, click/keyboard-accessible selection, zoom, severity legend.
- **KPIs:** traffic volume, mean speed (km/h), delay (min), alert count, comparison baseline.
- **Alerts:** road/segment, severity, observed time, affected direction, link to details.
- **Detail panel:** current versus typical, simple temporal trend, operational next steps.
- **Guardrails:** conspicuous mock-data label; stale threshold; explicit unavailable/error states.

## Sample agent prompt

"Use `trafficure-inspired-ui` to build an original Korean GIS/ITS monitoring dashboard for traffic congestion and incidents. Use the project CSS tokens and reusable patterns, prioritize map context and KPIs with units/timestamps, keep example data labeled as DEMO, implement responsive/mobile and WCAG-AA-friendly controls. Do not copy Lepton branding."

## Repository assets

- `theme/tokens.css` — proposed semantic tokens
- `theme/components.css` — sample responsive components
- `examples/dashboard.html` — original fictitious demo
- `references/site-audit.md` — source observations vs uncertain visual details
- `references/implementation-guide.md` — component and prompt specifications
- `scripts/validate.py` — local structural/contrast check

Reviewed 2026-11-06. Official public references: https://leptonsoftware.com/ and https://leptonsoftware.com/trafficure/.
