---
name: evidence-charts
description: Evidence.dev chart components — LineChart, BarChart, AreaChart, ScatterPlot, BubbleChart, Histogram, FunnelChart, Heatmap, CalendarHeatmap, BoxPlot, Sparkline, SankeyDiagram and custom ECharts
version: 1.0.0
---

# Evidence.dev Chart Components

Evidence charts are written as Svelte/HTML components inside `.md` files. Data is provided via SQL query blocks, then referenced by query name in curly braces. All charts are built on ECharts and support synchronized tooltips, annotations, and custom ECharts config overrides.

---

## Quick Reference

| Component | Use for | Minimum required props |
|---|---|---|
| `LineChart` | Trends over time, multi-series | `data`, `x`, `y` |
| `BarChart` | Category comparison, stacked/grouped | `data`, `x`, `y` |
| `AreaChart` | Cumulative trends, part-of-whole over time | `data`, `x`, `y` |
| `ScatterPlot` | Correlation between two numeric columns | `data`, `x`, `y` |
| `BubbleChart` | Three-metric comparison per category | `data`, `x`, `y`, `size` |
| `Histogram` | Distribution of a single metric | `data`, `x` |
| `FunnelChart` | Conversion / stage drop-off | `data`, `nameCol`, `valueCol` |
| `Heatmap` | Patterns across two categorical dimensions | `data`, `x`, `y`, `value` |
| `CalendarHeatmap` | Daily metric over weeks/months (GitHub style) | `data`, `date`, `value` |
| `BoxPlot` | Distribution summary (median, quartiles, whiskers) | `data`, `name`, `midpoint` |
| `Sparkline` | Compact inline trend | `data`, `dateCol`, `valueCol` |
| `SankeyDiagram` | Flows between categories | `data`, `sourceCol`, `targetCol`, `valueCol` |
| `ECharts` | Fully custom chart using raw ECharts config | `config` |
| `Chart` + primitives | Mixed-type charts (bar + line, etc.) | `data` on `<Chart>`, `y` on primitives |

---

## LineChart

Display how one or more metrics vary over time.

**Minimal usage:**
```svelte
<LineChart data={orders_by_month} x=month y=sales_usd0k />
```

**Common props:**

| Prop | Type | Default | Description |
|---|---|---|---|
| `data` | query name | required | Query result in `{curly braces}` |
| `x` | column name | required | X-axis column |
| `y` | column name or array | required | Y-axis column(s) |
| `series` | column name | — | Column that splits data into multiple series |
| `y2` | column name or array | — | Secondary y-axis column(s) |
| `y2SeriesType` | `line` \| `bar` \| `scatter` | `line` | Chart type for y2 series |
| `yFmt` | format string | — | Format for y values (e.g. `usd0k`, `pct1`) |
| `xFmt` | format string | — | Format for x values |
| `title` | string | — | Chart title (top left) |
| `subtitle` | string | — | Subtitle below title |
| `step` | boolean | `false` | Render as step line |
| `markers` | boolean | `false` | Show data point markers |
| `markerShape` | `circle` \| `emptyCircle` \| `rect` \| `triangle` \| `diamond` | `circle` | Marker shape when `markers=true` |
| `labels` | boolean | `false` | Show value labels on points |
| `colorPalette` | array of colors | built-in | Custom color array |
| `seriesColors` | `{{"SeriesName": "color"}}` | — | Per-series color overrides |
| `connectGroup` | string | — | Sync tooltips with other charts sharing the same name |

**Example — multi-series with secondary axis and bar:**
```svelte
<LineChart
    data={orders_by_month}
    x=month
    y=sales_usd0k
    y2=orders
    y2SeriesType=bar
    yAxisTitle="Sales per Month"
    title="Monthly Performance"
/>
```

**Example — step line with custom palette:**
```svelte
<LineChart
    data={orders_by_category}
    x=month
    y=sales_usd0k
    series=category
    step=true
    colorPalette={['#cf0d06', '#eb5752', '#e88a87', '#fcdad9']}
/>
```

**Annotations** (nest inside the chart tag):
```html
<LineChart data={orders_by_month} x=month y=sales yFmt=usd0>
    <ReferenceLine y=9000 label="Target" />
    <ReferenceArea xMin='2020-03-14' xMax='2020-08-15' label="Lockdown" color=warning />
</LineChart>
```

---

## BarChart

Compare a metric across categories. Supports stacked, grouped, 100% stacked, and horizontal layouts.

**Minimal usage:**
```svelte
<BarChart data={orders_by_month} x=month y=sales />
```

**Common props:**

