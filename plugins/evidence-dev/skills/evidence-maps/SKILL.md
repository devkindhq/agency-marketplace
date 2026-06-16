---
name: evidence-maps
description: Evidence.dev map components — AreaMap, BaseMap, BubbleMap, PointMap, USMap for geographic data visualization
version: 1.0.0
---

## When to use
Invoke when the user asks to:
- Add a map to an Evidence.dev page ("show this by region", "choropleth map", "bubble map")
- Display geographic or location-based data
- Use AreaMap, BubbleMap, or PointMap components
Note: GeoJSON files may need to be fetched via WebFetch or Bash if not already present.

# Evidence Map Components

Five map components for geographic data visualization. All are built on Leaflet (except USMap which uses ECharts). Maps auto-zoom to fit the data unless overridden.

---

## Level 1: Component Overview + Minimal Syntax

### AreaMap
Choropleth map — shades regions by a numeric or categorical value. Requires external GeoJSON to define region boundaries.

```svelte
<AreaMap
    data={my_query}
    areaCol=region_id
    geoJsonUrl='path/to/regions.geojson'
    geoId=FEATURE_ID_PROPERTY
    value=metric
/>
```

### BaseMap
Container for composing multiple map layers (`<Areas/>`, `<Points/>`, `<Bubbles/>`). Use when you need overlapping layer types on one map.

```svelte
<BaseMap>
  <Areas data={areas_query} areaCol=zip geoJsonUrl='/geo/zips.geojson' geoId=ZCTA5CE10 value=sales/>
  <Points data={points_query} lat=lat long=long color=#179917/>
</BaseMap>
```

### BubbleMap
Points sized proportionally to a numeric column. Size is easier to read than color for a primary metric — use `size` for the main metric and optionally `value` for color.

```svelte
<BubbleMap
    data={my_query}
    lat=lat
    long=long
    size=revenue
    pointName=location_name
/>
```

### PointMap
Fixed-size dots on a map, optionally color-coded by a metric. Use when all points are equally important and you just need location.

```svelte
<PointMap
    data={my_query}
    lat=lat
    long=long
    pointName=location_name
/>
```

### USMap
Flat choropleth of US states only. No GeoJSON required — built-in state boundaries. Uses ECharts renderer (not Leaflet).

```svelte
<USMap
    data={my_query}
    state=state_name
    value=metric
/>
```

---

## Level 2: Data Shape Requirements + Common Props + Practical Examples

### Data Shape by Component

**AreaMap / Areas layer**
```sql
-- Requires a column that matches values in the GeoJSON's geoId property
select zip_code, sum(sales) as sales from orders group by zip_code
-- zip_code values must match the GeoJSON feature property named in geoId=
```

**PointMap / BubbleMap / Points / Bubbles layers**
```sql
-- Requires numeric lat and long columns (decimal degrees, WGS84)
select
    location_name,
    latitude  as lat,    -- column name passed to lat= prop
    longitude as long,   -- column name passed to long= prop
    revenue
from locations
```

**USMap**
```sql
-- state column must contain full state names OR two-letter abbreviations
-- Full names: 'California', 'New York', etc.
-- Abbreviations: 'CA', 'NY', etc. (requires abbreviations=true)
select state_name, sum(orders) as orders from sales group by state_name
```

**GeoJSON requirement for AreaMap**
The GeoJSON must be a FeatureCollection. Each Feature needs a `properties` object containing the field referenced by `geoId`. The `areaCol` in your data must match the values of that property.

```
GeoJSON feature:  { "properties": { "ZCTA5CE10": "90210" } }
Data row:         { "zip_code": "90210", "sales": 12345 }
Component props:  geoId=ZCTA5CE10  areaCol=zip_code
```

### Practical AreaMap Example — Orders by State (Online GeoJSON)

```sql orders_by_state
select state, count(*) as orders
from orders
where state not in ('Alaska', 'Hawaii')
group by state
```

```svelte
<AreaMap
    data={orders_by_state}
    areaCol=state
    geoJsonUrl=https://d2ad6b4ur7yvpq.cloudfront.net/naturalearth-3.3.0/ne_110m_admin_1_states_provinces.geojson
    geoId=name
    value=orders
    height=400
/>
```

