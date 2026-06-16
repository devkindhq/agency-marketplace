---
name: evidence-inputs
description: Evidence.dev input components for filtering — Dropdown, TextInput, Checkbox, DateInput, DateRange, Slider, ButtonGroup, DimensionGrid with query integration patterns
version: 1.0.0
---

## When to use
Invoke when the user asks to:
- Add a filter, dropdown, date picker, or search box to a page
- Make a page interactive or let users filter the displayed data
- Use DateRange, Dropdown, TextInput, ButtonGroup, or Slider components

# Evidence Input Components

## Level 1 — What each input does, minimal syntax, and the variable it creates

All inputs expose their value via the `inputs` object in SQL and markdown. The variable name is whatever you pass to `name=`.

### Dropdown
Lets users pick one or many values from a list. Options can come from a query or be hardcoded.

```markdown
<Dropdown name=my_filter data={query} value=column_name />
```

Variable: `{inputs.my_filter.value}` — single string, or comma-separated list when `multiple=true`

---

### TextInput
A freeform text box for search or string filtering.

```markdown
<TextInput name=search_term />
```

Variable: `{inputs.search_term}` (no `.value` suffix needed)

---

### Checkbox
A toggleable boolean. Returns `true` or `false`.

```markdown
<Checkbox name=exclude_flag title="Exclude low values" />
```

Variable: `{inputs.exclude_flag}` — boolean `true` or `false`

---

### DateInput
A date picker. Can operate in single-date or range mode (via the `range` prop).

```markdown
<DateInput name=selected_date data={orders} dates=order_date />
```

Single-date variable: `{inputs.selected_date.value}`
Range variables: `{inputs.selected_date.start}` and `{inputs.selected_date.end}`

---

### DateRange
A dedicated date-range picker with preset options. Always produces start/end values.

```markdown
<DateRange name=date_window data={orders} dates=order_date />
```

Variables: `{inputs.date_window.start}` and `{inputs.date_window.end}`

---

### Slider
A numeric range slider. Returns the selected number.

```markdown
<Slider name=min_sales title="Min Sales" min=0 max=10000 defaultValue=500 />
```

Variable: `{inputs.min_sales}` (no `.value` suffix)

---

### ButtonGroup
Single-select button strip. Good for a small, fixed list of options.

```markdown
<ButtonGroup name=selected_category data={categories} value=category />
```

Variable: `{inputs.selected_category}` (no `.value` suffix)

---

### DimensionGrid
An interactive grid of dimension tables — one per string column in the source query. Produces a SQL condition fragment suitable for direct use in a `WHERE` clause.

```markdown
<DimensionGrid data={orders} name=dimension_filter metric='sum(sales)' />
```

Variable: `${inputs.dimension_filter}` — emits a SQL boolean expression like `category = 'Toys' and state = 'CA'`, or `true` when nothing is selected.

---

## Level 2 — Common props and practical filter examples

### How inputs connect to queries

Wrap input variables inside `${}` in your SQL code blocks. The query re-runs automatically when the input changes.

**Single-value equality (Dropdown / ButtonGroup / TextInput)**

```sql filtered_orders
select * from orders
where item = '${inputs.selected_item.value}'
```

**LIKE pattern match — useful for TextInput or a wildcard default**

```sql filtered_orders
select * from orders
where item like '${inputs.search_term}'
```

**Multi-select IN clause (Dropdown with multiple=true)**
Use `IN` and omit quotes around `${}`:

```sql filtered_orders
select * from orders
where category in ${inputs.category_filter.value}
```

**Date range filter (DateRange or DateInput with range)**

```sql filtered_orders
select * from orders
where order_date between '${inputs.date_window.start}' and '${inputs.date_window.end}'
```

**Single date threshold (DateInput)**

```sql filtered_orders
select * from orders
where order_date > '${inputs.cutoff_date.value}'
```

**Numeric threshold (Slider)**