| Prop | Type | Default | Description |
|---|---|---|---|
| `data` | query name | required | |
| `x` | column name | first column | X-axis column |
| `y` | column name or array | numeric columns | Y-axis column(s) |
| `series` | column name | — | Column for multi-series grouping |
| `type` | `stacked` \| `grouped` \| `stacked100` | `stacked` | Bar grouping method |
| `swapXY` | boolean | `false` | Flip to horizontal bar chart |
| `y2` | column name | — | Secondary y-axis |
| `y2SeriesType` | `bar` \| `line` \| `scatter` | `bar` | Type for y2 series |
| `yFmt` | format string | — | |
| `labels` | boolean | `false` | Show value labels |
| `stackTotalLabel` | boolean | `true` | Show total label on stacked bars |
| `fillColor` | color | — | Override bar fill color (single series) |
| `colorPalette` | array of colors | built-in | |
| `seriesColors` | `{{"Name": "color"}}` | — | |
| `title` | string | — | |
| `subtitle` | string | — | |

**Example — horizontal grouped bar:**
```svelte
<BarChart
    data={categories_by_channel}
    x=category
    y=sales
    series=channel
    type=grouped
    swapXY=true
    title="Sales by Channel"
/>
```

**Example — 100% stacked with labels:**
```svelte
<BarChart
    data={orders_by_category}
    x=month
    y=sales
    yFmt=pct0
    series=category
    type=stacked100
    labels=true
/>
```

**Example — dual axis with line overlay:**
```svelte
<BarChart
    data={orders_by_month}
    x=month
    y=sales
    yFmt=usd0k
    y2=num_orders
    y2SeriesType=line
/>
```

---

## AreaChart

Track how a metric with multiple series changes over time. Emphasizes changes in the sum of series.

**Minimal usage:**
```svelte
<AreaChart data={orders_by_month} x=month y=sales />
```

**Common props:**

| Prop | Type | Default | Description |
|---|---|---|---|
| `data` | query name | required | |
| `x` | column name | required | |
| `y` | column name or array | required | |
| `series` | column name | — | Split into multiple area series |
| `type` | `stacked` \| `stacked100` | `stacked` | |
| `step` | boolean | `false` | Step-line style |
| `fillColor` | color | — | Area fill color override |
| `lineColor` | color | — | Line color override |
| `fillOpacity` | 0–1 | `0.7` | Transparency of fill |
| `line` | boolean | `true` | Show line on top of area |
| `labels` | boolean | `false` | Show value labels |
| `labelFmt` | format string | same as y | Format for labels |
| `handleMissing` | `gap` \| `connect` \| `zero` | `gap` (single) / `zero` (multi) | |
| `yFmt` | format string | — | |
| `colorPalette` | array of colors | built-in | |

**Example — stacked area with formatted axis:**
```svelte
<AreaChart
    data={orders_by_category}
    x=month
    y=sales
    series=category
    yFmt=usd0
/>
```

**Example — 100% stacked with step:**
```svelte
<AreaChart
    data={orders_by_category}
    x=month
    y=sales
    series=category
    type=stacked100
    step=true
/>
```

---

## ScatterPlot

Show the correlation between two numeric metrics, optionally broken into series.

**Minimal usage:**
```svelte
<ScatterPlot data={price_vs_volume} x=price y=number_of_units />
```

**Common props:**

| Prop | Type | Default | Description |
|---|---|---|---|
| `data` | query name | required | |
| `x` | column name | required | |
| `y` | column name or array | required | |
| `series` | column name | — | Color-code points by category |
| `tooltipTitle` | column name | — | Column to use as tooltip title (e.g. product name) |
| `shape` | `circle` \| `emptyCircle` \| `rect` \| `triangle` \| `diamond` | `circle` | |
| `pointSize` | number | `10` | Size of points in pixels |
| `opacity` | 0–1 | `0.7` | |
| `fillColor` | color | — | Single-color override |
| `xFmt` | format string | — | |
| `yFmt` | format string | — | |
| `xAxisTitle` | boolean or string | `true` | |
| `yAxisTitle` | boolean or string | `true` | |
| `xMin` / `xMax` | number | — | Axis range |
| `yMin` / `yMax` | number | — | Axis range |
| `colorPalette` | array of colors | built-in | |

**Example — multi-series with axis formatting:**
```svelte
<ScatterPlot
    data={price_vs_volume}
    x=price
    y=number_of_units
    xFmt=usd0
    series=category
    tooltipTitle=product_name
/>
```

**Annotations supported** via `<ReferenceLine>` and `<ReferenceArea>` nested inside.

---

## BubbleChart

Display three metrics per data point: x position, y position, and bubble size.

**Minimal usage:**
```svelte
<BubbleChart data={price_vs_volume} x=price y=number_of_units size=total_sales />
```

**Common props:**