### Practical BubbleMap Example — Revenue by Location

```sql location_revenue
select location_name, lat, long, revenue from locations
```

```svelte
<BubbleMap
    data={location_revenue}
    lat=lat
    long=long
    size=revenue
    sizeFmt=usd
    value=revenue
    valueFmt=usd
    pointName=location_name
    maxSize=30
/>
```

### Practical USMap Example — Population by State

```sql state_pop
select state_name, population from state_data
```

```svelte
<USMap
    data={state_pop}
    state=state_name
    value=population
    colorScale=info
    legend=true
    title="Population by State"
/>
```

### Common Props (Leaflet-based maps: AreaMap, BubbleMap, PointMap, BaseMap)

| Prop | What it does | Example |
|------|-------------|---------|
| `height` | Map height in pixels (default 300) | `height=450` |
| `startingLat` / `startingLong` | Override auto-center | `startingLat=37.7` |
| `startingZoom` | Override auto-zoom (1–18) | `startingZoom=10` |
| `basemap` | Tile URL template | see Level 3 |
| `attribution` | Attribution text on map | `attribution='© OpenStreetMap'` |
| `title` | Title above the map | `title="Sales Map"` |
| `subtitle` | Subtitle below title | `subtitle="FY2024"` |

### Interactivity — Link Drilldown

Add a URL column to your query and pass the column name to `link=`. Clicking a point/area navigates to that URL.

```sql locations_with_links
select *, '/locations/' || id as detail_link from locations
```

```svelte
<PointMap data={locations_with_links} lat=lat long=long link=detail_link/>
```

### Interactivity — Map as Input

Set `name=` to expose the clicked row as `{inputs.name}`. Use in downstream queries or components.

```svelte
<AreaMap
    data={my_query}
    areaCol=region
    geoJsonUrl='/geo/regions.geojson'
    geoId=region_id
    value=sales
    name=selected_region
/>

<!-- Use the selection -->
Selected: {inputs.selected_region.region}
```

```sql filtered
select * from sales
where region = '${inputs.selected_region.region}'
  OR '${inputs.selected_region.region}' = 'true'
```

---

## Level 3: Full Prop Reference + Tile Providers + Advanced Customization

### AreaMap Props

#### Required
| Prop | Type | Description |
|------|------|-------------|
| `data` | query result | Query result in curly braces |
| `geoJsonUrl` | URL or path | Path/URL to GeoJSON FeatureCollection. Files in `static/` referenced as `/filename.geojson` |
| `areaCol` | column name | Column whose values match the GeoJSON `geoId` property |
| `geoId` | string | Property name in each GeoJSON feature that uniquely identifies it |

#### Data / Color
| Prop | Default | Description |
|------|---------|-------------|
| `value` | — | Column for color scale (numeric or categorical) |
| `valueFmt` | — | Format string for the value (e.g. `usd`, `pct`, Excel format) |
| `colorPalette` | theme default | Array of colors. For numeric: gradient stops. For categorical: one color per category. E.g. `{['#C65D47','#4A8EBA']}` |
| `min` | min of data | Override minimum for color scale |
| `max` | max of data | Override maximum for color scale |
| `color` | — | Single flat color for all areas (overrides value-based coloring) |

#### Legend
| Prop | Default | Description |
|------|---------|-------------|
| `legend` | `true` | Show/hide legend |
| `legendType` | auto | `categorical` or `scalar` |
| `legendPosition` | `bottomLeft` | `bottomLeft`, `topLeft`, `bottomRight`, `topRight` |

#### Styling
| Prop | Default | Description |
|------|---------|-------------|
| `opacity` | `0.8` | Fill opacity (0–1) |
| `borderWidth` | `0.75` | Border thickness in pixels |
| `borderColor` | `white` | Border CSS color |
| `selectedColor` | — | Fill color when area is selected |
| `selectedOpacity` | `0.8` | Opacity when selected |
| `selectedBorderWidth` | `0.75` | Border width when selected |
| `selectedBorderColor` | `white` | Border color when selected |

