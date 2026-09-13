# LinkedIn Posts — Kapil Mandru

Reference log of published LinkedIn posts (Managing Consultant | SAP EWM / TM Consultant), kept for style/context reference when drafting future posts.

---

## 2026-08 (posted ~4w before 2026-09-13, edited)

**Hook:**
> "Why doesn't TM work? IT should fix it."

**Body:**

I hear a version of this sentence in almost every SAP TM project.

And almost every time, the root cause isn't the system. It's the data feeding it.

SAP TM depends entirely on clean, complete master data to make good planning decisions:
→ Resource capacities
→ Ownership fields
→ Ship-to master data
→ Means of Transport classification
→ Freight agreements

When any of these are missing or incomplete, the symptoms show up downstream — and they always look like "the system is broken":
✗ Incompatibilities don't trigger
✗ Transportation planning fails
✗ Freight cost calculation is wrong
✗ Business ends up with poor, unreliable decisions

Here's the pattern I see over and over:
Business says: "The system doesn't work."
IT says: "The required master data is missing."
Both are right. Neither is the full picture.

You cannot compensate for poor master data through customizing. No amount of clever configuration fixes a Freight Agreement count of zero, or Ship-to data missing for hundreds of customers. Garbage in, garbage out — TM can only plan as well as the data allows it to.

The fix isn't more customizing. It's shared responsibility:
Good data + good configuration + clear business rules = reliable TM planning.

If you're implementing SAP TM (or any planning-heavy SAP module), get master data ownership on the table on day one — before the first line of customizing gets built. It will save you the "why doesn't it work" conversation six months later.

What's the master data issue that's slowed down your project the most?

#SAPTM #TransportationManagement #SAP #SupplyChain #MasterData #Consulting

**Visual:** Accompanying graphic — a two-panel "comic" style illustration titled "MASTER DATA QUALITY IS UNDERESTIMATED BY BUSINESS", showing a Business person and an IT/TM Consultant arguing across a table. Table columns compare 5 master data areas (Resource Capacities, Ownership Fields, Ship-to Data (790/791), MoT Classification, Freight Agreements) each marked incomplete/missing/not maintained/=0. Bottom banner: "POOR MASTER DATA = POOR RESULTS" / "GOOD DATA + GOOD CONFIGURATION + CLEAR BUSINESS RULES = RELIABLE TM PLANNING" / "SHARED RESPONSIBILITY. BETTER DATA. BETTER RESULTS."

**Themes/style notes:**
- Opens with a quoted, provocative line business stakeholders actually say
- Structures the problem with arrow/checkmark/X bullet lists
- Uses a "Business says / IT says" framing to show both sides are partially right
- Ends with a discussion-prompting question + hashtag block
- Pairs the post with an explanatory infographic/illustration
