# Special Content Types — QRG Reference

Distilled from Google's Search Quality Evaluator Guidelines (September 2025 edition), sections covering special content types and additional evaluation guidance.

---

## 1. Landing Pages and Forums — Rating UGC, Q&A, and Discussion Boards

**Framing:** The full page — question, all answers/responses, and resulting discussion — is the Main Content. Rate from the perspective of a visitor arriving from search, not an active participant.

**Identity:** Usernames and aliases are acceptable identifiers for forum contributors. A page can earn High or Highest with username-only authors if other quality criteria are met.

**E-E-A-T for UGC:** Judge E-E-A-T through the posts themselves. For some topics, first-hand Experience is the primary Trust signal; for others, Expertise matters more. Posters sometimes explicitly state their credentials or experience — factor that in.

**YMYL on forums:** Forum pages on YMYL topics require stricter scrutiny of Trust and accuracy. Harmfully misleading medical, financial, or legal advice in a forum post is Lowest quality regardless of how active or popular the thread is.

### Rating anchors

| Tier | Key signals |
|---|---|
| **Highest** | Deep, satisfying discussion; participants with clear Experience or Expertise; unique insights unavailable in everyday real-world community |
| **High** | Participants share genuine first-hand experience; substantive answers; some topical authority (e.g., forum dedicated to that niche) |
| **Medium** | New question with no answers yet; or mixed page — some insightful discussion alongside clutter or tangential drift |
| **Low** | Surface-level or sparse participation; mild inaccuracies; discussion not achieving its purpose over time |
| **Lowest** | Harmful or misleading advice; content that contradicts well-established expert consensus; encourages harm |

**Edge cases:**
- A brand-new thread with only the original question, no replies: rate Medium unless red flags exist. The page needs time to fulfill its purpose.
- Drift, combative threads, or spammy replies: weight the insightful content that does exist. Medium is appropriate if it is not potentially harmful.
- Sponsored "answers" that mimic real answers in format: counts as misleading page design, a Low quality signal.

---

## 2. AI-Generated Content — How Raters Evaluate It

The guidelines (including the September 2025 update) do not single out AI authorship as a quality signal in itself. **The method of creation does not determine quality; the output does.**

**AI content is rated by the same E-E-A-T and MC quality criteria as any other content:**

- Generative AI can produce both Highest and Lowest quality pages.
- High effort, originality, and added value using AI tools = can receive High or Highest.
- Lowest applies when AI tools are used to mass-produce pages with little to no effort, originality, or added value (see Scaled Content Abuse, Section 5 below).

**Specific Lowest triggers related to AI:**
- Pages using AI to generate fake "author" profiles — fabricated headshots or deceptive bio descriptions designed to make AI-written content appear human-written. This is Deceptive Design (Section 7 below).
- AI-paraphrased content from other sources, where the resulting page adds nothing new: rates Lowest even if the AI rewording is fluent and smooth.
- Mass pages created using AI where content "makes little or no sense to a reader but contains search keywords": Lowest.

**Important distinction:** Using AI does not automatically mean copied or low quality. Licensed, syndicated, or genuinely original AI-assisted work is not inherently Lowest. Ask: does the page provide meaningful added value a user could not find just as easily elsewhere?

---

## 3. News and Current Events Pages — Accuracy and Recency

### Freshness requirements

Some query types demand current results. Serving a stale page for these queries = FailsM:

| Query type | Examples | Staleness threshold |
|---|---|---|
| Breaking news | [tornado], [tsunami] | Hours; yesterday's update is useless |
| Recurring events | [olympics], [elections], [redsox schedule] | Must reflect the current or upcoming instance |
| Current-data queries | [population of paris], [airfare from NY to SFO] | Any outdated figure is misleading |
| Product queries | [iphone], [toyota camry] | Must cover the current model/version |

**Note:** Freshness matters more for Needs Met than for Page Quality. A well-maintained archive page can be High PQ even if the content is old — what matters is whether the content is presented as archival vs. current. An unmaintained or abandoned site with outdated and inaccurate information is a reason for Low PQ.

### Quality signals for news pages