```sql filtered_orders
select * from orders
where sales >= ${inputs.min_sales}
```

**Boolean flag (Checkbox)**

```sql filtered_orders
select * from orders
where not ${inputs.exclude_low_value}
    or (${inputs.exclude_low_value} and sales >= 10)
```

**DimensionGrid passthrough**
DimensionGrid outputs a ready-made SQL fragment — use it without quotes:

```sql filtered_orders
select * from orders
where ${inputs.dimension_filter}
```

---

### Common props shared by most inputs

| Prop | Applies to | Purpose |
|---|---|---|
| `name` | all | **Required.** Identifier used in `inputs.name` |
| `title` | all | Label displayed above the control |
| `defaultValue` | most | Initial value on page load |
| `description` | all | Tooltip shown on an info icon next to the title |
| `hideDuringPrint` | most | Hides the control in print/export (default `true`) |

---

### Dropdown — practical examples

**Query-populated with a default and title**

```markdown
<Dropdown
    data={categories}
    name=cat_filter
    value=category_name
    title="Category"
    defaultValue="Sinister Toys"
/>
```

**Multi-select with pre-selected defaults**

```markdown
<Dropdown
    data={categories}
    name=cat_filter
    value=category_name
    multiple=true
    defaultValue={['Sinister Toys', 'Odd Equipment']}
/>
```

Use `in ${inputs.cat_filter.value}` (no quotes) in your SQL.

**"All items" wildcard via DropdownOption + LIKE**

```markdown
<Dropdown name=item_filter data={items} value=item>
    <DropdownOption value="%" valueLabel="All Items" />
</Dropdown>
```

```sql
where item like '${inputs.item_filter.value}'
```

**Hardcoded options**

```markdown
<Dropdown name=status_filter>
    <DropdownOption value="active" valueLabel="Active" />
    <DropdownOption value="inactive" valueLabel="Inactive" />
</Dropdown>
```

---

### TextInput — fuzzy search

`TextInput` supports fuzzy (Damerau-Levenshtein) search via a helper syntax:

```sql fuzzy_results
select * from customers
order by {inputs.name_search.search('customer_name')}
limit 10
```

This is different from a `like` filter — it ranks results by similarity rather than filtering them out.

---

### DateInput — preset range defaults

When using `range` mode, you can give a preset as the default:

```markdown
<DateInput
    name=date_picker
    range
    defaultValue={'Last 30 Days'}
/>
```

Available presets: `'Last 7 Days'` `'Last 30 Days'` `'Last 90 Days'` `'Last 3 Months'` `'Last 6 Months'` `'Last 12 Months'` `'Last Month'` `'Last Year'` `'Month to Date'` `'Year to Date'` `'All Time'`

---

### ButtonGroup — style as tabs

```markdown
<ButtonGroup name=view_mode data={options} value=option display=tabs />
```

Hardcoded with a default:

```markdown
<ButtonGroup name=period>
    <ButtonGroupItem value="daily" valueLabel="Daily" />
    <ButtonGroupItem value="weekly" valueLabel="Weekly" default />
    <ButtonGroupItem value="monthly" valueLabel="Monthly" />
</ButtonGroup>
```

---

## Level 3 — Full prop reference tables and combining inputs

### Dropdown

| Prop | Required | Type | Default | Notes |
|---|---|---|---|---|
| `name` | yes | string | — | Reference as `inputs.name.value` |
| `data` | no | query ref | — | Query providing options |
| `value` | no | column name | — | Column used as the option value |
| `label` | no | column name | same as `value` | Column used as display label |
| `multiple` | no | boolean | `false` | Enables multi-select; use `IN` in SQL |
| `defaultValue` | no | string or array | — | Array form: `{['A', 'B']}` |
| `selectAllByDefault` | no | boolean | `false` | Selects all options; requires `multiple=true` |
| `noDefault` | no | boolean | `false` | Prevents any default selection |
| `disableSelectAll` | no | boolean | `false` | Removes the "Select all" button |
| `title` | no | string | — | Label above the dropdown |
| `order` | no | string | asc by value | e.g. `category desc` |
| `where` | no | SQL fragment | — | Filters the options list itself |
| `description` | no | string | — | Tooltip text |
| `hideDuringPrint` | no | boolean | `true` | |

