# Needs Met Rating — Structured Reference

*Extracted from Google Search Quality Evaluator Guidelines (2025), Part 3: Needs Met Rating Guideline (Sections 12–14)*

---

## 1. The Needs Met 5-Tier Scale

| Rating | Code | Core Criterion |
|---|---|---|
| Fully Meets | FullyM | The result is the single specific thing all or almost all users want. |
| Highly Meets | HM | Very helpful for any dominant, common, or reasonable minor interpretation. |
| Moderately Meets | MM | Helpful but has fewer valuable attributes than HM. Fits the query but less satisfying. |
| Slightly Meets | SM | Less helpful for a reasonable intent, OR helpful for an unlikely minor intent. |
| Fails to Meet | FailsM | Fails the needs of all or almost all users. Off-topic, incorrect, misleading, or useless. |

**Intermediate ratings exist.** You can use HM+, MM+, SM+ to indicate a result is close to the next tier up.

---

## 2. Tier-by-Tier Criteria

### Fully Meets (FullyM)

Three conditions must ALL be true:

1. **Query intent is specific, clear, and unambiguous** — no reasonable alternative interpretations.
2. **There is one specific result** that all or almost all users in the locale are looking for (a specific website, specific webpage, a know-simple fact, a specific local result).
3. **All or almost all users would be completely satisfied** — no need to see additional results.

**What qualifies:**
- Navigational queries with a clear single target: [amazon], [netflix.com], [titanic imdb]
- Know Simple queries with a verifiable, accurate, complete answer displayed prominently: [new york city population 2012], [what country is mount fuji in], [how tall was julia child]
- Specific local queries for a named business with correct contact/location info: [chef chu phone number] (verified correct)
- Specific address queries: [1600 pennsylvania ave washington dc]

**What disqualifies:**
- Any broad informational query: [knitting], [barack obama]
- Ambiguous queries with multiple plausible interpretations: [ada] (ADA, American Dental Association, American Diabetes Association)
- People name queries unless one dominant person is unambiguous
- Any result where some users would need to look further to satisfy their full need

**Conservative rule:** When in doubt, use a lower rating. If the result is very close to FullyM but a small subset of users would want more, use HM or HM+.

**Accuracy check required:** Before assigning FullyM for a fact or contact detail, verify the information is correct.

---

### Highly Meets (HM)

- Assigned to very helpful results for any dominant, common, or reasonable minor interpretation.
- The result is highly satisfying and a good fit for the query.
- HM is the highest achievable rating for most queries (those without a single specific target).
- Multiple HM results can exist for the same query.

**HM characteristics (context-dependent):**
- Entertaining/enjoyable for queries with entertainment intent
- Representative of real people's opinions and experience for subjective queries
- Easy to understand (clear images, helpful summary, accessible language)
- In-depth or expert-level for queries needing depth
- Fresh/timely for queries where recency matters (breaking news, viral trends)
- Any format: articles, video, images, social posts, forums — no length requirement

**Accuracy requirement:** HM informational results must be accurate and trustworthy. On YMYL topics, must represent well-established scientific/medical consensus unless user is explicitly seeking an alternative view.

**Not HM if:** The page is untrustworthy, outdated, or inaccurate.

---

### Moderately Meets (MM)

- Helpful for any reasonable interpretation, including reasonable minor ones.
- Fewer valuable attributes than HM — fits the query but is less satisfying.
- Not wrong or inaccurate, just less ideal. Average to good.
- Acceptable as a "middle ground" when some aspects are HM-level but others are SM-level.

**MM indicators:**
- Less representative of real opinions/perspectives than HM would be
- Content slightly harder to understand than an HM result
- Slightly out of date for time-sensitive queries
- Provides partial coverage — helpful as a starting point but incomplete

**Examples:** A short cute video of emperor penguins for query [emperor penguin] (helpful but not very satisfying). A text description of Virginia's location with no map (helpful but lacks visual aid).

---

### Slightly Meets (SM)

Two separate conditions — either one triggers SM:

1. **Less helpful result for a reasonable intent** — related to the need but doesn't fully address it; or has an aspect preventing a higher rating (e.g., outdated info, missing key details).
2. **Helpful result for an unlikely minor interpretation** — the result is good quality but addresses a low-probability meaning of the query.

**SM indicators:**
- Stale or outdated content for a time-sensitive query: [britney spears] → 2006 divorce article
- Incomplete answer that only partially covers the query
- Good quality page but wrong interpretation (e.g., [hot dog] → 1984 film "Hot Dog")
- Result with a misleading or exaggerated title (user experience mismatch)
- Incidental/indirect answer requiring inference (answer buried, not prominent)

**SM does NOT apply when:** A result is missing specific requested info entirely — that is FailsM.

---

### Fails to Meet (FailsM)

Assigned when the result fails the needs of all or almost all users.

