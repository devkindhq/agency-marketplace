---
name: evidence-data-components
description: Evidence.dev data display components — BigValue, DataTable, Delta, Value for showing metrics, tables and formatted values
version: 1.0.0
---

## When to use
Invoke when the user asks to:
- Add a data table, metric card, or delta indicator to a page
- Display a single value, KPI, or change metric
- Use BigValue, DataTable, Delta, or Value components

# Evidence Data Display Components

## Quick Reference

| Component  | Purpose                                         | Required props          |
|------------|-------------------------------------------------|-------------------------|
| `BigValue`  | Large standalone metric card with optional sparkline and comparison | `data`, `value` |
| `DataTable` | Paginated, sortable, searchable data table      | `data`                  |
| `Delta`     | Inline up/down change indicator                 | `data`                  |
| `Value`     | Single formatted value embedded in prose text   | `data`                  |

All components accept a query result via `data={query_name}` (curly braces required).

---

## BigValue

Displays a large metric value in a card. Multiple `BigValue` components placed adjacently auto-align into a row.

**Minimal syntax**

```markdown
<BigValue data={orders} value=num_orders />
```

**Common props**

| Prop              | Type                              | Default                    | Notes                              |
|-------------------|-----------------------------------|----------------------------|------------------------------------|
| `data`            | query name                        | required                   |                                    |
| `value`           | column name                       | required                   | Column supplying the main metric   |
| `title`           | string                            | column name                | Card heading                       |
| `fmt`             | format code                       | —                          | e.g. `usd0`, `pct1`, Excel codes   |
| `comparison`      | column name                       | —                          | Column for the delta value         |
| `comparisonTitle` | string                            | comparison column name     | Label shown next to the delta      |
| `comparisonFmt`   | format code                       | —                          | Format for the comparison value    |
| `comparisonDelta` | true \| false                     | `true`                     | Show arrow + color on comparison   |
| `sparkline`       | column name                       | —                          | Date column to drive the sparkline |
| `link`            | URL string                        | —                          | Makes the entire card clickable    |

**Example — metric card with MoM comparison**

```markdown
<BigValue
  data={orders_with_comparisons}
  value=num_orders
  title="Orders"
  comparison=order_growth
  comparisonFmt=pct1
  comparisonTitle="vs. Last Month"
/>
```

**Example — metric card with sparkline**

```markdown
<BigValue
  data={orders_with_comparisons}
  value=sales
  fmt=usd0
  sparkline=month
  comparison=sales_growth
  comparisonFmt=pct1
  comparisonTitle="MoM"
/>
```

**Example — non-delta comparison (just shows the raw prior value)**

```markdown
<BigValue
  data={orders_with_comparisons}
  value=num_orders
  comparison=prev_month_orders
  comparisonTitle="Last Month"
  comparisonDelta=false
/>
```

### Full BigValue prop reference

**Data props**

| Prop           | Options                                    | Default    |
|----------------|--------------------------------------------|------------|
| `data`         | query name                                 | required   |
| `value`        | column name                                | required   |
| `title`        | string                                     | column name|
| `fmt`          | Excel format \| built-in format            | —          |
| `minWidth`     | % or px value                              | `18%`      |
| `maxWidth`     | % or px value                              | —          |
| `link`         | URL string                                 | —          |
| `emptySet`     | `error` \| `warn` \| `pass`               | `error`    |
| `emptyMessage` | string                                     | `No records`|

**Comparison props**

| Prop              | Options                  | Default        |
|-------------------|--------------------------|----------------|
| `comparison`      | column name              | —              |
| `comparisonTitle` | string                   | column name    |
| `comparisonFmt`   | format code              | —              |
| `comparisonDelta` | `true` \| `false`        | `true`         |
| `downIsGood`      | `true` \| `false`        | `false`        |
| `neutralMin`      | number                   | `0`            |
| `neutralMax`      | number                   | `0`            |

**Sparkline props**