**DropdownOption** (for hardcoded options inside `<Dropdown>`):

| Prop | Required | Notes |
|---|---|---|
| `value` | yes | The value passed to the query |
| `valueLabel` | no | Display text; defaults to `value` |

---

### TextInput

| Prop | Required | Type | Default | Notes |
|---|---|---|---|---|
| `name` | yes | string | — | Reference as `inputs.name` or `inputs.name.search('col')` |
| `title` | no | string | — | |
| `placeholder` | no | string | `"Type to search"` | |
| `defaultValue` | no | string | — | Pre-filled text |
| `description` | no | string | — | |
| `hideDuringPrint` | no | boolean | `true` | |

---

### Checkbox

| Prop | Required | Type | Default | Notes |
|---|---|---|---|---|
| `name` | yes | string | — | Reference as `inputs.name` |
| `title` | no | string | — | Label next to the box |
| `checked` | no | boolean | `false` | Initial checked state |
| `description` | no | string | — | |

---

### DateInput

| Prop | Required | Type | Default | Notes |
|---|---|---|---|---|
| `name` | yes | string | — | Single: `inputs.name.value`; range: `inputs.name.start` / `inputs.name.end` |
| `range` | no | boolean | `false` | Switch to range-picker mode |
| `data` | no | query ref | — | Query to populate calendar bounds |
| `dates` | no | column name | — | Date column in `data` query |
| `start` | no | YYYY-MM-DD | — | Manual lower bound |
| `end` | no | YYYY-MM-DD | — | Manual upper bound |
| `title` | no | string | — | |
| `presetRanges` | no | string or array | — | Limits which presets appear in the dropdown |
| `defaultValue` | no | preset string | — | e.g. `{'Last 7 Days'}` |
| `description` | no | string | — | |
| `hideDuringPrint` | no | boolean | `true` | |

---

### DateRange

| Prop | Required | Type | Default | Notes |
|---|---|---|---|---|
| `name` | yes | string | — | Reference as `inputs.name.start` and `inputs.name.end` |
| `data` | no | query ref | — | Query to set calendar bounds |
| `dates` | no | column name | — | Date column in `data` query |
| `start` | no | YYYY-MM-DD | — | Manual lower bound |
| `end` | no | YYYY-MM-DD | — | Manual upper bound |
| `title` | no | string | — | |
| `presetRanges` | no | string or array | — | Restrict visible presets |
| `defaultValue` | no | preset string | — | e.g. `{'Year to Date'}` |
| `description` | no | string | — | |
| `hideDuringPrint` | no | boolean | `true` | |

Available preset strings for both date components: `'Last 7 Days'` `'Last 30 Days'` `'Last 90 Days'` `'Last 365 Days'` `'Last 3 Months'` `'Last 6 Months'` `'Last 12 Months'` `'Last Month'` `'Last Year'` `'Month to Date'` `'Month to Today'` `'Year to Date'` `'Year to Today'` `'All Time'`

---

### Slider