#### Tooltips
| Prop | Default | Description |
|------|---------|-------------|
| `showTooltip` | `true` | Enable/disable tooltips |
| `tooltipType` | `hover` | `hover` or `click` |
| `tooltipClass` | — | Tailwind classes applied to tooltip container |
| `tooltip` | — | Custom tooltip config array (see below) |

#### Viewport / Base Map
| Prop | Default | Description |
|------|---------|-------------|
| `startingLat` | auto | Center latitude |
| `startingLong` | auto | Center longitude |
| `startingZoom` | auto | Zoom level 1–18 |
| `height` | `300` | Height in pixels |
| `basemap` | Evidence default | Tile URL template — wrap in backtick+brace to escape `{z}/{x}/{y}` |
| `attribution` | — | Attribution HTML string |
| `ignoreZoom` | `false` | Prevent this layer from influencing auto-zoom |

#### Interactivity
| Prop | Description |
|------|-------------|
| `link` | Column name containing navigation URLs |
| `name` | Input name; exposes clicked row as `{inputs.name}` |

---

### BubbleMap Props

Same base map props as AreaMap. Additional bubble-specific props:

| Prop | Required | Default | Description |
|------|----------|---------|-------------|
| `lat` | yes | — | Column with latitude values |
| `long` | yes | — | Column with longitude values |
| `size` | yes | — | Column driving bubble size |
| `sizeFmt` | — | — | Format string for size value in tooltip |
| `maxSize` | — | `20` | Maximum bubble radius in pixels |
| `value` | — | — | Column for color scale |
| `valueFmt` | — | — | Format string for color value |
| `pointName` | — | — | Column for point label (tooltip title) |

---

### PointMap Props

Same base map props as AreaMap. Additional point-specific props:

| Prop | Required | Default | Description |
|------|----------|---------|-------------|
| `lat` | yes | — | Column with latitude values |
| `long` | yes | — | Column with longitude values |
| `value` | — | — | Column for color scale |
| `valueFmt` | — | — | Format string for value |
| `pointName` | — | — | Column for point label (tooltip title) |
| `size` | — | `5` | Fixed point radius in pixels |

---

### USMap Props

| Prop | Required | Default | Description |
|------|----------|---------|-------------|
| `data` | yes | — | Query result |
| `state` | yes | — | Column with state names or abbreviations |
| `value` | yes | — | Column driving state fill color |
| `abbreviations` | — | `false` | Set `true` if state column uses two-letter codes (CA, NY, etc.) |
| `colorScale` | — | `info` | Built-in scale: `info`, `positive`, `negative` |
| `colorPalette` | — | — | Custom color array, overrides `colorScale`. E.g. `{['maroon','white','#1c0d80']}` |
| `min` / `max` | — | data min/max | Clamp the color scale |
| `fmt` | — | — | Value format string |
| `title` | — | — | Title above map |
| `subtitle` | — | — | Subtitle below title |
| `link` | — | — | Column containing URLs for click navigation |
| `legend` | — | `false` | Show legend |
| `filter` | — | `false` | Add range filter to legend (requires `legend=true`) |
| `emptySet` | — | `error` | `error`, `warn`, or `pass` for empty datasets |
| `emptyMessage` | — | `No records` | Message shown on empty dataset |
| `renderer` | — | `canvas` | ECharts renderer: `canvas` or `svg` |
| `echartsOptions` | — | — | Raw ECharts config overrides |
| `seriesOptions` | — | — | ECharts series-level overrides |
| `downloadableData` | — | `true` | Show data download button |
| `downloadableImage` | — | `true` | Show image save button |

---

### BaseMap — Layer Components

Use `<Areas/>`, `<Points/>`, `<Bubbles/>` as children of `<BaseMap>`. Each layer accepts the same props as its standalone counterpart (minus the viewport/basemap props, which belong on `<BaseMap>` itself).

```svelte
<BaseMap
    basemap={`https://tile.openstreetmap.org/{z}/{x}/{y}.png`}
    attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    height=500
    startingLat=34.05
    startingLong=-118.25
    startingZoom=9
