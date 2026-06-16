---
name: evidence-core-concepts
description: Evidence.dev core concepts — SQL queries in markdown, templated pages, loops, if/else, formatting, query functions, exports, themes and the Svelte/Markdown hybrid syntax
version: 1.0.0
---

## When to use
Invoke when the user asks to:
- Create a new Evidence.dev page or report from scratch
- Understand how Evidence.dev pages, queries, and components fit together
- Start a new Evidence.dev project or understand its structure

# Evidence Core Concepts

Evidence is a code-based BI framework. You write `.md` files that mix standard Markdown, SQL queries, and Svelte-style components. Evidence compiles those files into a static web app where every chart and value is backed by real query results.

---

## Level 1 — The Mental Model

### How a Page Works

An Evidence page is a `.md` file in `pages/`. Evidence reads it top-to-bottom and does three things:

1. Runs every SQL code fence against your connected data sources.
2. Exposes each query result as a JavaScript array of row objects, named by the identifier you gave it.
3. Renders the rest of the file as HTML, substituting `{...}` expressions and `<Component />` tags with live data.

The URL for `pages/sales/monthly.md` is `/sales/monthly`. The homepage is `pages/index.md`.

### Writing a Query

A SQL query is just a fenced code block with the language set to `sql` and a name immediately after it:

````markdown
```sql orders_by_month
select
    date_trunc('month', order_datetime) as order_month,
    count(*) as number_of_orders,
    sum(sales) as sales_usd
from needful_things.orders
group by 1
order by 1 desc
```
````

The name (`orders_by_month`) becomes a variable. After the query runs, that variable holds an array of row objects — one object per row, one property per column.

### Using Query Results in Components

Pass the query name to a component using the `data` prop wrapped in curly braces:

```markdown
<LineChart
    data={orders_by_month}
    x=order_month
    y=sales_usd
    title="Sales by Month"
/>
```

Curly braces tell Evidence to evaluate a JavaScript expression. Without curly braces, a prop value is treated as a plain string.

### Reading a Single Value in Text

```markdown
There were {orders_by_month[0].number_of_orders} orders last month.
```

Or use the `<Value/>` component for automatic formatting:

```markdown
There were <Value data={orders_by_month} column=number_of_orders/> orders last month.
```

### The Full Round-Trip in One File

````markdown
---
title: Monthly Sales
---

```sql orders_by_month
select
    date_trunc('month', order_datetime) as order_month,
    count(*) as number_of_orders,
    sum(sales) as sales_usd
from needful_things.orders
group by 1
order by 1 desc
```

## Sales Overview

There are {orders_by_month.length} months of data.
Last month had <Value data={orders_by_month} column=sales_usd fmt=usd0k/> in sales.

<LineChart data={orders_by_month} x=order_month y=sales_usd/>
````

---

## Level 2 — Query Patterns, Templated Pages, Loops, If/Else, Formatting

### Query Chaining

Reference another query inside SQL using `${query_name}` — Evidence inlines it as a subquery:

````markdown
```sql sales_by_item
select item, sum(sales) as sales
from needful_things.orders
group by 1
```

```sql average_sales
select avg(sales) as average_sales
from ${sales_by_item}
```
````

Order on the page doesn't matter. Circular references are detected and flagged as errors. Some databases (Postgres, MySQL) require you to alias the subquery: `from ${sales_by_item} as sales_by_item`.

### SQL File Queries

For queries shared across multiple pages, put them in `queries/` and reference them in frontmatter:

```yaml
---
queries:
  - q4_data: my_file_query.sql
  - some_category/my_category_file_query.sql
---
```

If you omit the alias, the filename becomes the variable name (slashes become underscores).

### Query Parameters from Inputs

Queries can react to user inputs (dropdowns, text boxes, etc.) via `inputs`:

````markdown
```sql orders_by_month
select
    date_trunc('month', order_date) as month,
    sum(sales) as sales_usd
from needful_things.orders
where item = '${inputs.selected_item.value}'
group by 1
```
````

For templated pages, use `params` instead of `inputs` (see below).

### Filters — Linking an Input to a Query

````markdown
```sql unique_items
select item from needful_things.orders group by 1
```

<Dropdown name=selected_item data={unique_items} value=item/>

```sql orders_filtered
select
    date_trunc('month', order_date) as month,
    sum(sales) as sales_usd
from needful_things.orders
where item = '${inputs.selected_item.value}'
group by 1
```

<BarChart data={orders_filtered} x=month y=sales_usd/>
````

Use `%` as a wildcard with `like` to create an "All Items" default option:

```markdown
<Dropdown name=selected_item data={unique_items} value=item>
    <DropdownOption value="%" valueLabel="All Items"/>
</Dropdown>
```

### Templated Pages

Create one file that generates a page per row in a query. Name the file with square brackets:

```
pages/customers/[customer].md
```

The string inside the brackets is a URL parameter available as `{params.customer}` in the file.

Use `params` in SQL to filter for the current page's value:

````markdown
```sql customer_data
select sum(sales) as sales_usd
from needful_things.orders
where first_name = '${params.customer}'
group by 1
```

# {params.customer}

