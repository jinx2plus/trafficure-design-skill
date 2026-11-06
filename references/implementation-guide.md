# Implementation guide

## Prompt

> Build an **original** [traffic operations dashboard / spatial SaaS landing page] with the `trafficure-inspired-ui` skill. Follow semantic design tokens, map-first composition, calm editorial hierarchy, measured KPIs, severity colors, accessibility and mobile layout. All fictional data must be marked DEMO. Do not represent the proposed palette as official Lepton brand colors.

## Landing page

- Content width up to 1220px; hero grid 6/6 or 7/5
- Desktop section spacing 64–96px; mobile 48–56px
- Primary CTA teal on white, secondary outlined
- Light narrative blocks around a dark map preview
- KPIs with units, geography, source and time period

## Operations screen

- Toolbar: region, period, data source and timestamp
- Main: geography/network with severity legend and selection affordance
- Context: ranked alerts, affected links/corridors and baseline comparisons
- Lower: time trends, segment table, export actions
- States: loading / empty / stale / connectivity failure / insufficient access
- Map tile attribution and keyboard-accessible summary are required

## Reporting screen

- Include performance definitions before presenting rankings
- Compare current values to a stated reference period
- Label estimated/predicted values separately from observations
- Pair charts with an accessible data table or summary
- Highlight implications for traffic engineers, not merely decorative statistics

## Design customizations

Use user brand colors when available. Treat map-road colors as operational semantics, keeping labels/icons alongside each severity. Example brand and metrics are placeholders. Comply with selected basemap provider terms, attribution and licensing.

## Failure modes

- Never invent customer names, case-study results, live feed status or throughput impacts.
- Avoid placing a critical alert over the route map without dismiss/expand controls.
- Avoid a traffic signal red as a primary marketing CTA.
- Never claim precise official HEX values without a verifiable computed-style source.