**FailsM triggers:**
- Off-topic: result addresses a no-chance interpretation of the query
- Wrong locale/location: pest control company in Australia for a US user
- Critical query element ignored: [australian open mens singles result 2008] → returns 2004 results
- Factually incorrect information: wrong translation, wrong phone number, factually false answer
- Keyword match only, no actual relevance: [tooth loss five years old] → pike fish article
- Misleading/conspiracy content presented as fact
- Gibberish or low-quality pages that are unusable
- Surprising users with content they clearly did not seek: porn, offensive material, harmful content
- Unsatisfying visit-in-person results for transactional queries: [go kart for sale] → go kart arcades

**Automatic FailsM regardless of page quality:**
- Useless results (useless is useless, even if the page itself is high quality)
- Harmful/misleading content when user is not seeking it
- Incorrect facts for know-simple queries

---

## 3. Query Interpretation — Determining Dominant Intent

### Interpretation Hierarchy

| Term | Meaning |
|---|---|
| Dominant interpretation | What most users mean. Should be clear from context + research. Not all queries have one. |
| Common interpretation | What many or some users mean. A query can have multiple common interpretations. |
| Reasonable minor interpretation | What fewer users want, but still worth serving. |
| Unlikely minor interpretation | Theoretically possible but very few users want this. A result for this gets SM at best. |
| No-chance interpretation | Almost no user wants this. Results for it get FailsM. |

### How to Determine Dominant Intent

1. **Read the query literally** — every word matters. Missing a modifier (e.g., "non-emergency") disqualifies a result.
2. **Do web research** — do not rely solely on top Google results.
3. **Apply locale + user location** — same query can have different dominant intents by city (e.g., [verbena] in Austin TX vs. elsewhere).
4. **Consider recency** — query meanings change over time (e.g., [iphone] means the latest model now, not the first model from 2007).
5. **Consider query specificity** — specific queries have fewer valid interpretations; broad queries like [mercury] have many.

### Query Interpretation Signals

- **Explicit location in query** → very strong signal (e.g., [Dallas hotels] — user wants Dallas, not their own city)
- **Specific named entities** → narrow interpretation
- **Branded URL-style queries** → Website intent is dominant
- **"Near me" phrasing** → Visit-in-person intent
- **Action words** (buy, watch, download, pay) → Do intent
- **Question words** (who, what, how, when) → Know or Know Simple intent

---

## 4. Query Types and How Needs Met Differs

### Know Queries

User wants information or to explore a topic.

**Know Simple:** Single verifiable fact, fits in 1–2 sentences or a short list, most people agree on the answer. Examples: heights, populations, dates, conversions, weather. FullyM is achievable for Know Simple when the answer is accurate and prominently displayed.

**Know (broad):** Complex, exploratory, no single right answer, or different users want different things. FullyM is NOT achievable. HM requires depth, accuracy, good coverage.

**Needs Met differences:**
- For Know Simple: accuracy and completeness are paramount. An approximate or buried answer is SM.
- For broad Know: diversity of perspectives, depth, and freshness can all push toward HM.
- For YMYL Know queries: expert consensus must be represented; a non-medical source on allergy symptoms is SM even if current.

### Do Queries

User wants to accomplish a goal: download, buy, watch, play, interact, complete a task.

**Needs Met differences:**
- The result must enable the action, not just describe it.
- For transactional queries, a page that describes but doesn't allow the transaction gets SM or lower.
- Browsing/open-ended Do queries (e.g., [small bathroom organization ideas]) benefit from diverse content types — images, how-to guides, videos all qualify for HM if they meet the browsing intent.

### Website (Navigational) Queries

User wants a specific website or webpage.

**Needs Met differences:**
- The exact target page = FullyM.
- Official homepage when user likely wants a section = HM (user must do additional work to find the section).
- A competitor's homepage = FailsM.
- Imperfect URL queries (typos, .coom instead of .com) — honor the evident intent; the target site still = FullyM.

### Visit-in-Person Queries

User wants to physically go somewhere.

**Needs Met differences:**
- Proximity is critical — results from 60 miles away for a local grocery store query = FailsM.
- Info-in-block (address, hours, directions) pushes toward HM; requiring multiple clicks pushes down.
- Results that give arcades when user wants to purchase something = FailsM (wrong action type).
- A query like [walmart] has dual intent (visit + website) — results must address at least one well to get HM.

---

## 5. User Needs Framework

The guidelines use three layers of user need to evaluate results:

| Layer | Description | Example (query: [ibuprofen dosage]) |
|---|---|---|
| Immediate need | What the user explicitly wants from this search right now | The correct dosage for ibuprofen |
| Final goal | The larger objective behind the search | Taking the right amount to relieve pain safely |
| Background desire | Implicit quality standards the user expects without stating | Accurate medical info, not a random blog |