| Prop | Type | Default | Description |
|---|---|---|---|
| `data` | query name | required | |
| `x` | column name | required | |
| `y` | column name or array | required | |
| `size` | column name | required | Column that determines bubble size |
| `series` | column name | — | |
| `sizeFmt` | format string | — | Format for size column in tooltip |
| `scaleTo` | number | `1` | Multiply bubble sizes by this factor |
| `opacity` | 0–1 | `0.7` | |
| `shape` | `circle` \| `emptyCircle` \| `rect` \| `triangle` \| `diamond` | `circle` | |
| `tooltipTitle` | column name | — | |
| `xFmt` / `yFmt` | format string | — | |
| `colorPalette` | array of colors | built-in | |

**Example:**
```svelte
<BubbleChart
    data={price_vs_volume}
    x=price
    xFmt=usd0
    y=number_of_units
    series=category
    size=total_sales
    scaleTo=1.5
/>
```

---

## Histogram

Display the distribution of a metric by automatically binning values into buckets.

**Minimal usage:**
```svelte
<Histogram data={orders} x=sales />
```

**Common props:**

| Prop | Type | Default | Description |
|---|---|---|---|
| `data` | query name | required | |
| `x` | column name | required | Column to distribute (numeric) |
| `xFmt` | format string | — | Format for x-axis values |
| `fillColor` | color | — | Bar fill color |
| `fillOpacity` | 0–1 | `1` | |
| `xAxisTitle` | boolean or string | `false` | |
| `yAxisTitle` | boolean or string | `false` | |
| `yMin` / `yMax` | number | — | |
| `title` | string | — | |
| `subtitle` | string | — | |

**Example:**
```svelte
<Histogram
    data={orders}
    x=sales
    xAxisTitle="Order Value (USD)"
    fillColor="#476fff"
    title="Order Value Distribution"
/>
```

---

## FunnelChart

Visualize conversion across sequential stages.

**Minimal usage:**
```svelte
<FunnelChart data={funnel_data} nameCol=stage valueCol=customers />
```

**Common props:**

| Prop | Type | Default | Description |
|---|---|---|---|
| `data` | query name | required | |
| `nameCol` | column name | required | Column containing stage names |
| `valueCol` | column name | required | Column containing numeric values |
| `valueFmt` | format string | — | Format for value labels |
| `showPercent` | boolean | `false` | Show percentage in labels |
| `funnelSort` | `none` \| `ascending` \| `descending` | `none` | Sort order of stages |
| `funnelAlign` | `left` \| `right` \| `center` | `center` | Horizontal alignment |
| `labelPosition` | `left` \| `right` \| `inside` | `inside` | Where stage labels appear |
| `colorPalette` | array of colors | built-in | |
| `title` | string | — | |
| `subtitle` | string | — | |
| `legend` | boolean | `true` | |

**Example:**
```svelte
<FunnelChart
    data={funnel_data}
    nameCol=stage
    valueCol=customers
    showPercent=true
    funnelAlign=left
    title="Conversion Funnel"
/>
```

---

## Heatmap

Show patterns in a single metric across two categorical dimensions using color intensity.

**Important:** x and y columns must be strings. Cast date columns to string in your SQL before use.

**Minimal usage:**
```svelte
<Heatmap data={orders} x=day y=category value=order_count />
```

**Common props:**

| Prop | Type | Default | Description |
|---|---|---|---|
| `data` | query name | required | |
| `x` | column name | required | String column for x-axis |
| `y` | column name | required | String column for y-axis |
| `value` | column name | required | Numeric column for cell values |
| `valueFmt` | format string | — | Format for cell values |
| `colorScale` | array of colors | built-in | Color gradient e.g. `{['white', 'maroon']}` |
| `min` / `max` | number | data min/max | Override color scale bounds |
| `nullsZero` | boolean | `true` | Treat nulls as zero |
| `valueLabels` | boolean | `true` | Show values in cells |
| `cellHeight` | number | `30` | Row height in pixels |
| `borders` | boolean | `true` | Show cell borders |
| `xLabelRotation` | number | `0` | Rotate x-axis labels (e.g. `-45`) |
| `xAxisPosition` | `top` \| `bottom` | `top` | |
| `xSort` / `ySort` | column name | — | Sort axis by a column |
| `xSortOrder` / `ySortOrder` | `asc` \| `desc` | `asc` | |
| `filter` | boolean | `false` | Enable draggable legend filter |
| `title` | string | — | |
| `subtitle` | string | — | |

**Example — custom colors with rotated labels:**
```svelte
<Heatmap
    data={item_state}
    x=item
    y=state
    value=orders
    colorScale={['white', 'maroon']}
    xLabelRotation=-45
    cellHeight=25
    title="Item Sales by State"
    rightPadding=40
/>
```

---

## CalendarHeatmap

Display a daily metric across weeks and months in GitHub contribution graph style.

**Minimal usage:**
```svelte
<CalendarHeatmap data={orders_by_day} date=day value=sales />
```

**Common props:**