- **Positive reputation:** Journalistic awards, a history of high-quality original reporting, recommendations by professional societies = strong evidence of High/Highest for news sites.
- **Source transparency:** Named authors, clear editorial standards, and correction policies support Trust.
- **YMYL scrutiny:** News coverage of elections, public health, and major civic issues is YMYL. Inaccurate or manipulative civic news can be Lowest even if the site looks professional.
- **Deceptive "news":** A page that looks like a news source but exists to manipulate users politically or monetarily is Deceptive Purpose — rate Lowest.
- **Page date vs. content date:** Note that some sites always display today's date regardless of when content was last updated. Use tools like the Wayback Machine to verify actual freshness. The date shown on page may not reflect when content was actually written.

---

## 4. Porn, Violence, and Sensitive Content — Safe-Search and "Upsetting-Offensive" Guidelines

### The Porn flag

- Assign the **Porn flag** to all porn pages regardless of the query. The flag is query-independent.
- Flag if the result block or landing page contains pornographic images, links, text, pop-ups, or prominent porn ads.
- What counts as porn can vary by culture/locale — use your judgment.

### Needs Met rating matrix for porn

| Query type | Approach |
|---|---|
| Clear non-porn intent | Porn result = FailsM + Porn flag. Applies to: [girls], [wives], [mature women], [cheerleaders], [moms and sons], [car pictures], etc. |
| Possible porn intent (e.g., [breast], [sex]) | Rate assuming the non-porn interpretation is dominant. A medical/anatomy result = HM; a porn result = FailsM + Porn flag |
| Clear porn intent queries | Rate on helpfulness for that query. Being porn + matching the query does not automatically = HM. Poor UX, malware risk, or mismatch with specific query = lower rating. |

**Important:** Even a clearly porn query does not make all porn pages equally helpful. A porn page that tries to download malicious software rates low regardless of content relevance.

### Violence and harmful content

Pages that encourage or depict violence against individuals or Specified Groups (race, religion, gender, etc.) = **Lowest** (Harmful to Self/Others or Harmful to Specified Groups). Key examples:
- Detailed realistic instructions for suicide or murder
- Content encouraging violence or ill treatment of a Specified Group
- Extremely offensive or dehumanizing stereotypes of a Specified Group

### Child pornography

Any image appearing to depict a minor in sexually explicit conduct must be reported immediately per employer instructions. This applies regardless of whether the image is photographic, animated, AI-generated, or drawn. When in doubt, report.

### Upsetting or offensive personal opinions

Sharing upsetting or offensive personal opinions can serve a beneficial purpose (allows appreciation of different perspectives). Apply the QRG standards, not personal reaction. However: if the content spreads misleading information or has potential for harm, the harm assessment overrides the "interesting perspective" framing.

---

## 5. Foreign Language Pages — Handling Language Mismatches

### Core principle

When a query is in the locale's language, assume users want results in that language. An English-language rater's ability to read a foreign page is irrelevant — rate from the perspective of typical locale users.

### When foreign-language results = FailsM or near-FailsM

- Hindi (IN) query returns English Wikipedia page: most Hindi users cannot read it = Fails to Meet, even if content is otherwise excellent.
- Query typed in Latin script (e.g., [ronaldo]) in Hindi (IN) locale: users still expect Hindi results.
- Query includes English words but is structurally a non-English query (e.g., [samsung tablet] in Korean (KR)): users expect the Korean Samsung page.

### When English results are acceptable in non-English locales

- Query targets a global organization whose official presence is English-only (e.g., Harvard website queried in Hindi).
- Technical information typically expressed in English (part numbers, chemical formulas, CLI commands in an IT tutorial).
- The locale officially uses English as a primary language (e.g., Singapore English (SG)).

### Foreign Language flag

Apply the flag to results that are not in: (a) the task language, (b) a language used significantly in the task location, or (c) English. Apply the flag even if you personally understand the language. Do not apply the flag for those three exceptions — e.g., for Catalan (ES) tasks, do not flag Catalan, Spanish, or English pages.

---

## 6. Thin Content Patterns — Doorways, Scraped Content, and Auto-Generated Pages

All forms below receive a **Lowest** rating. The mechanism of creation is secondary — if the output is low-effort, unoriginal, and adds no value, it is Lowest.

### Scaled Content Abuse (Section 4.6.5)

Creating many pages with little effort or originality, no editing, and no manual curation. Key patterns:

- Automated or AI-generated pages that produce volume without per-page value
- Scraped feeds, search results, or other sites' content (including through synonymizing, translating, or obfuscation)
- Stitching or combining content from multiple sources without adding value
- Multiple sites created to hide the scaled nature of the content
- Pages that make little sense to a reader but are keyword-stuffed

**If you strongly suspect scaled content abuse after reviewing several pages on a site, apply Lowest even if you cannot confirm the exact method of generation.**

### Copied/Scraped Content (Section 4.6.6)

Lowest applies when all or almost all MC is:
- Copied exactly from an identifiable source (full-page copies, multi-source stitching)
- Copied with minimal alteration (word replacements, sentence shuffling, image cropping to evade detection)
- Copied from dynamic sources (search result pages, news feeds — even without an exact matchable source)
- Paraphrased from one or multiple sources (manually or via AI), with no meaningful original contribution

**What is not "copied":** Licensed/syndicated content (e.g., AP newswire articles on a news site). Original AI-assisted content where real effort was applied.

### Cannot Determine Purpose / No MC

A page with no Main Content, gibberish MC, or MC so sparse it has no discernible purpose = Lowest.

### Expired Domain Abuse

Using an expired domain to rank content that takes advantage of the domain's prior reputation = Lowest / spam.

---

## 7. Deceptive Pages — Cloaking, Misleading Titles, Fake Reviews

**All deceptive pages = Lowest, regardless of other quality signals.** Untrustworthiness overrides everything.

### Three categories of deception

**Deceptive purpose:** Page appears to serve one purpose but actually exists for another.
- Fake "independent review" pages that are actually affiliate-driven with fabricated testing claims
- Product recommendation pages impersonating celebrity blogs
- "News article" format used to manipulate users for political or monetary gain

**Deceptive information about the website or content creator:**
- Impersonating another site (copied logos, mimic URLs)
- Non-satirical impersonator social profiles
- Fake celebrity personal sites created to monetize without celebrity permission
- Fake physical address / "brick and mortar" claims for online-only businesses
- AI-generated fake author profiles with fabricated images and bios
- Author profiles claiming false credentials (e.g., falsely claiming to be a medical professional)

**Deceptive design:**
- Ads disguised as Main Content or search results
- Ads disguised as navigation links (fake directory pages)
- Buttons/links designed to look functional (e.g., "close" button) but actually trigger downloads or other actions
- Misleading page titles with no relation to actual content

### Deliberately Obstructed MC

Lowest if MC is deliberately hidden or blocked by:
- Ads that continuously cover content as user scrolls and cannot be closed without clicking
- Pop-ups that obscure MC and require an action benefiting the site to dismiss
- Interstitials coercing downloads or clicks that harm the visitor
- Ads that push MC so far down most users would not notice it
- White-on-white text or other deliberate rendering tricks

Note: Paywalls and login requirements on trustworthy sites are NOT deceptive. Many high-quality sites require subscription to survive.

---

## 8. Mobile vs. Desktop Quality — Evaluation Differences

The QRG does not define separate quality rating scales for mobile vs. desktop. However:

- **Tasks are framed around mobile users.** Raters are consistently told to "think about users typing or speaking queries into their phone."
- **Monetization visibility differs.** Ads on mobile pages may be more subtle than on desktop — raters must disable ad blockers and rate what actual users experience.
- **Result blocks designed for mobile context** (e.g., showing map pins, phone numbers, directions for local results) should be evaluated for helpfulness on the device context implied by the query.
- **Interstitials and pop-ups** that are hard to dismiss on mobile count against PQ; judge based on the experience a real user on that device type would have.
- **Some examples in the guidelines show mobile screenshots and some desktop.** Where the task implies mobile (voice queries, location queries, on-the-go intent), evaluate from a mobile user's perspective.

**Practical rule:** No separate rating scale, but queries with clear on-the-go or micro-moment intent (e.g., [gas station near me], [emergency vet]) should be evaluated assuming mobile usage, where friction (slow loading, hard-to-close ads, no click-to-call) is especially harmful.

---

## 9. Page-Level vs. Site-Level Signals — When Site Reputation Affects a Page's Rating

### The page is the primary unit of evaluation

You are rating the landing page, not the homepage. A high-quality site does not automatically elevate a low-quality page, and a page can be High quality on a site with a mixed reputation.