**Application:** A result that satisfies the immediate need but violates background desires (e.g., gives the right dosage from an untrustworthy source) cannot be rated HM on a YMYL topic. A result that misses the immediate need entirely gets FailsM even if the page is high quality and topically adjacent.

---

## 6. YMYL Topic Categories — Full Taxonomy

### Definition

YMYL (Your Money or Your Life) = topics that could significantly impact a person's health, financial stability, or safety, or the welfare of society. The defining test: **could inaccurate content cause real harm?**

### Four Primary YMYL Categories

**1. YMYL Health or Safety**
Topics that could harm mental, physical, or emotional health, or any form of safety (physical, online).

Examples:
- Symptoms of medical conditions (heart attack, stroke, allergic reaction)
- Drug dosages and interactions
- Medical treatments, procedures, and outcomes
- Mental health advice and crisis information
- Suicide and self-harm content
- Vaccine safety and efficacy
- Emergency procedures (e.g., evacuation routes for a tsunami, when to go to the ER)
- Child safety online
- Food safety

**2. YMYL Financial Security**
Topics that could damage a person's ability to support themselves and their families.

Examples:
- Investment advice (stocks, retirement, real estate)
- Tax filing instructions
- Loan and mortgage guidance
- Insurance decisions
- Bankruptcy and debt management
- Purchasing prescription drugs (requires licensed pharmacies)
- Fraud and scam avoidance

**3. YMYL Government, Civics & Society**
Topics that could negatively impact groups of people, institutions, elections, or public trust.

Examples:
- Voting eligibility and registration
- Election results and candidate information
- Laws and legal rights
- Government benefit programs
- Public health policy
- Civil rights and discrimination
- Content that could incite violence against groups (e.g., racial inferiority claims)

**4. YMYL Other**
Topics that could hurt people or negatively impact societal welfare that don't fit the above.

Examples:
- Violent extremism and terrorism
- Dangerous social media challenges (e.g., tide pod challenge)
- Content facilitating criminal activity
- Harmful misinformation with real-world consequences

### YMYL Spectrum — Three Zones

| Zone | Criteria | Examples |
|---|---|---|
| Clear YMYL | Minor inaccuracies could cause real harm; careful people seek expert sources | Tsunami evacuation routes, when to go to the ER, prescription drug purchasing |
| May be YMYL | Some risk but most people would casually consult friends | Weather forecast, how often to replace a toothbrush, car reviews |
| Not YMYL | Inaccuracies cause no meaningful harm | Music award winners, rock band opinions, washing frequency for jeans |

### YMYL Decision Test

1. Would a careful person seek out experts or highly trusted sources to prevent harm? Could even minor inaccuracies cause harm? → **Likely YMYL**
2. Is this a topic most people would be content to casually ask a friend about? → **Likely not YMYL**

---

## 7. Why YMYL Gets Stricter Evaluation

### The Reasoning

YMYL content has asymmetric downside risk: bad advice on investments or medical conditions can cause financial ruin, injury, or death. The same low-quality page that is SM for [knitting tips] becomes FailsM for [symptoms of heart attack] because the stakes are categorically different.

Three groups can be harmed:
1. The person directly viewing the content
2. People affected by the viewer's decisions after seeing the content
3. Society if the content spreads and influences collective behavior

### What "Stricter" Means in Practice

| Dimension | Non-YMYL standard | YMYL standard |
|---|---|---|
| Accuracy | Mild inaccuracies = MM | Mild inaccuracies = FailsM or Lowest PQ |
| Source authority | Any credible source can qualify for HM | Must be from authoritative, expert, or institutionally trusted sources |
| Expert consensus | Not required | Must represent well-established consensus; alternative views only acceptable when user explicitly seeks them |
| Personal experience | Can be HM for most topics | Only acceptable on YMYL when content is safe, non-medical/non-financial tips consistent with expert consensus |
| Trustworthiness signals | Considered | Heavily weighted; no E-E-A-T evidence = cannot be HM |

### YMYL: Experience vs. Expertise

Some YMYL content is appropriate from lived experience; other YMYL content must come from experts:

| YMYL Topic | Experience-based content acceptable | Must come from experts |
|---|---|---|
| Sleep challenges when pregnant | Non-medical pillow/positioning tips from people who've been through it | Sleep medications safe during pregnancy |
| Liver cancer treatment | Sincere forum discussion about coping emotionally | Treatment options and associated life expectancies |
| Filling out tax forms | Humorous non-expert video about the frustration of doing taxes | Actual instructions on how to fill out the forms |
| How to vote | Personal post about why they believe voting matters | Eligibility rules and registration procedures |

---

## 8. High vs. Low Needs Met — Examples by Query Type

### Navigational Queries