| Prop               | Options                         | Default            |
|--------------------|---------------------------------|--------------------|
| `sparkline`        | column name (date column)       | —                  |
| `sparklineType`    | `line` \| `area` \| `bar`      | `line`             |
| `sparklineColor`   | CSS name \| hex \| RGB \| HSL  | —                  |
| `sparklineYScale`  | `true` \| `false`               | `false`            |
| `sparklineValueFmt`| format code                     | same as `fmt`      |
| `sparklineDateFmt` | format code                     | `YYYY-MM-DD`       |
| `connectGroup`     | string                          | —                  |
| `description`      | string                          | —                  |

---

## DataTable

Displays a richly formatted, paginated table. Without any `Column` children it renders all query columns automatically.

**Minimal syntax**

```svelte
<DataTable data={orders} />
```

**With explicit columns**

```svelte
<DataTable data={orders} search=true sort="sales desc">
  <Column id=category />
  <Column id=item />
  <Column id=sales fmt=usd />
</DataTable>
```

**Example — total row with weighted mean**

```svelte
<DataTable data={countries} totalRow=true rows=5>
  <Column id=country />
  <Column id=gdp_usd totalAgg=sum />
  <Column id=gdp_growth totalAgg=weightedMean weightCol=gdp_usd fmt=pct2 />
  <Column id=population totalAgg=mean fmt='#,##0"M"' />
</DataTable>
```

**Example — grouped accordion with subtotals**

```svelte
<DataTable data={orders} groupBy=state subtotals=true totalRow=true>
  <Column id=state />
  <Column id=category totalAgg="" />
  <Column id=orders />
  <Column id=sales fmt=usd />
  <Column id=growth contentType=delta fmt=pct1 totalAgg=weightedMean weightCol=sales />
</DataTable>
```

**Example — color scale + delta + sparkline columns**

```svelte
<DataTable data={categories}>
  <Column id=category />
  <Column id=value_usd contentType=colorscale colorScale=positive />
  <Column id=yoy contentType=delta fmt=pct1 title="Y/Y Chg" />
  <Column id=sales contentType=sparkline sparkX=date sparkY=sales />
</DataTable>
```

### Full DataTable prop reference

**Table-level props**

| Prop                | Options                       | Default      |
|---------------------|-------------------------------|--------------|
| `data`              | query name                    | required     |
| `rows`              | number \| `all`               | `10`         |
| `title`             | string                        | —            |
| `subtitle`          | string                        | —            |
| `search`            | `true` \| `false`             | `false`      |
| `sort`              | `column asc` \| `column desc` | —            |
| `sortable`          | `true` \| `false`             | `true`       |
| `totalRow`          | `true` \| `false`             | `false`      |
| `totalRowColor`     | hex \| css color name         | —            |
| `totalFontColor`    | hex \| css color name         | —            |
| `rowNumbers`        | `true` \| `false`             | `false`      |
| `rowLines`          | `true` \| `false`             | `true`       |
| `rowShading`        | `true` \| `false`             | `false`      |
| `backgroundColor`   | hex \| css color name         | —            |
| `headerColor`       | hex \| css color name         | —            |
| `headerFontColor`   | hex \| css color name         | —            |
| `compact`           | `true` \| `false`             | `false`      |
| `wrapTitles`        | `true` \| `false`             | `false`      |
| `formatColumnTitles`| `true` \| `false`             | `true`       |
| `downloadable`      | `true` \| `false`             | `true`       |
| `link`              | column name                   | —            |
| `showLinkCol`       | `true` \| `false`             | `false`      |
| `generateMarkdown`  | `true` \| `false`             | `false`      |
| `emptySet`          | `error` \| `warn` \| `pass`  | `error`      |
| `emptyMessage`      | string                        | `No records` |

**Grouping props**

| Prop               | Options                       | Default      |
|--------------------|-------------------------------|--------------|
| `groupBy`          | column name                   | —            |
| `groupType`        | `accordion` \| `section`      | `accordion`  |
| `subtotals`        | `true` \| `false`             | `false`      |
| `subtotalFmt`      | format code                   | —            |
| `groupsOpen`       | `true` \| `false`             | `true`       |
| `accordionRowColor`| hex \| css color name         | —            |
| `subtotalRowColor` | hex \| css color name         | —            |
| `subtotalFontColor`| hex \| css color name         | —            |
| `groupNamePosition`| `top` \| `middle` \| `bottom` | `middle`     |