| Prop | Type | Default | Description |
|---|---|---|---|
| `data` | query name | required | |
| `date` | column name | required | Date column (one row per day) |
| `value` | column name | required | Numeric column |
| `valueFmt` | format string | — | |
| `colorScale` | array of colors | built-in | e.g. `{['#ebedf0', '#216e39']}` |
| `min` / `max` | number | data min/max | Color scale bounds |
| `yearLabel` | boolean | `true` | Show year label on left |
| `monthLabel` | boolean | `true` | Show month labels on top |
| `dayLabel` | boolean | `true` | Show day labels on left |
| `legend` | boolean | `true` | |
| `filter` | boolean | `false` | Draggable legend filter |
| `title` | string | — | |
| `subtitle` | string | — | |

**Example — custom color scale, multi-year:**
```svelte
<CalendarHeatmap
    data={orders_by_day}
    date=day
    value=sales
    colorScale={['rgb(254,234,159)', 'rgb(218,66,41)']}
    title="Daily Sales"
/>
```

---

## BoxPlot

Summarize the distribution of a metric using median, quartiles, and optional whiskers. Requires pre-aggregated data.

**Minimal usage (with quartiles):**
```svelte
<BoxPlot
    data={sales_distribution_by_channel}
    name=channel
    intervalBottom=first_quartile
    midpoint=median
    intervalTop=third_quartile
/>
```

**Or use confidence interval shorthand:**
```svelte
<BoxPlot data={experiments} name=experiment midpoint=median confidenceInterval=margin_of_error />
```

**Common props:**

| Prop | Type | Default | Description |
|---|---|---|---|
| `data` | query name | required | |
| `name` | column name | required | Column for box labels (x-axis) |
| `midpoint` | column name | required | Column for the center line |
| `intervalBottom` | column name | — | Bottom of box (e.g. Q1) |
| `intervalTop` | column name | — | Top of box (e.g. Q3) |
| `confidenceInterval` | column name | — | Alternative: half-width of box (midpoint ± CI) |
| `min` | column name | — | Whisker minimum |
| `max` | column name | — | Whisker maximum |
| `yFmt` | format string | — | |
| `color` | column name | — | Column containing color strings per box |
| `seriesColors` | `{{"Name": "color"}}` | — | |
| `swapXY` | boolean | `false` | Horizontal layout |
| `yMin` / `yMax` | number | — | |
| `title` | string | — | |

**Example — horizontal with whiskers:**
```svelte
<BoxPlot
    data={sales_distribution_by_channel}
    name=channel
    min=min
    intervalBottom=first_quartile
    midpoint=median
    intervalTop=third_quartile
    max=max
    yFmt=usd0
    swapXY=true
    title="Daily Sales Distribution"
/>
```

---

## Sparkline

A compact inline chart for embedding in tables or prose. Renders small and is optimized for space.

**Minimal usage:**
```svelte
<Sparkline data={sales_by_date} dateCol=date valueCol=sales />
```

**Common props:**

| Prop | Type | Default | Description |
|---|---|---|---|
| `data` | query name | required | |
| `dateCol` | column name | required | Date/category column |
| `valueCol` | column name | required | Numeric column |
| `type` | `line` \| `area` \| `bar` | `line` | Sparkline style |
| `color` | color | — | Line/area/bar color |
| `valueFmt` | format string | — | Tooltip value format |
| `dateFmt` | format string | — | Tooltip date format |
| `height` | number | `15` | Height in pixels |
| `width` | number | `50` | Width in pixels |
| `yScale` | boolean | `false` | Scale y-axis to data range |
| `interactive` | boolean | `true` | Enable hover tooltip (false = static SVG) |
| `connectGroup` | string | — | Sync with other charts |

**Example — three synced sparklines:**
```html
<Sparkline data={sales} dateCol=date valueCol=sales type=bar  valueFmt=usd dateFmt=mmm connectGroup=g1/>
<Sparkline data={sales} dateCol=date valueCol=sales type=area color=maroon valueFmt=usd dateFmt=mmm connectGroup=g1/>
<Sparkline data={sales} dateCol=date valueCol=sales type=line color=purple valueFmt=usd dateFmt=mmm connectGroup=g1/>
```

---

## SankeyDiagram

Display flows of a metric transferring between categories. Supports multi-level flows via `UNION ALL` queries.

**Minimal usage:**
```svelte
<SankeyDiagram data={traffic_data} sourceCol=source targetCol=target valueCol=count />
```

**Common props:**

