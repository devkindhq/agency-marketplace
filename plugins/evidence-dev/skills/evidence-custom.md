---
name: evidence-custom
description: Evidence.dev custom components and plugins — creating Svelte components, component queries, plugin development and publishing
version: 1.0.0
---

# Evidence Custom Components & Plugins

## Level 1 — What are custom components, and when do you need them?

Evidence ships a built-in component library (`@evidence-dev/core-components`) that covers charts, tables, values, and common UI patterns. Components use HTML-style syntax in Markdown:

```html
<BarChart data={orders_by_month} x="order_month" y="sales_usd" />
```

**Use built-in components** for standard charts (Bar, Line, Area, Scatter, etc.), tables, `<Value>` inline text, reference lines, and annotations. These work out of the box with no extra setup.

**Build a custom component** when you need to:
- Compose multiple built-in components into a reusable block (e.g. a "KPI card" that combines a Value + sparkline)
- Add UI that Evidence does not provide (custom HTML layouts, bespoke visualisations, interactive inputs)
- Encapsulate a query + its display together (self-contained component)
- Share components across multiple Evidence projects (publish as a plugin)

Custom components are Svelte files placed in the `components/` folder at the root of your Evidence project. Evidence discovers them automatically — no registration needed for local components.

---

## Level 2 — Creating a custom component

### File structure

```
.
├── pages/
│   └── index.md
└── components/
    └── Hello.svelte
```

### Passing data via props (the basic pattern)

Define the query in the Markdown page, then pass the result to the component as a prop.

```markdown
<!-- index.md -->
```sql sales_by_country
select 'Canada' as country, 100 as sales_usd
union all select 'USA' as country, 200 as sales_usd
union all select 'UK' as country, 300 as sales_usd
```

<Hello myData={sales_by_country} />
```

```html
<!-- components/Hello.svelte -->
<script>
  export let myData;
  import { BarChart } from '@evidence-dev/core-components';
</script>

<p>Sales by country:</p>
<BarChart data={myData} />
```

Key rules:
- Use `export let propName` for every prop the component accepts
- Import any Evidence built-in components explicitly inside the `<script>` block
- The `components/` folder only supports `.svelte` files — no Markdown inside components

### Utility functions available inside custom components

All utilities are imported explicitly. Import only what you need.

**Error handling**
```javascript
import checkInputs from '@evidence-dev/component-utilities/checkInputs';
// checkInputs(data, reqCols, optCols) — throws if data empty or columns missing

import { ErrorChart } from '@evidence-dev/core-components';
// <ErrorChart error={error} chartType="My Chart" />
```

**Data manipulation**
```javascript
import getDistinctValues  from '@evidence-dev/component-utilities/getDistinctValues';   // getDistinctValues(data, column)
import getDistinctCount   from '@evidence-dev/component-utilities/getDistinctCount';    // getDistinctCount(data, column)
import getSortedData      from '@evidence-dev/component-utilities/getSortedData';       // getSortedData(data, col, isAsc)
import getColumnSummary   from '@evidence-dev/component-utilities/getColumnSummary';    // getColumnSummary(data, "object"|"array")
import getCompletedData   from '@evidence-dev/component-utilities/getCompletedData';    // fills gaps in a continuous series
```

**Formatting**
```javascript
import { formatValue } from '@evidence-dev/component-utilities/formatting';  // formatValue(value, columnFormat, columnUnitSummary)
import { fmt }         from '@evidence-dev/component-utilities/formatting';  // fmt(value, formatString) — simpler
import formatTitle     from '@evidence-dev/component-utilities/formatTitle'; // formatTitle(column, columnFormat)
```

---

## Level 3 — Component queries, plugin development, and publishing

### Component queries — self-contained data fetching

Instead of passing data from a parent page, components can run their own SQL queries. This is useful for widgets that always fetch the same data (e.g. a schema browser, a row-count badge).

#### Static queries (SQL fixed at component creation time)

```html
<!-- components/TableList.svelte -->
<script>
  import { buildQuery } from '@evidence-dev/component-utilities/buildQuery';
  import { QueryLoad }  from '@evidence-dev/core-components';

  const query = buildQuery('SELECT * FROM information_schema.tables');
</script>

<QueryLoad data={query} let:loaded={tables}>
  <svelte:fragment slot="skeleton" />

  <ul>
    {#each tables as table}
      <li>{table.table_name}</li>
    {/each}
  </ul>
</QueryLoad>
```

`QueryLoad` handles execution, loading state, and errors. The `let:loaded` directive exposes the result under the variable name you choose (prefer a descriptive name over the default `loaded`).

#### Dynamic queries (SQL changes based on user input / reactive state)