### Column component

```svelte
<Column id=column_name title="Display Name" fmt=usd align=right />
```

**Base Column props**

| Prop          | Options                                                                              | Default        |
|---------------|--------------------------------------------------------------------------------------|----------------|
| `id`          | column name                                                                          | required       |
| `title`       | string                                                                               | column name    |
| `description` | string                                                                               | —              |
| `align`       | `left` \| `center` \| `right`                                                       | `left`         |
| `fmt`         | format code                                                                          | —              |
| `fmtColumn`   | column name                                                                          | —              |
| `totalAgg`    | `sum` \| `mean` \| `weightedMean` \| `median` \| `min` \| `max` \| `count` \| `countDistinct` \| custom string | `sum` |
| `totalFmt`    | format code                                                                          | —              |
| `weightCol`   | column name                                                                          | —              |
| `wrap`        | `true` \| `false`                                                                   | `false`        |
| `wrapTitle`   | `true` \| `false`                                                                   | `false`        |
| `colGroup`    | string                                                                               | —              |
| `redNegatives`| `true` \| `false`                                                                   | `false`        |
| `contentType` | `link` \| `image` \| `delta` \| `colorscale` \| `sparkline` \| `sparkarea` \| `sparkbar` \| `bar` \| `html` | — |

**contentType=delta props**

| Prop          | Options              | Default |
|---------------|----------------------|---------|
| `deltaSymbol` | `true` \| `false`   | `true`  |
| `downIsGood`  | `true` \| `false`   | `false` |
| `showValue`   | `true` \| `false`   | `true`  |
| `neutralMin`  | number               | `0`     |
| `neutralMax`  | number               | `0`     |
| `chip`        | `true` \| `false`   | `false` |

**contentType=colorscale props**

| Prop              | Options                              | Default        |
|-------------------|--------------------------------------|----------------|
| `colorScale`      | `default` \| `positive` \| `negative` \| `info` \| hex \| array of colors | `green` |
| `colorMin`        | number                               | min of column  |
| `colorMid`        | number                               | mid of column  |
| `colorMax`        | number                               | max of column  |
| `colorBreakpoints`| array of numbers                     | —              |
| `scaleColumn`     | column name                          | —              |

**contentType=sparkline / sparkarea / sparkbar props**

| Prop         | Options              | Default |
|--------------|----------------------|---------|
| `sparkX`     | column from array    | —       |
| `sparkY`     | column from array    | —       |
| `sparkYScale`| `true` \| `false`   | `false` |
| `sparkHeight`| number               | `18`    |
| `sparkWidth` | number               | `90`    |
| `sparkColor` | hex \| css color     | —       |

Sparklines require an array column built with `ARRAY_AGG({'date': date, 'value': val})` in DuckDB.

**contentType=bar props**

| Prop              | Options          | Default       |
|-------------------|------------------|---------------|
| `barColor`        | hex \| css color | —             |
| `negativeBarColor`| hex \| css color | —             |
| `hideLabels`      | `true` \| `false`| `false`       |
| `backgroundColor` | hex \| css color | `transparent` |

**contentType=link props**

| Prop           | Options                    | Default   |
|----------------|----------------------------|-----------|
| `linkLabel`    | column name \| string      | raw url   |
| `openInNewTab` | `true` \| `false`          | `false`   |

**contentType=image props**

| Prop     | Options     | Default                  |
|----------|-------------|--------------------------|
| `height` | number (px) | original image height    |
| `width`  | number (px) | original image width     |
| `alt`    | column name | filename without extension|

---

## Delta

Displays an inline colored up/down change indicator, suitable for embedding within prose or sentence-level text.

**Minimal syntax**

```markdown
Revenue is <Delta data={growth} column=revenue_growth fmt=pct1 /> vs last month.
```

**Common props**

| Prop           | Type                 | Default      |
|----------------|----------------------|--------------|
| `data`         | query name           | required     |
| `column`       | column name          | first column |
| `fmt`          | format code          | —            |
| `chip`         | `true` \| `false`   | `false`      |
| `downIsGood`   | `true` \| `false`   | `false`      |
| `neutralMin`   | number               | `0`          |
| `neutralMax`   | number               | `0`          |
| `symbolPosition`| `left` \| `right`  | `right`      |

