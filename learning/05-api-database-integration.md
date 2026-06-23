# Pack 05 — API / Database / Supabase / PostgreSQL / Data Integration

**Status:** Not Started
**Honest starting position:** Verified existing experience with API/database/Supabase/PostgreSQL.
**Goal:** Deepen, document, and make this experience demonstrable for AI integration roles.

---

## Skill Goal

Document and extend Sahid's verified API and database experience into a concrete,
showable artifact that demonstrates how structured data moves between business systems
and an AI platform — the exact problem Proofpoint's AI Integration Specialist solves.

Build a local demo plan showing how JobHunterGPT's CSV data could migrate to a
database-backed structure with an API layer, and map this to the enterprise pattern
the JD describes.

---

## Why It Matters for Proofpoint-Style Roles

Proofpoint's JD: "Connect, shape, and manage data pipelines between business systems
such as Salesforce, Totango, Jira, Redshift, and Snowflake and the AI platform.
Design data flows that ensure agents and workflows have the right data at the right
time, including field mapping, transformation logic, and ongoing data quality management."

This is the most technically demanding section of the JD. The candidate must understand:
- How data moves between systems (APIs, connectors, exports)
- How data is shaped before it reaches the AI (field mapping, transformation)
- How data quality is maintained over time

Sahid's existing API/database/Supabase/PostgreSQL experience is a real differentiator
here. This pack turns that experience into documented, demonstrable proof.

---

## What Sahid Can Honestly Say Now

- Has worked with APIs (confirmed — record specific examples here).
- Has worked with Supabase and PostgreSQL (confirmed — document the project).
- Understands structured data, queries, and how data moves between systems.
- JobHunterGPT currently uses a CSV tracker — understands the migration path to
  a database-backed system.

ACTION REQUIRED: Fill in the specific projects, dates, and tools before claiming
this in an interview. The evidence files below are the place to record this.

---

## What Sahid Cannot Claim Yet

- Salesforce API, Jira REST API, Redshift, or Snowflake experience (not verified).
- Enterprise-scale data pipeline work (ETL, data warehousing, CDC).
- Production database administration (unless specifically done).
- Cloud data platform experience (AWS Glue, dbt, Airflow, etc.).

---

## Three Learning Tasks

**Task 1: Document your existing API and database experience.**
Write a factual summary of every API or database project you have worked on.

For each project record:
  Project name | Year | What API or database | What you built/did | Outcome | Can you show it?

Be specific. "I worked with Supabase" is not enough. "I used Supabase to store
[X] for [Y project], querying with PostgreSQL and exposing [Z] via a REST endpoint"
is what hiring managers want.
Save as: `learning/evidence/05-api-database-experience.txt`

**Task 2: Map the Proofpoint data flow to your experience.**
Draw (in text format) the data flow the JD describes:

  [Salesforce] ──API──> [AI Platform (Amazon Quick)] ──query──> [AI Agent] ──answer──> [User]

Then draw an equivalent flow using tools you have worked with:

  [Supabase / PostgreSQL / CSV] ──API/query──> [Python script / Claude API] ──> [Output]

This shows the interviewer you understand the pattern, even if you haven't used
Salesforce specifically.
Save as: `learning/evidence/05-data-flow-diagram.txt`

**Task 3: Build the migration plan for JobHunterGPT.**
Write a step-by-step plan for migrating JobHunterGPT's `data/applications.csv`
tracker to a Supabase/PostgreSQL-backed database.

Include:
  a. Schema design (table name, columns, types matching the CSV columns)
  b. Migration script outline (CSV → INSERT INTO applications)
  c. Query examples (SELECT applications WHERE status = 'Prepared')
  d. API endpoint design (GET /applications, POST /applications)
  e. How an AI agent would query this database to answer "What applications are pending?"

This does not need to be built yet — the plan is the deliverable.
Save as: `learning/evidence/05-jobhuntergpt-database-migration-plan.txt`

---

## Optional Extension: Build It

If time permits, implement the migration plan:
  1. Create a Supabase project (free tier available).
  2. Create the applications table using the schema from Task 3.
  3. Write a Python script (`data_migration.py`) that reads `applications.csv`
     and inserts rows into Supabase via the Python client.
  4. Write a query that returns all "Prepared" applications.
  5. Document the working demo.

This would turn Pack 05 into a genuine, showable demo for technical interviews.
Save implementation in: `data_migration.py` (root of project)

---

## Mini Demo Task

In a practice interview setting, answer this question:
"Tell me about your experience connecting data systems to AI platforms."

Honest answer structure:
1. Name a specific project where you used an API or database.
2. Describe what the data was, how it moved, and what the AI did with it.
3. Connect it to the pattern the JD describes.
4. Be honest about what scale you've worked at.

Do not claim Salesforce or enterprise-scale experience. Do name Supabase and
PostgreSQL specifically if you have used them.

---

## Evidence to Collect

- [ ] `learning/evidence/05-api-database-experience.txt` — documented experience
- [ ] `learning/evidence/05-data-flow-diagram.txt` — pattern mapping
- [ ] `learning/evidence/05-jobhuntergpt-database-migration-plan.txt` — migration plan
- [ ] (optional) `data_migration.py` — working implementation

---

## Completion Criteria

- Can describe at least one specific API/database project with name, year, and outcome.
- Can draw the data flow pattern from a business system to an AI agent in text.
- Migration plan for JobHunterGPT exists and is technically coherent.
- Can answer "What experience do you have connecting data systems to AI?" with
  specific, dated examples.

---

## Interview Sentence After Completion

"I've worked with Supabase and PostgreSQL on [specific project] and have built
[specific integration]. For JobHunterGPT I designed a migration path from CSV
to a database-backed architecture with an API layer — which maps directly to the
kind of data orchestration described in this role. I haven't worked with Salesforce
or Redshift specifically, but the data pipeline pattern is one I understand and
have applied."
