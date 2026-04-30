---
name: evidence-cli
description: Evidence.dev CLI commands, project setup, deployment configuration — dev server, build, rendering modes, environment variables, deployment platforms
version: 1.0.0
---

# Evidence CLI & Deployment

## Level 1 — The Three Commands You Need Every Day

### Create a new project

```shell
npx degit evidence-dev/template my-project
cd my-project
npm install
npm run sources
npm run dev
```

### Start the dev server (existing project)

```shell
npm run dev
```

Opens at `http://localhost:3000`. Hot reloading is on by default — save a `.md` file to see changes instantly.

### Build for production

```shell
npm run build
```

Outputs a static site to the `build/` directory. All pages and queries are pre-rendered at build time.

---

## Level 2 — All CLI Commands and Project Structure

### Full Command Reference

| Command | Description |
|---|---|
| `npx degit evidence-dev/template my-project` | Create a new project from the template |
| `npm run sources` | Extract data from sources (run before first dev or build) |
| `npm run dev` | Start the development server |
| `npm run build` | Build the app for production |
| `npm run build:strict` | Build, but fails on any query or component error |
| `npm run preview` | Preview the built site locally |
| `Ctrl/Cmd + C` | Stop the dev server |
| `r` | Restart the dev server (while running) |

Pass flags with an extra `--` separator:

```shell
npm run dev -- --port 4000
npm run dev -- --host 0.0.0.0   # useful inside containers
npm run dev -- --open /my-page  # open a specific page on startup
```

### `npm run sources` Flags

| Flag | Description |
|---|---|
| `--changed` | Only run sources whose queries have changed |
| `--sources source1,source2` | Run sources from specified sources only |
| `--queries query1,query2` | Run specific queries only |
| `--debug` | Show debug output |

### `npm run dev` Flags

| Flag | Description |
|---|---|
| `--port <port>` | Specify port (default `3000`, auto-increments if taken) |
| `--host [host]` | Specify hostname |
| `--open [path]` | Open browser to path on startup |

