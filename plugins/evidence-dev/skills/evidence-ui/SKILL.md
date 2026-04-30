---
name: evidence-ui
description: Evidence.dev UI layout components — Accordion, Alert, Grid, Tabs, Modal, Note, Details, DownloadData, Embed, Image, Link, LinkButton, BigLink, Info, LastRefreshed, PrintFormat
version: 1.0.0
---

# Evidence UI Components

Evidence.dev provides a set of built-in UI components for layout, navigation, content organization, and print formatting. All components are used directly in `.md` pages as HTML-style tags. No imports required.

---

## Level 1 — What Each Component Does + Minimal Syntax

| Component | Purpose | Minimal syntax |
|---|---|---|
| `Accordion` / `AccordionItem` | Collapsible sections | `<Accordion><AccordionItem title="X">content</AccordionItem></Accordion>` |
| `Alert` | Styled message banner | `<Alert>message</Alert>` |
| `BigLink` | Large styled navigation link | `<BigLink url="/path">Label</BigLink>` |
| `Details` | Single collapsible section | `<Details title="X">content</Details>` |
| `DownloadData` | CSV download button for a query | `<DownloadData data={query_name}/>` |
| `Embed` | iframe / video embed | `<Embed url="https://..."/>` |
| `Grid` | Multi-column layout | `<Grid cols=2>items</Grid>` |
| `Image` | Responsive image with controls | `<Image url="https://..."/>` |
| `Info` | Inline tooltip icon | `<Info description="tooltip text"/>` |
| `LastRefreshed` | Data freshness timestamp | `<LastRefreshed/>` |
| `Link` | Inline styled link | `<Link url="https://..." label="text"/>` |
| `LinkButton` | Link styled as a button | `<LinkButton url="/path">Label</LinkButton>` |
| `Modal` | Pop-up dialog triggered by a button | `<Modal buttonText="Open" title="Title">content</Modal>` |
| `Note` | Small/muted supplemental text | `<Note>footnote text</Note>` |
| `Tabs` / `Tab` | Tabbed content panes | `<Tabs><Tab label="X">content</Tab></Tabs>` |
| `LineBreak` | Explicit line break | `<LineBreak/>` |
| `PageBreak` | Print page break | `<PageBreak/>` |
| `PrintGroup` | Keep items on same print page | `<PrintGroup>items</PrintGroup>` |

---

## Level 2 — Common Props + Practical Layout Examples

### Accordion

Collapsible section group. Multiple items can be open simultaneously by default. Use `single` to allow only one open at a time.

```markdown
<Accordion>
  <AccordionItem title="Revenue Definition">

    Revenue is recognized when the subscription renews.

  </AccordionItem>
  <AccordionItem title="CAC Definition">

    Customer Acquisition Cost = total sales & marketing spend / new customers.

  </AccordionItem>
</Accordion>
```

Single-open mode:
```markdown
<Accordion single>
  <AccordionItem title="Q1">...</AccordionItem>
  <AccordionItem title="Q2">...</AccordionItem>
</Accordion>
```

Custom title slot (embed a `Value` component in the header):
```markdown
<AccordionItem title="Growth">
  <span slot='title'>Growth <Value data={growth} fmt=pct1 /></span>
  Body content here.
</AccordionItem>
```

**Key props — `Accordion`**
- `single` — only one item open at a time
- `class` — Tailwind classes on the accordion wrapper

**Key props — `AccordionItem`**
- `title` (required) — header text
- `description` — adds an info icon with tooltip
- `class` — Tailwind classes on the item

---

### Alert

Inline message banner. Default style is neutral. Use `status` for semantic color.

```markdown
<Alert status="warning">
  Data for December is preliminary and subject to revision.
</Alert>

<Alert status="negative">
  Pipeline sync failed — figures may be stale.
</Alert>
```

`status` options: `info` | `positive` | `warning` | `negative`

---

### BigLink

Large, styled card-style link. Use for navigation sections or prominent CTAs.

```markdown
<BigLink url="/sales/performance">Sales Performance Dashboard</BigLink>
<BigLink url="https://docs.evidence.dev">Documentation</BigLink>
```