### When site reputation applies to the page

- **Extremely negative site reputation** means all pages on that site are Lowest — regardless of what the individual page contains. If the site has credible evidence of fraud, criminal behavior, or systematic manipulation, no individual page can escape that.
- **Positive site reputation** strengthens confidence in individual page quality, especially for YMYL topics where the rater needs external signals to assess trustworthiness.
- **Site Reputation Abuse** (Section 4.6.4): A third-party page published on a high-authority host site primarily to capitalize on that host's ranking signals = Lowest/spam. The content would not rank on its own; it's parasitically hosted. Examples: "best casinos" page on a medical site; coupon page using a news site's authority.

### What is NOT site reputation abuse

- Forum/UGC sites hosting user-generated content
- News sites syndicating from AP or Reuters
- Editorial columns, op-eds, native advertising aimed at readers (not just at ranking)
- Affiliate links treated appropriately, or standard ad units

### Site-level signals in practice

- Research the reputation of the **entire website** for the relevant topic, not just the page type it appears in.
- A site known for authoritative tech reviews may be untrustworthy for financial advice. Always align the reputation research to the topic of the page being rated.
- Positive reputation indicators: awards, expert society recommendations, history of high-quality original reporting, trusted by multiple credible external sources.
- Negative indicators: fraud reports, user complaints about not receiving goods/services, legal actions, negative coverage on watchdog or consumer protection sites.

---

## 10. Common Rating Mistakes — Pitfalls the Guidelines Specifically Warn Against

### Trusting search ranking as a quality signal

> "Do not assign a high rating to a webpage just because it appears at the top of a list of search results on Google."

A page ranking highly is not evidence it is high quality. Rating must be independent of current search rankings.

### Judging quality by visual appearance alone

The guidelines explicitly warn against a superficial "does it look good?" approach. A polished design can mask Lowest-quality content. Pages that initially look Low may turn out High on careful inspection — and vice versa.

### Using personal offense as a quality signal

A page sharing an opinion that is upsetting, offensive, or distasteful to the rater is not automatically Low quality. Apply the QRG's harm standards — not personal reaction. However: harm assessment overrides this; if the content causes real harm, rate accordingly.

### Conflating Needs Met with Page Quality

These are distinct ratings. A page can have High PQ but fail to meet the query (e.g., a high-quality medical encyclopedia article returned for [atm near me]). Always assess both dimensions independently.

### Assuming page type determines quality tier

- Celebrity gossip pages can be High quality.
- Forum pages can be Highest quality.
- Encyclopedia articles can be irrelevant or Low for many queries.
- There is no page type that is inherently High or inherently Low.

### Conflating "copied" with all reproduction

Licensed syndicated content (AP wire articles) is not copied content. Legitimate paraphrasing by experts adding genuine value is not thin content. The key test is: does the page add meaningful value for users beyond what they'd get from the source?

### Over-flagging Foreign Language

Do not apply the Foreign Language flag when the page is in the task language, English, or a language widely spoken in the task region. Personal ability to read the language is irrelevant to whether the flag should be applied.

### Skipping reputation research on unfamiliar sites

For YMYL pages especially, you cannot rate trust without researching the site. If something feels deceptive but you cannot confirm it, explore more pages, run reputation searches. Pattern of deception across multiple pages is grounds for Lowest. When in doubt and safety seems at risk, apply Lowest and leave immediately.

### Not disabling ad blockers

Ads are part of the page experience. Rating with an ad blocker gives incorrect results — you will not see obstructive or deceptive ad placements that are material to PQ rating.

### Giving Lowest only when harm can be "proven"

The guidelines explicitly allow Lowest based on strong suspicion of malicious intent, scams, or harmful behavior. You do not need proof. If you strongly suspect harm, rate Lowest.

### Mishandling queries with dual intent (website + visit-in-person)

For queries like [target], [citibank], [dmv], there are two equally strong intents: visit the website and visit in person. A result satisfying only one intent cannot receive Fully Meets. Results must address both intents to qualify for that top rating.

---

*Source: Google Search Quality Evaluator Guidelines, September 2025. Sections: 4.5, 4.6, 9.3, 11.0, 15.0–15.4, 18.0, 23.0, and cross-cutting guidance throughout.*