**Example — chip style with neutral band**

```markdown
<Delta data={growth} column=neutral fmt=pct1 chip=true neutralMin=-0.02 neutralMax=0.02 />
```

**Example — inverted sentiment (down is good), symbol on left**

```markdown
<Delta data={costs} column=cost_change fmt=pct1 downIsGood=true symbolPosition=left chip=true />
```

### Full Delta prop reference

| Prop           | Options                            | Default      |
|----------------|------------------------------------|--------------|
| `data`         | query name                         | required     |
| `column`       | column name                        | first column |
| `row`          | number                             | `0`          |
| `value`        | number                             | —            |
| `fmt`          | Excel format \| built-in format    | —            |
| `downIsGood`   | `true` \| `false`                 | `false`      |
| `showSymbol`   | `true` \| `false`                 | `true`       |
| `showValue`    | `true` \| `false`                 | `true`       |
| `text`         | string                             | —            |
| `neutralMin`   | number                             | `0`          |
| `neutralMax`   | number                             | `0`          |
| `chip`         | `true` \| `false`                 | `false`      |
| `symbolPosition`| `left` \| `right`                | `right`      |
| `emptySet`     | `error` \| `warn` \| `pass`       | `error`      |
| `emptyMessage` | string                             | `No records` |

---

## Value

Displays a single formatted value from a query, inline within markdown text. Defaults to the first row of the first column.

**Minimal syntax**

```markdown
<Value data={query_name} />
```

**With column and row**

```markdown
<!-- row is zero-indexed -->
<Value data={monthly_orders} column=orders row=6 />
```

**Common props**

| Prop          | Type                 | Default      |
|---------------|----------------------|--------------|
| `data`        | query name           | required     |
| `column`      | column name          | first column |
| `row`         | number               | `0`          |
| `fmt`         | format code          | —            |
| `agg`         | `sum` \| `avg` \| `min` \| `median` \| `max` | — |
| `color`       | CSS name \| hex \| RGB \| HSL | —   |
| `placeholder` | string               | —            |

**Example — inline sentence with aggregation and formatting**

```markdown
Average order value is <Value data={orders} column=sales agg=avg fmt=usd0 />.
```

**Example — draft placeholder before the query exists**

```markdown
Revenue was <Value placeholder="$X.XM" />, up <Value placeholder="X%" /> year-over-year.
```

**Example — red negatives with custom color**

```markdown
Margin delta: <Value data={report} column=margin_delta fmt=pct1 redNegatives=true />
```

### Full Value prop reference

| Prop           | Options                                     | Default      |
|----------------|---------------------------------------------|--------------|
| `data`         | query name                                  | required*    |
| `column`       | column name                                 | first column |
| `row`          | number                                      | `0`          |
| `placeholder`  | string                                      | —            |
| `fmt`          | Excel format \| built-in format             | —            |
| `agg`          | `sum` \| `avg` \| `min` \| `median` \| `max` | —          |
| `color`        | CSS name \| hex \| RGB \| HSL              | —            |
| `redNegatives` | `true` \| `false`                          | `false`      |
| `description`  | string                                      | —            |
| `emptySet`     | `error` \| `warn` \| `pass`                | `error`      |
| `emptyMessage` | string                                      | `No records` |

*`data` is not required when `placeholder` is used.

---

## Format Codes (common)

| Code     | Example output  |
|----------|-----------------|
| `usd`    | $1,234.56       |
| `usd0`   | $1,235          |
| `usd2`   | $1,234.56       |
| `eur`    | €1,234.56       |
| `pct`    | 12.3%           |
| `pct1`   | 12.3%           |
| `pct2`   | 12.34%          |
| `num0`   | 1,235           |
| `+0.0%;-0.0%;0.0%` | +12.3% / -12.3% / 0.0% (Excel signed format) |

Full format reference: `/core-concepts/formatting`

## Parallelisation
Safe — writes only to .md page files.