- `url` (required) — internal path or full URL

---

### Details

Single collapsible section. Simpler than Accordion — no grouping. Expands all content on print by default.

```markdown
<Details title="Metric Definitions">

  **ARR** — Annualised Recurring Revenue, calculated from active subscriptions.

  **NRR** — Net Revenue Retention, includes expansion and churn.

</Details>
```

Start expanded:
```markdown
<Details title="Methodology" open=true>
  content
</Details>
```

**Key props**
- `title` — label shown next to the toggle icon (default: "Details")
- `open` — `true` / `false`, default `false`
- `printShowAll` — `true` / `false`, default `true` (expands on print)

---

### DownloadData

Renders a "Download" link that exports a query result as CSV. Not shown on mobile.

```markdown
<DownloadData data={orders}/>
<DownloadData data={orders} text="Export CSV" queryID=orders_export/>
```

**Key props**
- `data` (required) — query result variable `{query_name}`
- `text` — button label (default: "Download")
- `queryID` — prefix for the downloaded filename
- `display` — `true` / `false` (toggle visibility, e.g. from hover state)

---

### Embed

Renders an iframe. Useful for YouTube, Loom, Metabase, etc.

```markdown
<Embed
  url="https://www.youtube.com/embed/VIDEO_ID"
  title="Q4 Review Recording"
/>
```

Custom size, centered, no border:
```markdown
<Embed
  url="https://www.youtube.com/embed/VIDEO_ID"
  title="Demo"
  width=800
  height=450
  border=false
/>
```

**Key props**
- `url` (required) — embeddable URL (use embed/share URLs, not watch URLs)
- `title` — accessibility label
- `width` — pixels (default: 100%)
- `height` — pixels (default: 400)
- `border` — `true` / `false` (default: `true`)
- `class` — Tailwind classes on the wrapper

---

### Grid

Arranges direct children in a responsive column grid. Collapses to vertical on small screens. Wrap multiple items that should share one cell in a `<Group>`.

```markdown
<Grid cols=2>
  <LineChart data={sales} x=month y=revenue/>
  <BarChart data={sales} x=month y=orders/>
</Grid>
```

Mixed content in one cell using `Group`:
```markdown
<Grid cols=3>
  <BigValue data={kpis} value=revenue/>
  <BigValue data={kpis} value=orders/>
  <Group>
    Regional breakdown
    <DataTable data={by_region}/>
  </Group>
</Grid>
```

**Key props**
- `cols` — `1` | `2` | `3` | `4` | `5` | `6` (default: `2`)
- `gapSize` — `none` | `sm` | `md` | `lg` (default: `md`)

---

### Image

Responsive image with alignment, sizing, and border controls. For simple cases, standard markdown `![alt](url)` also works.

```markdown
<Image
  url="https://example.com/logo.png"
  description="Company logo"
  height=80
  align="left"
/>
```

With border and padding:
```markdown
<Image
  url="https://example.com/screenshot.png"
  description="Dashboard screenshot"
  height=400
  border=true
  class="p-4"
/>
```

**Key props**
- `url` (required)
- `description` — alt text for accessibility
- `width` / `height` — pixels
- `align` — `center` | `left` | `right` (default: `center`)
- `border` — `true` / `false` (default: `false`)
- `class` — Tailwind classes

---

### Info

Inline tooltip icon. Can be used standalone or is built into other components via their `description` prop.

```markdown
Revenue is net of refunds <Info description="Refunds processed within 30 days are excluded"/>
```

With theme color:
```markdown
<Info description="Calculated using trailing 12 months" color="primary"/>
```

**Key props**
- `description` (required) — tooltip text
- `color` — any valid color or theme token (default: `base-content-muted`)
- `size` — icon size number (default: `4`)
- `className` — custom class on the trigger element

---

### LastRefreshed

Shows how long ago the data was last built. Useful in page footers.

```markdown
<LastRefreshed/>
```

Custom prefix:
```markdown
<LastRefreshed prefix="Data last updated"/>
```