<Value data={customer_data} column=sales_usd/> in total sales.
````

Pages are only built if they are linked to. Generate links from an index page:

````markdown
```sql customers
select
    first_name,
    '/customers/' || first_name as customer_link,
    sum(sales) as sales_usd
from needful_things.orders
group by 1
```

<DataTable data={customers} link=customer_link/>
````

Nesting works too — `pages/customers/[customer]/[branch].md` gives you `params.customer` and `params.branch`.

### Loops

`{#each}` iterates over query rows, letting you generate repeated sections:

```markdown
{#each orders_by_month as month}

## {month.order_month}

<Value data={month} column=number_of_orders/> orders,
<Value data={month} column=sales_usd fmt=usd0k/> in sales.

{/each}
```

Each iteration exposes the current row as the alias (`month` above). Access columns with dot notation.

### If / Else

Control rendered content based on data conditions:

```javascript
{#if orders_by_month[0].sales_usd > orders_by_month[1].sales_usd}

Sales are up month-over-month.

{:else if orders_by_month[0].sales_usd === orders_by_month[1].sales_usd}

Sales are flat.

{:else}

Sales are down vs last month.

{/if}
```

Common pattern — hide a table when empty:

```javascript
{#if query_name.length !== 0}
<DataTable data={query_name}/>
{/if}
```

### Value Formatting

Apply formats via the `fmt` prop on any component that renders a value:

```markdown
<Value data={sales_data} column=sales fmt='$#,##0'/>

<LineChart data={sales_data} x=date y=sales xFmt="m/d" yFmt="usd0k"/>
```

**Built-in format tags** (most common):

| Tag | Example output |
|---|---|
| `usd` | $412 (auto) |
| `usd0` / `usd1` / `usd2` | $7,043 / $7,043.1 / $7,043.12 |
| `usd0k` / `usd1m` | $64k / $4.6M |
| `num0` / `num1` / `num2` | 11 / 11.2 / 11.23 |
| `pct0` / `pct1` / `pct2` | 73% / 73.1% / 73.10% |
| `shortdate` | Jan 9/22 |
| `longdate` | January 9, 2022 |
| `eur`, `gbp`, `aud` | same pattern as usd |

Currency tags follow the pattern `{currency_code}{decimal_places}{magnitude}` — e.g. `aud2k`, `eur1m`.

**SQL format tags** — append the format name to the column name with an underscore so the column is always formatted wherever it appears:

```sql
select
    sum(sales) as sales_usd,
    avg(margin) as margin_pct
from orders
```

**Format function** for inline expressions where you cannot use a component:

```javascript
Sales delta: {fmt(sales_per_year[0].total_sales - sales_per_year[1].total_sales, '+#,##0;-#,##0')}
```

**Custom formats** are defined in Evidence Settings (Value Formatting section) and then referenced by name anywhere `fmt` is accepted.

### Page Variables

Access information about the current page with `{$...}` syntax:

```markdown
Current path: {$page.route.id}
```

---

## Level 3 — Full Syntax Reference, Query Functions, Exports, Themes

### Full Syntax Summary