>
  <Areas
      data={zip_sales}
      areaCol=zip_code
      geoJsonUrl='/geo/ca_zips.geojson'
      geoId=ZCTA5CE10
      value=sales
      valueFmt=usd
      opacity=0.6
  />
  <Bubbles
      data={locations}
      lat=lat
      long=long
      size=revenue
      sizeFmt=usd
      pointName=name
      opacity=0.5
  />
  <Points
      data={stores}
      lat=lat
      long=long
      color=#cc0000
      size=8
  />
</BaseMap>
```

**Bubbles-only props (not in Points/Areas):**
- `paneType` — specifies the Leaflet pane type for rendering
- `z` — z-index for the pane (higher = on top; useful for layering)

---

### Custom Tooltip Configuration

All Leaflet-based maps accept a `tooltip` array to define exactly what appears in the tooltip.

```svelte
<PointMap
    data={my_query}
    lat=lat
    long=long
    tooltipType=hover
    tooltip={[
        {id: 'location_name', showColumnName: false, valueClass: 'text-xl font-semibold'},
        {id: 'revenue', fmt: 'usd', fieldClass: 'text-[grey]', valueClass: 'text-[green]'},
        {id: 'detail_url', showColumnName: false, contentType: 'link', linkLabel: 'View details', valueClass: 'font-bold mt-1'}
    ]}
/>
```

**Tooltip item options:**
| Key | Description |
|-----|-------------|
| `id` | Column name |
| `title` | Custom label string (overrides column name) |
| `fmt` | Format string for the value |
| `showColumnName` | `false` to hide the label, showing only the value |
| `contentType` | `'link'` to render the value as a hyperlink |
| `linkLabel` | Display text for the link (when `contentType='link'`) |
| `formatColumnTitle` | Auto-capitalize first letter of column name (only when `title` not set) |
| `valueClass` | Tailwind classes for the value cell |
| `fieldClass` | Tailwind classes for the label cell |

---

### Tile Providers

Wrap tile URLs in backtick+brace syntax to prevent Evidence from interpreting `{z}`, `{x}`, `{y}` as template variables.

```svelte
<!-- OpenStreetMap (no API key) -->
<AreaMap ... basemap={`https://tile.openstreetmap.org/{z}/{x}/{y}.png`}
    attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'/>

<!-- Stadia Alidade Smooth Dark -->
<AreaMap ... basemap={`https://tiles.stadiamaps.com/tiles/alidade_smooth_dark/{z}/{x}/{y}{r}.{ext}`}
    attribution='&copy; Stadia Maps'/>
```

Browse more providers and preview them at: https://leaflet-extras.github.io/leaflet-providers/preview/

---

### Public GeoJSON Sources

**Natural Earth (via geojson.xyz) — no API key needed:**
- Countries (110m): `https://d2ad6b4ur7yvpq.cloudfront.net/naturalearth-3.3.0/ne_110m_admin_0_countries.geojson`
- US States (110m): `https://d2ad6b4ur7yvpq.cloudfront.net/naturalearth-3.3.0/ne_110m_admin_1_states_provinces.geojson`

**GeoJSON format reminder:**
```json
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": { "YOUR_GEO_ID_FIELD": "match-value" },
      "geometry": { "type": "Polygon", "coordinates": [...] }
    }
  ]
}
```

Files stored in your project's `static/` directory are referenced as `/filename.geojson` (absolute path from site root).

---

### Color Palette Patterns

**Numeric gradient (two stops = simple gradient):**
```svelte
colorPalette={['#C65D47', '#4A8EBA']}
```

**Numeric gradient (multi-stop):**
```svelte
colorPalette={[['yellow','yellow'],['orange','orange'],['red','red'],['darkred','darkred']]}
```

**Categorical (one color per category — match order to your categories):**
```svelte
colorPalette={['#C65D47', '#5BAF7A', '#4A8EBA', '#D35B85', '#E1C16D', '#6F5B9A', '#4E8D8D']}
```

## Parallelisation
Safe — writes only to .md page files. GeoJSON downloads are read-only side effects.