**Key props**
- `prefix` — text before the timestamp (default: "Last refreshed")
- `printShowDate` — `true` / `false` (default: `true` — shows full date on print instead of "X hours ago")
- `dateFmt` — date format string when `printShowDate=true`

---

### Link

Inline hyperlink component. Use when you need to control tab behavior or apply custom styles. Standard markdown `[text](url)` also works for basic links.

```markdown
<Link url="https://github.com/evidence-dev/evidence" label="View on GitHub"/>
<Link url="https://example.com" label="Opens in new tab" newTab=true/>
```

**Key props**
- `url` (required)
- `label` — link text (default: "Click here")
- `newTab` — `true` / `false` (default: `false`)
- `class` — Tailwind classes

---

### LinkButton

Renders a link styled as a button. Use for primary call-to-action navigation.

```markdown
<LinkButton url="/reports/executive-summary">
  View Executive Summary
</LinkButton>
```

- `url` (required) — internal path or full URL
- Content between tags is the button label

---

### Modal

Pop-up dialog with a trigger button. Supports markdown and embedded components inside the body.

```markdown
<Modal title="Methodology" buttonText="How is this calculated?">

  **ARR** is calculated from all active subscriptions at month-end.

  Churned accounts are excluded after the 5th of the following month.

</Modal>
```

With a chart inside:
```markdown
<Modal title="Monthly Trend" buttonText="See Chart">
  <LineChart data={monthly} x=month y=revenue/>
</Modal>
```

**Key props**
- `buttonText` (required) — label on the trigger button
- `title` — heading inside the modal
- `open` — `true` / `false` (default: `false`)

Note: leave a blank line after the opening tag when using markdown inside the body.

---

### Note

Small, muted text for footnotes, caveats, or source attribution.

```markdown
<Note>
  Figures exclude inter-company transactions. Source: Finance ERP, extracted 2024-01-31.
</Note>
```

Custom color using Tailwind:
```markdown
<Note class="text-negative">
  This metric is currently under review and may change.
</Note>
```

- `class` — Tailwind classes (use theme tokens like `text-positive`, `text-negative`, `text-warning`)

---

### Tabs / Tab

Organizes content into switchable panes. Each `Tab` requires a `label`.

```markdown
<Tabs>
  <Tab label="Overview">
    Summary content here.
  </Tab>
  <Tab label="Detail">
    <DataTable data={detail_rows}/>
  </Tab>
  <Tab label="Definitions">
    <Details title="Metrics">definitions...</Details>
  </Tab>
</Tabs>
```

**Key props — `Tabs`**
- `id` — string; when set, selected tab is persisted in the URL (shareable)
- `color` — active tab color (hex, rgb, hsl, or theme token; default: `base-content`)
- `fullWidth` — `true` / `false`, tabs stretch to full page width
- `background` — `true` / `false`, adds background fill to active tab

**Key props — `Tab`**
- `label` (required) — tab header text
- `id` — unique id (only needed if two tabs share the same label)
- `printShowAll` — `true` / `false` (default: `true` — all tabs printed, not just active)
- `description` — tooltip on the tab header

---

### Print Format Components

Three components control PDF/print layout. They have no visual effect on screen (except `LineBreak`).

**LineBreak** — inserts a line break in both UI and print:
```markdown
Revenue <LineBreak/> Cost
```
- `lines` — number of breaks (default: `1`)

**PageBreak** — forces a new page when printing/exporting PDF:
```markdown
<LineChart data={q1} x=month y=revenue/>

<PageBreak/>

<LineChart data={q2} x=month y=revenue/>
```

**PrintGroup** — keeps wrapped content together on the same print page; optionally hides content from print:
```markdown
<PrintGroup>
  <Heatmap data={channel_item} x=channel y=item value=orders/>
  <Heatmap data={channel_item} x=channel y=item value=revenue/>
</PrintGroup>
```

Hide from print only:
```markdown
<PrintGroup hidden=true>
  <BarChart data={experimental} x=month y=value/>
</PrintGroup>
```

- `hidden` — `true` / `false` (default: `false`); content is hidden in print/PDF but visible on screen

---

## Level 3 — Full Prop Reference Tables + Combining Components

### Accordion Props

**`<Accordion>`**