| Prop | Type | Default | Description |
|---|---|---|---|
| `data` | query name | required | |
| `sourceCol` | column name | required | Origin node column |
| `targetCol` | column name | required | Destination node column |
| `valueCol` | column name | required | Flow volume column |
| `percentCol` | column name | — | Column for percent labels on links |
| `valueFmt` | format string | — | |
| `orient` | `horizontal` \| `vertical` | `horizontal` | Layout direction |
| `nodeLabels` | `name` \| `value` \| `full` | `name` | What to show on nodes |
| `linkLabels` | `full` \| `value` \| `percent` | `full` | What to show on links (requires `percentCol` for `full`/`percent`) |
| `linkColor` | `base-content-muted` \| `source` \| `target` \| `gradient` | `base-content-muted` | Color of flow links |
| `nodeAlign` | `justify` \| `left` \| `right` | `justify` | Horizontal node alignment |
| `nodeGap` | number | `8` | Gap between nodes in pixels |
| `nodeWidth` | number | `20` | Node rectangle width |
| `depthOverride` | `{{"node name": depth}}` | — | Force a node to a specific depth level |
| `colorPalette` | array of colors | built-in | |
| `sort` | boolean | `false` | Sort nodes by size |
| `title` | string | — | |
| `subtitle` | string | — | |

**Example — vertical layout with value labels and gradient links:**
```svelte
<SankeyDiagram
    data={traffic_data}
    sourceCol=source
    targetCol=target
    valueCol=count
    orient=vertical
    nodeLabels=full
    valueFmt=num0k
    linkColor=gradient
    colorPalette={['#ad4940', '#3d8cc4', '#1b5218', '#ebb154']}
    title="Traffic Flow"
/>
```

**Multi-level sankey** — union all levels in one query using the same source/target columns:
```sql
select channel as source, 'all_traffic' as target, count(*) as count from events group by 1, 2
union all
select 'all_traffic' as source, page_route as target, count(*) as count from events group by 1, 2
```

---

## Mixed-Type Charts

Combine bar, line, area, scatter, and bubble primitives on a single chart using the `<Chart>` wrapper.

**Basic structure:**
```svelte
<Chart data={fda_recalls}>
    <Bar y=voluntary_recalls />
    <Line y=fda_recalls name="FDA Recalls" />
</Chart>
```

**`<Chart>` props** (same axis/styling props as other charts):

| Prop | Description |
|---|---|
| `data` | Query result |
| `x` | X-axis column (defaults to first column) |
| `y` | Default y-axis column |
| `series` | Default series column |
| `title`, `subtitle`, `legend` | Chart chrome |
| `swapXY` | Horizontal layout |
| `yMin`, `yMax`, `yScale`, `yLog` | Axis control |
| `colorPalette`, `seriesColors` | Colors |
| `echartsOptions` | Raw ECharts override |

**Primitive components and their key props:**

| Primitive | Key props |
|---|---|
| `<Line>` | `y`, `series`, `name`, `lineColor`, `lineType` (`solid`/`dashed`/`dotted`), `lineWidth`, `markers`, `markerShape` |
| `<Bar>` | `y`, `name`, `type` (`stacked`/`grouped`), `stackName`, `fillColor`, `fillOpacity` |
| `<Area>` | `y`, `series`, `name`, `fillColor`, `fillOpacity`, `line` |
| `<Scatter>` | `y`, `name`, `shape`, `pointSize`, `opacity`, `fillColor` |
| `<Bubble>` | `y`, `size`, `name`, `shape`, `minSize`, `maxSize`, `opacity` |
| `<Hist>` | `x`, `fillColor`, `fillOpacity` |

**Tip:** The easiest mixed-type chart is a secondary axis on `LineChart` or `BarChart` using `y2` and `y2SeriesType`.

---

## Annotations

All standard charts support nested annotation components: `ReferenceLine`, `ReferenceArea`, `ReferencePoint`, and `Callout`.

### ReferenceLine

Draw a horizontal, vertical, or sloped line.

```html
<!-- Horizontal line at y value -->
<ReferenceLine y=9000 label="Target" />

<!-- Vertical line at x value -->
<ReferenceLine x='2020-03-14' label="Launch" hideValue=true />

<!-- Sloped line between two points -->
<ReferenceLine x='2019-01-01' y=6500 x2='2021-12-01' y2=12000 label="Trend" />

<!-- Lines from a dataset -->
<ReferenceLine data={milestones} x=date label=event_name hideValue />
```

**Key styling props:** `color`, `lineColor`, `lineType` (`solid`/`dashed`/`dotted`), `lineWidth`, `labelPosition` (`aboveStart`/`aboveCenter`/`aboveEnd`/`belowStart`/`belowCenter`/`belowEnd`), `labelColor`, `bold`, `italic`

**Semantic colors:** `positive`, `negative`, `warning`, `info`, `base-content-muted`

### ReferenceArea

Highlight a band or box on the chart.

```html
<!-- X-axis range -->
<ReferenceArea xMin='2020-03-14' xMax='2020-06-30' label="Lockdown" color=warning />

<!-- Y-axis range -->
<ReferenceArea yMin=250 color=positive label="Good" />

<!-- Box (x and y range) -->
<ReferenceArea xMin=16000 xMax=24000 yMin=-0.03 yMax=0.055 label="Target zone" border=true />

<!-- From a dataset -->
<ReferenceArea data={campaigns} xMin=start_date xMax=end_date label=campaign_name />
```

