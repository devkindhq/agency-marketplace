# QRG: Introduction, Role, and Rating Scales

*Source: Google Search Quality Evaluator Guidelines, September 2025 (182pp) + Overview doc (36pp)*

---

## 1. What Quality Raters Are and Do

- ~16,000 external raters globally (EMEA ~4,000 / North America ~7,000 / LATAM ~1,000 / APAC ~4,000), 80+ languages
- Raters evaluate sample searches to measure how well ranking algorithms perform — they do NOT directly rank individual pages
- **No single rating moves a page up or down in Search.** Ratings are aggregated to calibrate algorithms and provide positive/negative training examples
- Raters must represent typical users in their locale, not apply personal opinions, religious views, or political preferences
- Two core rating tasks: **Page Quality (PQ)** and **Needs Met (NM)**

---

## 2. Core Philosophy

Google's mission: help people find helpful, relevant, reliable information.

Three elements:
1. **High-quality automated ranking** — systems identify useful, reliable information
2. **Helpful search features** — direct access to authoritative sources
3. **Content policies** — prevent harmful or low-quality content from appearing

Key principle: **Websites and pages should be created to help people.** If a page was created primarily to make money with little effort to help users, or to deceive/harm, it warrants a Lowest rating.

Page type alone does not determine quality — encyclopedia, humor, shopping, forum, and error pages can all be Highest or Lowest quality. Purpose drives the rating.

---

## 3. Key Definitions

| Term | Definition |
|---|---|
| **Webpage** | Any page accessible via web browser; includes text, images, video, interactive features |
| **Website/Site** | A collection of pages owned/controlled by one entity. Major sections (subdomains) with distinct purposes can be treated as separate websites |
| **Homepage** | The main/root page of a site (e.g., apple.com) |
| **Website Owner** | The person, company, or organization responsible for the site |
| **Content Creator** | The individual(s) or entity who created the specific content on a page |
| **Generative AI** | ML model that creates content (text, images, code, etc.). Can be helpful or misused |
| **User** | Any person searching — diverse ages, genders, races, religions, political views |

### Page Content Types

| Type | Description |
|---|---|
| **MC (Main Content)** | Any part of the page that directly helps it achieve its purpose. Includes title, text, images, video, interactive features, user-generated content, tabs with additional info |
| **SC (Supplementary Content)** | Contributes to UX but is not the main purpose (e.g., navigation, related links, comments section) |
| **Ads/Monetization** | Advertisements and monetisation features. Presence of ads ≠ low quality, but ads that interfere with MC are a negative signal |

---

## 4. Three-Step Page Quality Process

**Step 1 — Determine the purpose of the page**
What was this page created to do? (inform, sell, entertain, share, etc.)

**Step 2 — Assess if the purpose is harmful**
If the page was designed to deceive, harm, or mislead → automatic **Lowest** rating

**Step 3 — Assign the PQ rating**
Based on how well the page achieves its beneficial purpose, using the 5-tier scale below

---

## 5. Page Quality (PQ) Rating Scale

A 5-point scale (with half-points in practice): how well does the page achieve its purpose?

| Rating | Core Meaning | Key Characteristics |
|---|---|---|
| **Lowest** | Untrustworthy, deceptive, harmful, or spammy | Harmful purpose, malware, deception, pure spam, no MC, dangerous misinformation |
| **Low** | Intended to serve a purpose but fails in an important way | Thin/low-effort MC, missing E-E-A-T, clickbait, mildly negative reputation |
| **Medium** | Achieves its purpose but nothing special | Nothing notably wrong, nothing notably strong. Or: strong High characteristics offset by mild Low ones |
| **High** | Achieves its beneficial purpose well | Solid MC quality, positive reputation, high E-E-A-T for the topic |
| **Highest** | Achieves its purpose very well | Exceptional MC, very positive reputation, very high E-E-A-T, stands out from the crowd |

**YMYL amplification:** Pages on Your Money or Your Life topics must meet a significantly higher bar — what would be Medium for a general topic may be Low for a YMYL topic.

---

## 6. Needs Met (NM) Rating Scale

A 6-point scale: how well does a search result satisfy the user's intent?

| Rating | Numeric | Core Meaning |
|---|---|---|
| **Fully Meets (FullyM)** | 6 | Special category: only applies when the query has one specific correct answer, and this result IS that answer. User is immediately and completely satisfied, needs no other results |
| **Highly Meets (HM)** | 5 | Very helpful for the dominant query intent. Most users with this query would be very satisfied |
| **Moderately Meets (MM)** | 4 | Helpful for the dominant intent, or very helpful for a less common but reasonable interpretation |
| **Slightly Meets (SM)** | 3 | Helpful for a small fraction of users, or partially helpful but incomplete for the dominant intent |
| **Fails to Meet (FailsM)** | 1–2 | Fails for all or almost all users. Off-topic, wrong language, outdated, or completely misses the intent |
| **N/A** | — | Not applicable (used in specific task types) |

**Two-step NM process:**
1. Determine the dominant user intent from the query (+ user location if relevant)
2. Assess how fully the result satisfies that intent

---

## 7. E-E-A-T Overview

Four dimensions used in PQ rating (details in `eeat.md`):

| Letter | Dimension | What it means |
|---|---|---|
| **E** | Experience | Does the creator have first-hand, real-world experience with this topic? |
| **E** | Expertise | Does the creator have formal or deep knowledge of the subject? |
| **A** | Authoritativeness | Is the creator/site recognised as a go-to source for this topic? |
| **T** | Trustworthiness | Is the page accurate, honest, safe, and reliable? **(Most important dimension)** |

Trustworthiness is the foundation — a page can have Experience and Expertise but still fail on Trust (e.g., accurate info presented deceptively).

---

## 8. YMYL Overview

Topics where low-quality content could significantly harm health, finances, safety, or society.

Four YMYL categories:
- **YMYL Health or Safety** — physical, mental, emotional health; personal safety; online safety
- **YMYL Financial Security** — ability to support oneself/family
- **YMYL Government, Civics & Society** — elections, public institutions, civic information
- **YMYL Other** — anything else with potential for serious harm

YMYL is a spectrum (clear YMYL → may be YMYL → not YMYL). When in doubt: *Would a careful person seek experts or highly trusted sources to prevent harm? Could minor inaccuracies cause harm?* If yes → YMYL.

Full YMYL taxonomy with examples → `needs-met.md`

---

## 9. Relationship Between PQ and NM

- **PQ** evaluates the page itself in isolation — quality regardless of any search query
- **NM** evaluates how well the page serves a specific user for a specific query
- A high-PQ page can have low NM if it doesn't match the query intent
- A low-PQ page can never have high NM — poor quality undermines usefulness
- For YMYL queries, both PQ and NM standards are elevated simultaneously