| Prop | Type | Default | Description |
|---|---|---|---|
| `single` | boolean | `false` | Only one item open at a time |
| `class` | string | — | Tailwind classes on the wrapper |

**`<AccordionItem>`**

| Prop | Type | Required | Default | Description |
|---|---|---|---|---|
| `title` | string | yes | — | Header text |
| `description` | string | — | — | Info icon with tooltip on hover |
| `class` | string | — | — | Tailwind classes on the item |

Slot: use `<span slot='title'>` inside `AccordionItem` to embed components (e.g. `Value`) in the header.

---

### Alert Props

| Prop | Options | Description |
|---|---|---|
| `status` | `info` / `positive` / `warning` / `negative` | Color variant; omit for default neutral |
| `description` | string | Info icon with tooltip |

---

### BigLink Props

| Prop | Type | Required | Description |
|---|---|---|---|
| `url` | string | yes | Internal path or full URL |

---

### Details Props

| Prop | Type | Default | Description |
|---|---|---|---|
| `title` | string | `"Details"` | Toggle label |
| `open` | boolean | `false` | Expanded by default |
| `printShowAll` | boolean | `true` | Expand on print/PDF |

---

### DownloadData Props

| Prop | Type | Required | Default | Description |
|---|---|---|---|---|
| `data` | query result | yes | — | Query variable `{name}` |
| `text` | string | — | `"Download"` | Button label |
| `queryID` | string | — | `"evidence_download"` | CSV filename prefix |
| `display` | boolean | — | `true` | Control visibility |

---

### Embed Props

| Prop | Type | Required | Default | Description |
|---|---|---|---|---|
| `url` | string | yes | — | Embeddable URL |
| `title` | string | — | `""` | Accessibility label |
| `width` | number | — | `100%` | Width in pixels |
| `height` | number | — | `400` | Height in pixels |
| `border` | boolean | — | `true` | Show border |
| `class` | string | — | — | Tailwind classes on wrapper |

---

### Grid Props

| Prop | Options | Default | Description |
|---|---|---|---|
| `cols` | `1`–`6` | `2` | Number of columns |
| `gapSize` | `none` / `sm` / `md` / `lg` | `md` | Gap between cells |

Use `<Group>` (no props) to group multiple items into a single grid cell.

---

### Image Props

| Prop | Type | Required | Default | Description |
|---|---|---|---|---|
| `url` | string | yes | — | Image URL |
| `description` | string | — | `""` | Alt text |
| `width` | number | — | — | Width in pixels |
| `height` | number | — | — | Height in pixels |
| `align` | `center` / `left` / `right` | — | `center` | Alignment |
| `border` | boolean | — | `false` | Show border |
| `class` | string | — | — | Tailwind classes |

---

### Info Props

| Prop | Type | Required | Default | Description |
|---|---|---|---|---|
| `description` | string | yes | — | Tooltip text |
| `color` | string | — | `base-content-muted` | Icon color (hex, token) |
| `size` | number | — | `4` | Icon size |
| `className` | string | — | — | Classes on trigger element |

---

### LastRefreshed Props

| Prop | Type | Default | Description |
|---|---|---|---|
| `prefix` | string | `"Last refreshed"` | Text before timestamp |
| `printShowDate` | boolean | `true` | Show full date on print |
| `dateFmt` | string | — | Format for print date (Evidence format string) |

---

### Link Props

| Prop | Type | Required | Default | Description |
|---|---|---|---|---|
| `url` | string | yes | — | Destination URL |
| `label` | string | — | `"Click here"` | Link text |
| `newTab` | boolean | — | `false` | Open in new tab |
| `class` | string | — | — | Tailwind classes |

---

### LinkButton Props

| Prop | Type | Required | Description |
|---|---|---|---|
| `url` | string | yes | Destination URL (internal or external) |

Content between tags becomes the button label.

---

### Modal Props

| Prop | Type | Required | Default | Description |
|---|---|---|---|---|
| `buttonText` | string | yes | — | Trigger button label |
| `title` | string | — | — | Heading inside the modal |
| `open` | boolean | — | `false` | Start open |

---