| Query | High NM Result | Low NM Result |
|---|---|---|
| [amazon] | amazon.com homepage | Corporate office address block for Amazon |
| [cnn health] | CNN.com/health section page | CNN homepage (requires extra navigation) |
| [titanic imdb] | The exact IMDb Titanic page | Any other film database or a different Titanic page |

### Know Simple Queries

| Query | High NM Result | Low NM Result |
|---|---|---|
| [what country is mount fuji in] | Block displaying "Japan" clearly and correctly | Page mentioning Japan only incidentally, buried in text |
| [new york city population 2012] | Block or page with the exact 2012 figure, prominently displayed | Page with current population only; year mismatch |
| [air canada phone number] | Correct 1-888-247-2262 number | Any incorrect phone number — even with good presentation |

### Know (Broad) Queries

| Query | High NM Result | Low NM Result |
|---|---|---|
| [michael jordan] | Wikipedia article with comprehensive biographical info | Stale fan site with no recent updates |
| [poison ivy] | Medical/nature page with treatment, identification, images | Blog post about "Poison Ivy" character from Batman |
| [allergy symptoms] | Medical resource covering multiple allergy types thoroughly | News article about one seasonal trigger; not a medical source |

### Do / Transactional Queries

| Query | High NM Result | Low NM Result |
|---|---|---|
| [broadway tickets] | Page where tickets can actually be purchased | Informational page about Broadway with no purchase option |
| [watch stranger things] | Netflix or streaming page where the show plays | Article reviewing Stranger Things |
| [go kart for sale] | Page listing go karts for purchase | Go kart arcade listing in the same city |

### Visit-in-Person Queries

| Query | High NM Result | Low NM Result |
|---|---|---|
| [nearby coffee shops] (DC) | Interactive map block with popular nearby options and directions | A single obscure coffee shop 15 miles away |
| [ralphs] (San Clemente, CA) | Ralphs locations in San Clemente or immediate area | Ralphs locations 60 miles away in San Diego |
| [company to get rid of the possum in my attic] (Naperville, IL) | US-based pest control company in Illinois | Pest control company in Australia |

### YMYL Queries

| Query | High NM Result | Low NM Result |
|---|---|---|
| [symptoms of dehydration] | Highly authoritative medical website with accurate, complete, trustworthy MC | Non-medical page with no evidence of expertise; potentially misleading |
| [mentos and coke death] | Well-known fact-checking site calling the claim false with explanation | Blog repeating the false claim without debunking it |
| [1969 moon landing] | NASA's official website with detailed summary, video, images | Page with keyword matches but fabricated or conspiracy-theory content |

---

## 9. Decision Framework: How to Rate a Query + Page

### Step 1 — Understand the Query

- What is the dominant interpretation? (research if needed)
- What are the common and minor interpretations?
- What query type is it? (Know Simple / Know / Do / Website / Visit-in-Person)
- Is the locale or user location relevant?
- Is the topic YMYL? (use the four-category taxonomy and the two decision questions)

### Step 2 — Understand What the User Needs

- Immediate need: what specific thing are they looking for right now?
- Final goal: what is the larger task they are trying to accomplish?
- Background desires: what implicit quality standards do they expect?

### Step 3 — Evaluate the Result Against the Query

Ask: **Does this result completely, mostly, partially, or not at all satisfy the dominant user intent?**

Then apply the tier test:

```
Is the query specific + result exactly what all users want + users would be satisfied?
  → FullyM

Is the result very helpful for the dominant or a reasonable minor intent?
  → HM (if accurate, trustworthy, YMYL-appropriate)

Is the result helpful but less satisfying than ideal?
  → MM

Is the result less helpful, or helpful only for an unlikely interpretation?
  → SM

Does the result fail all or almost all users? (wrong topic, wrong answer, misleading, wrong location, off-topic match)
  → FailsM
```

### Step 4 — Apply YMYL Adjustment

If the topic is YMYL:
- Downgrade if source lacks expertise/authority
- Downgrade if content contradicts expert consensus without clear reason
- Downgrade if mild inaccuracies are present (threshold is lower than non-YMYL)
- FailsM for factual errors, misleading content, or harmful advice

### Step 5 — Consider What You Are Rating

- **SCRB (Special Content Result Block):** Rate the block content if users likely don't click through. If users would click, both block and landing page must be helpful to justify HM.
- **Web Search Result Block:** Rate the landing page — a click is required.
- **Misleading title:** If the title misrepresents the landing page, max rating is SM.

### Key Override Rules

- A high Page Quality rating does NOT override FailsM. Useless is useless.
- An incorrect answer on a Know Simple query = FailsM, regardless of how well the page is designed.
- A result for a no-chance interpretation = FailsM.
- Porn, harmful, or offensive content when user clearly is not seeking it = FailsM.
- For Website queries with clear navigational intent: even low-quality target pages = FullyM (users are allowed to search for any website).