**Key styling props:** `color`, `areaColor`, `opacity`, `border`, `borderColor`, `borderType`, `labelPosition` (`topLeft`/`top`/`topRight`/`left`/`center`/`right`/`bottomLeft`/`bottom`/`bottomRight`), `labelColor`

### ReferencePoint

Annotate a specific x/y coordinate.

```html
<ReferencePoint x="2019-07-01" y=6590 label="Big drop" labelPosition=bottom />

<!-- From a dataset -->
<ReferencePoint data={anomalies} x=date y=value label=description labelPosition=bottom />
```

**Key styling props:** `color`, `symbol` (`circle`/`rect`/`triangle`/`diamond`/`pin`/`arrow`/`none`), `symbolSize`, `symbolOpacity`, `labelPosition` (`top`/`right`/`bottom`/`left`)

### Callout

Like `ReferencePoint` but styled for longer descriptive text.

```html
<Callout x="2021-05-01" y=11012 labelPosition=bottom>
    Sales spike due to
    holiday campaign launch
</Callout>
```

---

## Custom ECharts

### echartsOptions — Override the ECharts config

Available on all standard charts. Note the **double curly braces**.

```svelte
<BarChart
    data={query_name}
    x=col_x
    y=col_y
    echartsOptions={{
        legend: {
            right: 'right',
            top: 'middle',
            orient: 'vertical'
        },
        grid: { right: '120px' }
    }}
/>
```

### seriesOptions — Apply options to all series

Avoids repeating per-series config when all series need the same change.

```svelte
<BarChart
    data={country_sales}
    x=year
    y=sales
    series=country
    seriesOptions={{
        itemStyle: {
            borderWidth: 1,
            borderColor: 'red'
        }
    }}
/>
```

### printEchartsConfig — Debug helper

Add `printEchartsConfig=true` to any chart to print the full ECharts config below the chart. Useful when writing custom `echartsOptions`.

```svelte
<LineChart data={q} x=date y=value printEchartsConfig=true />
```

### ECharts Component — Fully custom charts

Use `<ECharts config={...}>` for chart types not covered by Evidence components (treemap, pie, donut, gauge, etc.). Data must be included in the config object; spread query results with `[...query_name]`.

```svelte
<ECharts config={
    {
        tooltip: { formatter: '{b}: {c} ({d}%)' },
        series: [{
            type: 'pie',
            data: [...pie_data]
        }]
    }
}/>
```

```svelte
<ECharts config={
    {
        tooltip: { formatter: '{b}: {c} ({d}%)' },
        series: [{
            type: 'pie',
            radius: ['40%', '70%'],  // donut
            data: [...donut_data]
        }]
    }
}/>
```

For complex configs, define the options object in a `<script>` tag and reference it:

```html
<script>
let options = {
    title: { text: 'My Chart' },
    series: [{ type: 'treemap', data: [...my_data] }]
};
</script>

<ECharts config={options} />
```

---

## Full Prop Reference

### Props common to most charts

| Prop | Type | Default | Charts |
|---|---|---|---|
| `data` | query name | required | all |
| `x` | column name | varies | most |
| `y` | column name or array | varies | most |
| `series` | column name | — | Line, Bar, Area, Scatter, Bubble |
| `sort` | boolean | `true` | most |
| `title` | string | — | all |
| `subtitle` | string | — | all |
| `legend` | boolean | `true` for multi-series | all |
| `chartAreaHeight` | number | `180` | most |
| `renderer` | `canvas` \| `svg` | `canvas` | most |
| `downloadableData` | boolean | `true` | most |
| `downloadableImage` | boolean | `true` | most |
| `emptySet` | `error` \| `warn` \| `pass` | `error` | all |
| `emptyMessage` | string | `"No records"` | all |
| `colorPalette` | array of colors | built-in | most |
| `seriesColors` | `{{"Name": "color"}}` | — | most |
| `seriesOrder` | array of series names | data order | most |
| `echartsOptions` | object | — | most |
| `seriesOptions` | object | — | most |
| `printEchartsConfig` | boolean | `false` | most |
| `connectGroup` | string | — | most |

### Formatting props

| Prop | Description |
|---|---|
| `xFmt` | Format for x-axis values |
| `yFmt` | Format for y-axis values |
| `y2Fmt` | Format for secondary y-axis |
| `seriesLabelFmt` | Format for series labels in legend |
| `valueFmt` | Format for value column (Heatmap, CalendarHeatmap, FunnelChart, SankeyDiagram) |
| `labelFmt` | Format for data labels shown on chart |