### Note Props

| Prop | Type | Description |
|---|---|---|
| `class` | string | Tailwind classes (e.g. `text-negative`, `text-warning`) |

---

### Tabs Props

**`<Tabs>`**

| Prop | Type | Default | Description |
|---|---|---|---|
| `id` | string | — | Persists selected tab in URL when set |
| `color` | string | `base-content` | Active tab color (hex / theme token) |
| `fullWidth` | boolean | `false` | Tabs span full page width |
| `background` | boolean | `false` | Background fill on active tab |

**`<Tab>`**

| Prop | Type | Required | Default | Description |
|---|---|---|---|---|
| `label` | string | yes | — | Tab header text |
| `id` | string | — | — | Override id (when labels are duplicated) |
| `printShowAll` | boolean | — | `true` | Show all tabs in print/PDF |
| `description` | string | — | — | Tooltip on tab header |

---

### PrintGroup Props

| Prop | Options | Default | Description |
|---|---|---|---|
| `hidden` | `true` / `false` | `false` | Hides content from print/PDF only |

**LineBreak:** `lines` (number, default `1`)

**PageBreak:** no props.

---

## Combining Components — Practical Patterns

### Dashboard section with tabs, grid, and download

```markdown
<Tabs id="revenue-tabs">
  <Tab label="Summary">
    <Grid cols=3>
      <BigValue data={kpis} value=arr title="ARR"/>
      <BigValue data={kpis} value=nrr title="NRR"/>
      <BigValue data={kpis} value=churn title="Churn Rate"/>
    </Grid>
    <LineChart data={monthly_arr} x=month y=arr/>
    <DownloadData data={monthly_arr} text="Export ARR data" queryID=arr_export/>
  </Tab>
  <Tab label="By Region">
    <DataTable data={by_region}/>
    <DownloadData data={by_region} queryID=region_export/>
  </Tab>
</Tabs>
```

### Accordion with embedded charts

```markdown
<Accordion single>
  <AccordionItem title="North America">
    <LineChart data={na_trend} x=month y=revenue/>
  </AccordionItem>
  <AccordionItem title="EMEA">
    <LineChart data={emea_trend} x=month y=revenue/>
  </AccordionItem>
</Accordion>
```

### Alert + Details for data quality notices

```markdown
<Alert status="warning">
  December figures are preliminary. Final numbers available by Jan 15.
</Alert>

<Details title="What changed?">

  The December close process was delayed due to a system migration.
  Numbers will be restated once the ERP sync is complete.

</Details>
```

### Print-ready report structure

```markdown
## Executive Summary

<PrintGroup>
  <Grid cols=3>
    <BigValue data={kpis} value=arr/>
    <BigValue data={kpis} value=nrr/>
    <BigValue data={kpis} value=new_logos/>
  </Grid>
</PrintGroup>

<PageBreak/>

## Regional Breakdown

<PrintGroup>
  <BarChart data={by_region} x=region y=revenue/>
  <DataTable data={by_region}/>
</PrintGroup>

<LastRefreshed prefix="Report generated"/>
```

### Modal for methodology without cluttering the page

```markdown
Revenue grew 23% YoY <Info description="Compared to same period prior year, constant currency"/>

<Modal title="Revenue Recognition Policy" buttonText="Full methodology">

  Revenue is recognized at the point of subscription renewal.

  **Exclusions:**
  - Intercompany transactions
  - Refunds processed within 30 days

</Modal>

<Note>
  All figures in USD thousands unless otherwise stated. Source: Salesforce + Stripe reconciliation.
</Note>
```

### Navigation hub page with BigLink and LinkButton

```markdown
## Dashboards

<Grid cols=2>
  <BigLink url="/sales/pipeline">Pipeline Overview</BigLink>
  <BigLink url="/finance/p-and-l">P&L Dashboard</BigLink>
  <BigLink url="/marketing/campaigns">Campaign Performance</BigLink>
  <BigLink url="/ops/capacity">Capacity Planning</BigLink>
</Grid>

<LineBreak lines=2/>

<LinkButton url="/admin/data-sources">Manage Data Sources</LinkButton>
```
