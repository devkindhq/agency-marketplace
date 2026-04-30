# Agency Marketplace

A domain-based Claude Code plugin marketplace by [DevKind](https://devkind.com.au). Each domain is a plugin, each skill lives inside it.

Built for teams that work with real data — analytics, reporting, SEO, and beyond.

## Structure

```
plugins/
├── evidence-dev/
│   └── skills/
│       ├── evidence-core-concepts   ← SQL queries, syntax, templating, themes
│       ├── evidence-charts          ← LineChart, BarChart, AreaChart, and 10 more
│       ├── evidence-data-components ← BigValue, DataTable, Delta, Value
│       ├── evidence-inputs          ← Dropdown, Slider, DateRange, DimensionGrid...
│       ├── evidence-maps            ← AreaMap, BubbleMap, PointMap, USMap
│       ├── evidence-ui              ← Accordion, Grid, Tabs, Modal, Alert...
│       ├── evidence-data-sources    ← BigQuery, DuckDB, Postgres, Snowflake...
│       ├── evidence-cli             ← install, dev, build, deploy
│       └── evidence-custom          ← custom Svelte components, plugin dev
└── seo/
    └── skills/
        └── search-quality-rater     ← Google Quality Rater Guidelines (E-E-A-T)
```

---

## Install

### Option 1 — From GitHub (recommended)

```bash
claude plugin marketplace add devkindhq/agency-marketplace

# Install individual plugins
claude plugin install evidence-dev@agency-marketplace
claude plugin install seo@agency-marketplace
```

### Option 2 — Local clone

```bash
git clone git@github.com:devkindhq/agency-marketplace.git
cd agency-marketplace
./install.sh
```

---

## Update

Pull the latest skills and refresh:

```bash
claude plugin marketplace update agency-marketplace
```

---

## Plugins

### evidence-dev

> Complete Claude Code skill suite for [Evidence.dev](https://evidence.dev) — the open-source business intelligence framework that lets you write reports in Markdown with SQL.

9 skills with progressive disclosure — quick reference at the top, full prop tables at the bottom. All props sourced directly from the Evidence.dev documentation.

| Skill | What it covers |
|-------|---------------|
| `evidence-core-concepts` | The mental model: SQL code fences, query variables, Svelte/Markdown hybrid syntax, loops, if/else, formatting, themes |
| `evidence-charts` | LineChart, BarChart, AreaChart, ScatterPlot, BubbleChart, Histogram, FunnelChart, Heatmap, CalendarHeatmap, BoxPlot, Sparkline, SankeyDiagram, ECharts |
| `evidence-data-components` | BigValue, DataTable (with Column child), Delta, Value |
| `evidence-inputs` | Dropdown, TextInput, Checkbox, DateInput, DateRange, Slider, ButtonGroup, DimensionGrid — with SQL filter integration patterns |
| `evidence-maps` | AreaMap, BaseMap, BubbleMap, PointMap, USMap — with GeoJSON and data shape requirements |
| `evidence-ui` | Accordion, Alert, Grid, Tabs, Modal, Note, Details, DownloadData, Embed, Image, Link, LinkButton, BigLink, LastRefreshed, PrintFormat |
| `evidence-data-sources` | BigQuery, PostgreSQL, MySQL, MSSQL, Snowflake, Redshift, DuckDB, MotherDuck, SQLite, Databricks, Trino, CSV, Google Sheets, JavaScript |
| `evidence-cli` | Install, dev server, build, deployment platforms, SPA vs SSG rendering modes, environment variables, base paths |
| `evidence-custom` | Custom Svelte components, component queries, plugin development and publishing |

---

### seo

> Skills for SEO practitioners working with Google's quality guidelines.

| Skill | What it covers |
|-------|---------------|
| `search-quality-rater` | Evaluate content against Google's Search Quality Rater Guidelines — E-E-A-T, Page Quality, Needs Met |

---

## About DevKind

[DevKind](https://devkind.com.au) builds AI-powered tools and workflows for digital agencies and data teams. This marketplace is part of our internal Claude Code setup, open-sourced for the community.

Contributions welcome — open a PR to add your own domain plugin.