```html
<!-- components/DynamicTableList.svelte -->
<script>
  import { QueryLoad }        from '@evidence-dev/core-components';
  import { getQueryFunction } from '@evidence-dev/component-utilities/buildQuery';
  import { Query }            from '@evidence-dev/sdk/usql';

  let query;
  const queryFunction = Query.createReactive({
    execFn: getQueryFunction(),
    callback: v => query = v
  });

  let limit = 10;
  let schemaName = 'public';

  // Re-runs whenever limit or schemaName change
  $: queryFunction(`
    SELECT * FROM information_schema.tables
    WHERE table_schema = '${schemaName}'
    LIMIT ${limit}
  `);
</script>

<label>Rows: <input type="number" bind:value={limit} min={0} /></label>
<label>Schema: <input type="text" bind:value={schemaName} /></label>

<QueryLoad data={query} let:loaded={tables}>
  <svelte:fragment slot="skeleton" />
  <ul>
    {#each tables as table}
      <li>{table.table_name}</li>
    {/each}
  </ul>
</QueryLoad>
```

The `$:` reactive block is Svelte's way of declaring a statement that re-runs when its dependencies change. `Query.createReactive` wires the result back into the component via the `callback`.

#### Error slot in QueryLoad

```html
<QueryLoad data={query} let:loaded={tables}>
  <svelte:fragment slot="skeleton" />

  <svelte:fragment slot="error" let:error>
    <div class="text-red-600">
      <h3>Unable to load data</h3>
      <p>{error.message}</p>
    </div>
  </svelte:fragment>

  <!-- main content only renders when query succeeds -->
  <ul>
    {#each tables as table}
      <li>{table.table_name}</li>
    {/each}
  </ul>
</QueryLoad>
```

---

### Plugin development — sharing components across projects

A plugin is an npm package containing Svelte components. Use the [Evidence Labs repo](https://github.com/evidence-dev/labs) as a starting template.

#### Steps to create and publish a plugin

1. Clone the Labs example repo
2. Replace components in `src/lib/` with your own
3. Add demo pages under `pages/`
4. Set up component exporting (see below)
5. Test with `npm run dev`
6. Update `package.json`: set `name` to your package name, `version` to `0.0.1`
7. Publish: `npm publish` (requires an npm account)
8. To release updates, bump the version and re-run `npm publish`

#### Component exporting — Module Exports (recommended)

Add the `evidenceInclude` flag to every component you want exposed:

```html
<!-- src/lib/ComponentOne.svelte -->
<script context="module">
  export const evidenceInclude = true;
</script>
```

Create `src/lib/index.js` and re-export each component:

```javascript
// src/lib/index.js
export { default as ComponentOne } from './ComponentOne';
export { default as ComponentTwo } from './ComponentTwo';
```

#### Component exporting — Manifest (alternative, useful for large libraries)

```yaml
# src/lib/evidence.manifest.yaml
components:
  - ComponentOne
  - ComponentTwo
```

Plus the same `index.js` exports above. The manifest takes priority over module exports if both are present.

---

### Installing and registering plugins in an Evidence project

**Install**
```bash
npm install @acme/charting
```

**Register** in `evidence.config.yaml`:
```yaml
plugins:
  components:
    @evidence-dev/core-components: {}
    @acme/charting: {}
```

#### Aliases — rename a component on import

```yaml
components:
  @acme/charting:
    aliases:
      LongNameForAChart: AcmeChart   # use <AcmeChart /> in Markdown
```

#### Overrides — replace a built-in component

```yaml
components:
  @evidence-dev/core-components: {}
  @acme/charting:
    overrides:
      - LineChart   # replaces the built-in LineChart with the plugin's LineChart
```

To override with a differently named component, alias it first then override:
```yaml
  @acme/charting:
    aliases:
      CustomLineChart: LineChart
    overrides:
      - LineChart
```

#### Using a generic Svelte library (not an Evidence plugin)

```yaml
components:
  @evidence-dev/core-components: {}
  carbon-components-svelte:
    provides:
      - Button
      - CodeSnippet
```

Components must be named exports (`import { ComponentName } from 'package'`), not default exports.

---

### Data source plugins

Source plugins add new database/connector types to Evidence.

**Install and register:**
```bash
npm install @cool-new-db/evidence-source-plugin
```

```yaml
# evidence.config.yaml
plugins:
  components:
    @evidence-dev/core-components: {}
  datasources:
    @cool-new-db/evidence-source-plugin
```

After registering, restart the dev server and configure the connection at `localhost:3000/settings`.

---

### Quick reference checklist

**In the Markdown page**
- [ ] Write the SQL query block with a result name
- [ ] Pass query results to the component as props: `<MyComponent data={query_name} />`

**In the Svelte component**
- [ ] Place the file in `components/` at the project root
- [ ] Declare props with `export let propName`
- [ ] Import Evidence built-ins explicitly: `import { BarChart } from '@evidence-dev/core-components'`
- [ ] For self-contained queries, use `buildQuery` (static) or `Query.createReactive` + `getQueryFunction` (dynamic)
- [ ] Wrap query results in `<QueryLoad>` to handle loading and error states

**When publishing as a plugin**
- [ ] Flag each component with `export const evidenceInclude = true` in a `context="module"` script block
- [ ] Export all components from `src/lib/index.js`
- [ ] Set package name and version in `package.json` before `npm publish`