| Prop | Required | Type | Default | Notes |
|---|---|---|---|---|
| `name` | yes | string | — | Reference as `inputs.name` |
| `min` | no | number | `0` | |
| `max` | no | number | `100` | Must be greater than `min` |
| `step` | no | number | `1` | Increment size |
| `defaultValue` | no | number or column name | — | Initial position |
| `data` | no | query ref | — | Query for dynamic bounds |
| `range` | no | column name | — | Sets min and max from column min/max |
| `minColumn` | no | column name | — | First row value used as `min` |
| `maxColumn` | no | column name | — | First row value used as `max` |
| `size` | no | `small` `medium` `large` `full` | `small` | Visual width |
| `showMinMax` | no | boolean | `true` | Show min/max labels |
| `showInput` | no | boolean | `false` | Show a numeric text input beside the slider |
| `debounceDelay` | no | number (ms) | `0` | Delay before query re-runs |
| `fmt` | no | format string | — | Evidence format code (e.g. `usd0`, `#,##0`) |
| `description` | no | string | — | |
| `hideDuringPrint` | no | boolean | `true` | |

---

### ButtonGroup

| Prop | Required | Type | Default | Notes |
|---|---|---|---|---|
| `name` | yes | string | — | Reference as `inputs.name` |
| `data` | no | query ref | — | Query providing options |
| `value` | no | column name | — | Column used as option value |
| `label` | no | column name | same as `value` | Column used as display label |
| `title` | no | string | — | |
| `defaultValue` | no | string | — | Must match a value in the list |
| `order` | no | column name | query order | Sort column |
| `where` | no | SQL fragment | — | Filters the options list |
| `display` | no | `buttons` `tabs` | `buttons` | Visual style |
| `preset` | no | `dates` | — | Built-in date preset options |
| `description` | no | string | — | |

**ButtonGroupItem** (for hardcoded options):

| Prop | Required | Notes |
|---|---|---|
| `value` | yes | |
| `valueLabel` | no | Display text; defaults to `value` |
| `default` | no | Marks this item as the default selection |
| `hideDuringPrint` | no | boolean, default `true` |

---

### DimensionGrid

| Prop | Required | Type | Default | Notes |
|---|---|---|---|---|
| `data` | yes | query ref | — | Source query; one table per string column |
| `name` | no | string | — | Reference as `${inputs.name}` in SQL `WHERE` |
| `metric` | no | SQL aggregate | `count(*)` | e.g. `'sum(sales)'` |
| `metricLabel` | no | string | — | Label for the metric column |
| `title` | no | string | — | |
| `subtitle` | no | string | — | Displayed under title |
| `fmt` | no | format string | — | Format for metric values |
| `limit` | no | number | `10` | Max rows per dimension table |
| `multiple` | no | boolean | `false` | Allow multi-row selection per column |

---

### Combining multiple inputs

All inputs on a page can be used together in a single query. Chain them in your `WHERE` clause:

```markdown
<Dropdown name=category data={categories} value=category_name title="Category" />
<DateRange name=date_range defaultValue={'Last 30 Days'} />
<Slider name=min_sales title="Min Sales ($)" min=0 max=50000 step=500 fmt="usd0" />
<TextInput name=search title="Search item name" placeholder="Type to filter..." />
```

```sql filtered_results
select
    order_date,
    category,
    item,
    sales
from orders
where category = '${inputs.category.value}'
  and order_date between '${inputs.date_range.start}' and '${inputs.date_range.end}'
  and sales >= ${inputs.min_sales}
  and item like '%${inputs.search}%'
```

**Key rules when combining:**
- Dropdown single-select and ButtonGroup: use `= '${inputs.name.value}'` (quoted)
- Dropdown multi-select: use `in ${inputs.name.value}` (no quotes, no parentheses — Evidence handles them)
- TextInput direct match: quoted `'${inputs.name}'`; fuzzy: `order by {inputs.name.search('col')}`
- DateInput / DateRange: always quoted `'${inputs.name.start}'`
- Slider / Checkbox: never quoted — they emit numbers and booleans
- DimensionGrid: never quoted — it emits a complete SQL expression

**Referencing values in markdown text** (outside SQL):

```markdown
Showing {inputs.category.value} orders from {inputs.date_range.start} to {inputs.date_range.end}
with sales above {inputs.min_sales}
```

## Parallelisation
Safe — writes only to .md page files.