| Syntax | Purpose |
|---|---|
| ` ```sql name ` | Define and run an inline SQL query |
| `{expression}` | Evaluate any JavaScript expression |
| `{query[0].column}` | Access a specific row/column value |
| `{query.length}` | Number of rows returned |
| `<Component prop={value}/>` | Render a built-in or custom component |
| `{#each rows as row}...{/each}` | Loop over query rows |
| `{#if cond}...{:else}...{/if}` | Conditional rendering |
| `{$page.route.id}` | Page-level variable |
| `{@partial "file.md"}` | Include a reusable partial |
| `{fmt(value, code)}` | Format a value inline |

### Frontmatter Reference

Frontmatter is YAML at the top of the file, wrapped in `---`. Must appear before any content.

```yaml
---
title: My Page
description: Used by search engines
hide_title: false
hide_header: false
hide_toc: false
hide_breadcrumbs: false
full_width: false
max_width: 1280
sidebar: show         # show | hide | never
sidebar_position: 3
sidebar_link: true
og:
  title: Override link preview title
  description: Override link preview body
  image: /my-social-image.png
queries:
  - alias_name: path/to/query.sql
  - path/to/other.sql
---
```

Custom frontmatter keys are accessible as expressions: if you add `region: APAC` to frontmatter, you can write `{region}` anywhere in the page.

### Expressions in Markdown

Curly braces evaluate JavaScript anywhere in the body text:

```markdown
2 + 2 = {2 + 2}

There are {orders.length} months of data.

Last month: {orders_by_month[0].number_of_orders} orders.
```

### Components

All components take `data={query_name}` for their data source.

**Minimum viable chart:**

```markdown
<LineChart data={orders_by_month}/>
```

Evidence assumes: first column = x, remaining numeric columns = y.

**Explicit axes:**

```markdown
<BarChart
    data={orders_by_month}
    x=order_month
    y=sales_usd
    series=category
    title="Sales by Category"
/>
```

**Multiple y columns:**

```markdown
<LineChart data={my_data} y={["revenue", "cost", "profit"]}/>
```

**Annotations inside charts:**

```markdown
<LineChart data={sales_data} x=date y=sales>
    <ReferenceLine data={target_data} y=target label=name/>
</LineChart>
```

**Value in text:**

```markdown
<Value data={orders} column=num_orders fmt=num0/>
```

### Query Functions (Experimental)

Query functions let you filter and aggregate query results on the client side without writing additional SQL.

**`.where(sqlStatement)`** — filter rows:

```markdown
<DataTable data={orders.where(`sales > 100`)}/>
```

**`.limit(n)`** — cap row count:

```markdown
<DataTable data={orders.limit(10)}/>
```

**`.offset(n)`** — skip rows:

```markdown
<DataTable data={orders.offset(20)}/>
```

**`.groupBy([columns], withRowCount)`** — group:

```markdown
<DataTable data={orders.groupBy(["category", "item"])}/>
```

**`.agg({aggObj})`** — aggregate (chain with `.groupBy()`):

```markdown
<DataTable data={orders.groupBy(["category"]).agg({sum: "sales", avg: "sales"})}/>
```

Supported aggregation keys: `sum`, `avg`, `min`, `max`, `median`.

**Pattern: loop + `.where()` to split one query into per-category charts:**

````markdown
```sql categories
SELECT DISTINCT category FROM orders
```

```sql orders_by_category
SELECT category, item, sum(sales) as total_sales
FROM orders
GROUP BY ALL
```

{#each categories as cat}

### {cat.category}

<BarChart
    data={orders_by_category.where(`category = '${cat.category}'`)}
    x=item
    y=total_sales
/>

{/each}
````

### Partials

Reusable chunks of Evidence markdown stored in `./partials/`. Reference them with:

```markdown
{@partial "my-partial.md"}
```

Partials do not hot-reload in dev — refresh the browser after editing a partial.

### Exports

All export options are available in both dev and prod.

| Export | How |
|---|---|
| PDF | Top-right menu > "Export PDF". Reflects current filter/query state. |
| CSV | Hover a table or chart > "Download Data" (bottom-right). |
| PNG | Hover a chart > "Download image". |
| Copy-paste | Cmd+A / Ctrl+A selects all page content (excluding chrome). Paste into email, Docs, Word. |

### Themes

Configuration lives in `evidence.config.yaml` at the project root.

**Appearance modes:**

```yaml
appearance:
    default: system   # light | dark | system
    switcher: true    # show/hide the mode toggle in the UI
```

**Color palettes** — for series-based charts (`colorPalette` prop):

```yaml
theme:
    colorPalettes:
        default:
            light:
                - "#236aa4"
                - "#45a1bf"
            dark:
                - "#236aa4"
                - "#45a1bf"
        myBrandPalette:
            - "#e11d48"
            - "#6d28d9"
```

Use in a component:

```markdown
<BarChart data={my_data} colorPalette=myBrandPalette/>
```

**Color scales** — for continuous data (heatmaps, color-scaled columns):

```yaml
theme:
    colorScales:
        default:
            light: ["#ADD8E6", "#00008B"]
        myScale:
            - "#f97316"
            - "#ef4444"
```

**UI color tokens** — override brand, background, and semantic colors:

```yaml
theme:
    colors:
        primary: "#ef4444"           # same for light and dark
        accent:
            light: "#7c3aed"
            dark: "#a78bfa"
        myColor: "#10b981"           # custom token
```

Tokens: `primary`, `accent`, `base`, `info`, `positive`, `warning`, `negative`.

**Custom Tailwind styles** — you can use any Tailwind class on HTML elements inside markdown:

```markdown
<p class="text-red-600 italic font-serif">Custom styled text.</p>

<div class="bg-primary p-4 text-primary-content">Branded callout.</div>
```

Add `class="markdown"` to apply Evidence's default prose styles to a custom HTML element.

---

## Quick Reference Card

```
QUERY DEFINITION
  ```sql my_query
  select ...
  ```

DATA ACCESS
  {my_query.length}             — row count
  {my_query[0].column_name}     — first row, specific column
  data={my_query}               — pass all rows to a component

COMPONENTS (minimum)
  <LineChart data={q}/>
  <BarChart data={q} x=col y=col/>
  <DataTable data={q}/>
  <Value data={q} column=col/>

LOOP
  {#each query as row}
    {row.column}
  {/each}

CONDITIONAL
  {#if condition}...{:else}...{/if}

FORMAT
  fmt=usd0k  fmt=pct1  fmt=num2  fmt='$#,##0.0'
  {fmt(value, 'formatCode')}

TEMPLATE PAGE
  File: pages/entity/[param].md
  SQL:  where id = '${params.param}'
  Text: {params.param}

INPUT FILTER
  <Dropdown name=x data={q} value=col/>
  SQL:  where col = '${inputs.x.value}'

QUERY FUNCTIONS (experimental)
  data={q.where(`col > 10`)}
  data={q.limit(5)}
  data={q.groupBy(["col"]).agg({sum: "sales"})}
```

## Parallelisation
Safe — this skill is a reference. Applying it (creating .md files) is safe if agents write to different page files.