**Common format strings:** `usd`, `usd0`, `usd0k`, `usd1k`, `pct0`, `pct1`, `num0`, `num0k`, `mmm` (month abbrev), `mmm d` (month + day)

### Axis control props (Line, Bar, Area, Scatter, Bubble, BoxPlot)

| Prop | Type | Default |
|---|---|---|
| `yLog` | boolean | `false` |
| `yLogBase` | number | `10` |
| `yMin` / `yMax` | number | — |
| `yScale` | boolean | `false` |
| `y2Min` / `y2Max` | number | — |
| `y2Scale` | boolean | `false` |
| `xAxisTitle` | boolean or string | `false` (`true` for Scatter/Bubble) |
| `yAxisTitle` | boolean or string | `false` (`true` for Scatter/Bubble) |
| `xGridlines` | boolean | `false` |
| `yGridlines` | boolean | `true` |
| `xAxisLabels` | boolean | `true` |
| `yAxisLabels` | boolean | `true` |
| `xBaseline` | boolean | `true` |
| `yBaseline` | boolean | `false` |
| `xTickMarks` | boolean | `false` |
| `yTickMarks` | boolean | `false` |
| `swapXY` | boolean | `false` |
| `xLabelWrap` | boolean | `false` |
| `leftPadding` | number | — |
| `rightPadding` | number | — |

### Value label props (Line, Bar, Area)

| Prop | Type | Default |
|---|---|---|
| `labels` | boolean | `false` |
| `labelSize` | number | `11` |
| `labelPosition` | varies by chart | varies |
| `labelColor` | color | auto |
| `labelFmt` | format string | same as y |
| `showAllLabels` | boolean | `false` |

### LineChart-specific props

| Prop | Type | Default |
|---|---|---|
| `step` | boolean | `false` |
| `stepPosition` | `start` \| `middle` \| `end` | `end` |
| `lineColor` | color | — |
| `lineOpacity` | 0–1 | `1` |
| `lineType` | `solid` \| `dashed` \| `dotted` | `solid` |
| `lineWidth` | number | `2` |
| `markers` | boolean | `false` |
| `markerShape` | `circle` \| `emptyCircle` \| `rect` \| `triangle` \| `diamond` | `circle` |
| `markerSize` | number | `8` |
| `handleMissing` | `gap` \| `connect` \| `zero` | `gap` |
| `y2SeriesType` | `line` \| `bar` \| `scatter` | `line` |

### BarChart-specific props

| Prop | Type | Default |
|---|---|---|
| `type` | `stacked` \| `grouped` \| `stacked100` | `stacked` |
| `stackName` | string | — |
| `fillColor` | color | — |
| `fillOpacity` | 0–1 | `1` |
| `outlineWidth` | number | `0` |
| `outlineColor` | color | — |
| `stackTotalLabel` | boolean | `true` |
| `seriesLabels` | boolean | `true` |
| `y2SeriesType` | `bar` \| `line` \| `scatter` | `bar` |
| `yAxisColor` | boolean or color | `true` when y2 used |

### AreaChart-specific props

| Prop | Type | Default |
|---|---|---|
| `type` | `stacked` \| `stacked100` | `stacked` |
| `step` | boolean | `false` |
| `stepPosition` | `start` \| `middle` \| `end` | `end` |
| `fillColor` | color | — |
| `lineColor` | color | — |
| `fillOpacity` | 0–1 | `0.7` |
| `line` | boolean | `true` |
| `handleMissing` | `gap` \| `connect` \| `zero` | `gap` / `zero` |

### ScatterPlot-specific props

| Prop | Type | Default |
|---|---|---|
| `shape` | `circle` \| `emptyCircle` \| `rect` \| `triangle` \| `diamond` | `circle` |
| `pointSize` | number | `10` |
| `opacity` | 0–1 | `0.7` |
| `fillColor` | color | — |
| `outlineWidth` | number | `0` |
| `outlineColor` | color | — |
| `tooltipTitle` | column name | — |
| `xMin` / `xMax` | number | — |

### BubbleChart-specific props

| Prop | Type | Default |
|---|---|---|
| `size` | column name | required |
| `sizeFmt` | format string | — |
| `scaleTo` | number | `1` |
| `opacity` | 0–1 | `0.7` |
| `shape` | shape string | `circle` |
| `tooltipTitle` | column name | — |

### BoxPlot-specific props

| Prop | Type | Default |
|---|---|---|
| `name` | column name | required |
| `midpoint` | column name | required |
| `intervalBottom` | column name | — |
| `intervalTop` | column name | — |
| `confidenceInterval` | column name | — |
| `min` | column name | — |
| `max` | column name | — |
| `color` | column name | — |
| `swapXY` | boolean | `false` |

### Sparkline-specific props