`dev` and `build` use Vite under the hood and support [Vite's CLI options](https://vitejs.dev/guide/cli.html#options). `preview` uses `npx serve` and supports [Serve's options](https://github.com/vercel/serve/blob/main/source/utilities/cli.ts#L30).

### Project Structure

```
my-project/
├── pages/                  # Markdown pages (.md files)
│   ├── index.md            # Home page
│   └── +layout.svelte      # Custom layout (optional override)
├── sources/                # Data source definitions
│   └── my_source/
│       ├── connection.yaml         # Non-secret connection config
│       ├── connection.options.yaml # Secret credentials (base64)
│       └── my_query.sql            # Source queries
├── static/                 # Static assets (images, favicon)
├── evidence.config.yaml    # Evidence configuration
└── package.json
```

Pages are `.md` files in `pages/`. Add a file to add a route — `pages/sales/overview.md` becomes `/sales/overview`.

### Source Queries vs Markdown Queries

- **Source queries** (`.sql` files in `sources/`) run directly against your data source in the source's SQL dialect. Run with `npm run sources`. Populate the data cache.
- **Markdown queries** (code blocks in `.md` files) use DuckDB dialect, run against the data cache on every page load. Results are directly available to components.

Reference cached data in a markdown query as `source_name.query_name`:

````markdown
```orders_summary
select * from my_source.my_query
```

<DataTable data={orders_summary} />
````

### Custom Layout

Copy the default layout to override it:

```bash
cp .evidence/template/src/pages/+layout.svelte pages
```

Key `EvidenceDefaultLayout` props:

| Prop | Default | Description |
|---|---|---|
| `title` | — | App title replacing the Evidence logo |
| `logo` | — | Image path replacing the Evidence logo |
| `lightLogo` / `darkLogo` | — | Separate logos for light/dark mode |
| `hideSidebar` | `false` | Hide sidebar navigation |
| `hideHeader` | `false` | Hide the page header |
| `hideBreadcrumbs` | `false` | Hide breadcrumbs |
| `hideTOC` | `false` | Hide table of contents |
| `fullWidth` | `false` | Content spans full screen width |
| `maxWidth` | — | Content width in pixels (default ~1280px) |
| `neverShowQueries` | `false` | Remove "show queries" option in deployed app |
| `sidebarDepth` | `3` | Sidebar nav depth (2 or 3) |
| `githubRepo` | — | GitHub repo URL shown in header |

---

## Level 3 — Deployment, Rendering Modes, Environments, Base Paths

### Deployment Overview

Evidence is a static site generator by default. `npm run build` pre-renders every page and query into HTML. The output in `build/` can be served from any static host.

Build process:
1. All source queries run once at build time
2. All pages (including all parameterized page permutations) are generated
3. If a query fails during `build:strict`, the build stops — the old deployed version keeps serving

Schedule or trigger regular builds to keep data fresh.

**`npm run build:strict`** fails if:
- Any SQL query fails (a query returning zero rows is not a failure)
- Any component renders an error state (a component receiving a valid but empty result set will fail — wrap with `{#if}` to avoid this)

### Self-Hosting Platforms

Evidence static output can be deployed to:

- AWS Amplify
- Azure Static Apps
- Cloudflare Pages
- Firebase Hosting
- GitHub Pages
- GitLab Pages
- Hugging Face Spaces
- Netlify
- Vercel
- Windows IIS
- Any static file server

### Storing Credentials for Production

In production, credentials must be supplied as **environment variables**. They are never read from `connection.options.yaml` at build time on the server.

To find the exact variable names for your sources:
1. Run `npm run dev`
2. Go to `http://localhost:3000/settings`
3. Open the deployment panel and select your target platform

**Credential variable format:**

```
EVIDENCE_SOURCE__<source_name>__<variable_name>
```

Variable names are **case sensitive** — preserve the casing shown on the settings page.

### Environment Variables Reference

| Prefix | Usage | Example |
|---|---|---|
| `EVIDENCE_SOURCE__name__var` | Database credentials for a named source | `EVIDENCE_SOURCE__my_db__password` |
| `EVIDENCE_VAR__name` | Variables usable inside source queries | `EVIDENCE_VAR__customer_name` |
| `VITE_name` | Variables accessible in `.md` pages via `import.meta.env` | `VITE_tier=premium` |

**Using `EVIDENCE_VAR__` in a source query:**

```sql
select * from orders
where customer_name = '${customer_name}'
```

**Using `VITE_` in a page:**

```svelte
<script>
  const tier = import.meta.env.VITE_tier;
</script>

{#if tier === 'premium'}
Premium content
{/if}
```

Evidence reads a `.env` file at the project root for local development.

### Environments (Dev vs Prod)

Configure dev credentials via the settings page at `localhost:3000/settings`.

Configure prod credentials as environment variables on your deployment platform.

Common data environment patterns:
- **Separate databases** — same schema/tables, different database per environment
- **Separate schemas** — same database, different schema per environment (Postgres supports an optional `schema` credential parameter)
- **Separate accounts** — fully isolated accounts per environment

### Rendering Modes

#### Static Site Generation (default)

- All pages pre-rendered to HTML at build time
- Fast page loads, rich SEO
- Build time grows with page count
- Best for most apps

#### Single Page App (SPA)

- Only one HTML file generated; pages rendered client-side via JavaScript
- Fast builds, slower page loads, generic SEO
- Use when: >1,000 pages, very frequent data updates, or large data sources

**Enabling SPA mode:**

1. Update `package.json` scripts:

```json
"build": "VITE_EVIDENCE_SPA=true evidence build",
"preview": "VITE_EVIDENCE_SPA=true evidence preview"
```

2. Install the adapter:

```bash
npm install --save-dev @sveltejs/adapter-static
```

3. Create `svelte.config.js` at the project root:

```javascript
import adapter from '@sveltejs/adapter-static';

export default {
    kit: {
        adapter: adapter({
            fallback: 'index.html'
        })
    },
};
```

4. When self-hosting an SPA, redirect all URLs to `index.html`. NGINX example:

```nginx
root /path/to/your/project/build/;

location / {
    try_files $uri $uri/ $uri.html /index.html;
}
```

### Base Paths (Subdirectory Hosting)

Serve Evidence from a subdirectory, e.g. `https://acme.com/analytics`.

**`evidence.config.yaml`:**

```yaml
deployment:
  basePath: /my-base-path
```

Rules:
- Must start with `/`
- Must not end with `/`
- Must be a valid URL path

All markdown links are automatically adjusted to include the base path.

**Adjust the build output directory** (required for `npm run preview` to work correctly):

```json
"build": "EVIDENCE_BUILD_DIR=./build/my-base-path evidence build"
```

**Custom Svelte components** do not have links auto-adjusted. Use `addBasePath`:

```svelte
<script>
  export let link;
  import { addBasePath } from '@evidence-dev/sdk/utils/svelte';
</script>

<a href={addBasePath(link)}>My Link</a>
```

### dbt Monorepo Setup

Install Evidence inside a dbt project:

```shell
cd path/to/your/dbt/project
npx degit evidence-dev/template reports
npm --prefix ./reports install
npm --prefix ./reports run sources
npm --prefix ./reports run dev
```

This co-locates modelling changes (`/models`) and reporting changes (`/reports`) in the same commits.