| Prop | Type | Default |
|---|---|---|
| `dateCol` | column name | required |
| `valueCol` | column name | required |
| `type` | `line` \| `area` \| `bar` | `line` |
| `color` | color | — |
| `valueFmt` | format | — |
| `dateFmt` | format | — |
| `height` | number | `15` |
| `width` | number | `50` |
| `interactive` | boolean | `true` |

### SankeyDiagram-specific props

| Prop | Type | Default |
|---|---|---|
| `sourceCol` | column name | required |
| `targetCol` | column name | required |
| `valueCol` | column name | required |
| `percentCol` | column name | — |
| `valueFmt` | format string | — |
| `orient` | `horizontal` \| `vertical` | `horizontal` |
| `nodeLabels` | `name` \| `value` \| `full` | `name` |
| `linkLabels` | `full` \| `value` \| `percent` | `full` |
| `linkColor` | `base-content-muted` \| `source` \| `target` \| `gradient` | `base-content-muted` |
| `nodeAlign` | `justify` \| `left` \| `right` | `justify` |
| `nodeGap` | number | `8` |
| `nodeWidth` | number | `20` |
| `depthOverride` | `{{"node": depth}}` | — |
| `sort` | boolean | `false` |

### Heatmap-specific props

| Prop | Type | Default |
|---|---|---|
| `value` | column name | required |
| `valueFmt` | format string | — |
| `colorScale` | array of colors | built-in |
| `min` / `max` | number | data min/max |
| `nullsZero` | boolean | `true` |
| `zeroDisplay` | string | — |
| `valueLabels` | boolean | `true` |
| `mobileValueLabels` | boolean | `false` |
| `cellHeight` | number | `30` |
| `borders` | boolean | `true` |
| `xLabelRotation` | number | `0` |
| `xAxisPosition` | `top` \| `bottom` | `top` |
| `xSort` / `ySort` | column name | — |
| `xSortOrder` / `ySortOrder` | `asc` \| `desc` | `asc` |
| `filter` | boolean | `false` |

### CalendarHeatmap-specific props

| Prop | Type | Default |
|---|---|---|
| `date` | column name | required |
| `value` | column name | required |
| `valueFmt` | format string | — |
| `colorScale` | array of colors | built-in |
| `min` / `max` | number | data min/max |
| `yearLabel` | boolean | `true` |
| `monthLabel` | boolean | `true` |
| `dayLabel` | boolean | `true` |
| `filter` | boolean | `false` |

### FunnelChart-specific props

| Prop | Type | Default |
|---|---|---|
| `nameCol` | column name | required |
| `valueCol` | column name | required |
| `valueFmt` | format string | — |
| `showPercent` | boolean | `false` |
| `funnelSort` | `none` \| `ascending` \| `descending` | `none` |
| `funnelAlign` | `left` \| `right` \| `center` | `center` |
| `labelPosition` | `left` \| `right` \| `inside` | `inside` |
| `outlineColor` | color | transparent |
| `outlineWidth` | number | `1` |

### ReferenceLine props

| Prop | Description |
|---|---|
| `x` / `y` | Inline coordinate or dataset column for line position |
| `x2` / `y2` | Endpoint for sloped lines |
| `label` | Text or column name |
| `hideValue` | boolean — remove value from label |
| `color` | Semantic or hex color |
| `lineColor` | Override just the line color |
| `lineType` | `solid` \| `dashed` \| `dotted` (default `dashed`) |
| `lineWidth` | number (default `1.3`) |
| `labelPosition` | `aboveStart`/`aboveCenter`/`aboveEnd`/`belowStart`/`belowCenter`/`belowEnd` |
| `symbolStart` / `symbolEnd` | Shape at line endpoints |
| `bold` / `italic` | Label text formatting |

### ReferenceArea props

| Prop | Description |
|---|---|
| `xMin` / `xMax` | X-axis bounds (inline value or column name) |
| `yMin` / `yMax` | Y-axis bounds |
| `label` | Text or column name |
| `color` | Semantic or hex |
| `areaColor` | Override just area color |
| `opacity` | Area fill opacity |
| `border` | boolean — render border around area |
| `borderColor` / `borderType` / `borderWidth` | Border styling |
| `labelPosition` | `topLeft`/`top`/`topRight`/`left`/`center`/`right`/`bottomLeft`/`bottom`/`bottomRight` |

### ReferencePoint / Callout props

| Prop | Description |
|---|---|
| `x` / `y` | Coordinate or column name |
| `label` | Text or column name (required) |
| `color` | Semantic or hex |
| `labelPosition` | `top`/`right`/`bottom`/`left` |
| `symbol` | `circle`/`rect`/`triangle`/`diamond`/`pin`/`arrow`/`none` |
| `symbolSize` | number (default `8`) |
| `symbolOpacity` | number |
| `symbolBorderWidth` / `symbolBorderColor` | Symbol border |
| `labelWidth` | `fit` / number |
| `bold` / `italic` | Label text formatting |
