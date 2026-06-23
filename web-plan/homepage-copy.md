# Homepage Copy — JobHunterGPT

Public-safe. No private data. No resume content. No application packages.
Review against privacy-rules.md before publishing.

---

## Meta

**Page title:** JobHunterGPT — Human-in-the-Loop AI Job Preparation
**Meta description:** A local Python prototype that automates job application
preparation while keeping a human in the loop at every step. Built by Sahid
Attaf, AI systems builder, Curaçao.

---

## Hero Section

**Headline:**
JobHunterGPT

**Subheadline:**
A human-in-the-loop AI pipeline for job application preparation.
Built from scratch. Tested with 70 automated tests. Never submits anything automatically.

**Two CTAs:**
- [See the Demo →]  links to /demo
- [View on GitHub →]  links to public GitHub repo

---

## What It Is

**Section heading:** What is JobHunterGPT?

**Body:**
JobHunterGPT is a local Python prototype that automates the preparation side
of a job search while keeping a human in the loop at every step.

It reads a job description and a candidate profile, extracts ATS keywords,
calculates a fit score, generates a cover letter draft from verified facts
only, and runs a structural reviewer before any file can be used.

It does not submit applications automatically.
It does not invent qualifications.
It does not access the internet during the core pipeline.

---

## Key Stats

Four stat blocks in a row:

| Stat | Label |
|------|-------|
| 8 | Python Modules |
| 70 | Automated Tests |
| 10 | Reviewer Checks |
| 0 | Auto-submissions |

---

## The Design Principle

**Section heading:** Human review at every step.

**Body:**
Every output the system generates — the cover letter, the fit score report,
the ATS keyword analysis — must pass a structural review before it can be used.

The package reviewer runs ten checks. If an ERROR-level check fails, the
package is marked NEEDS_FIXES and the pipeline stops. If it passes, the
package is marked READY_FOR_HUMAN_REVIEW — not READY_TO_SEND.

The human reads it. The human decides. The system prepares, not acts.

---

## Builder Section

**Section heading:** Built by Sahid Attaf

**Body:**
I'm an AI systems builder based in Willemstad, Curaçao. For the past five years
I've been designing and building AI-powered workflow systems for real business
problems — in hospitality operations, real estate development, and business
automation.

JobHunterGPT is the clearest example of how I think about AI workflow design:
structured input, rule-based validation, generation from verified facts only,
and a human checkpoint before any output is used.

I built it while job searching — which meant every module had to actually work
before I moved to the next one.

**Tools:** Python · Claude Code · GitHub · VS Code

**Link:** [LinkedIn →] | [GitHub →]

---

## Pipeline Overview (Simplified)

**Section heading:** How it works in 5 steps.

1. Read the job description → extract ATS keywords
2. Compare keywords against the candidate profile → calculate fit score (0–100)
3. Pull verified facts from the resume → generate cover letter draft
4. Package all outputs into a dated folder
5. Run 10 structural checks → return READY_FOR_HUMAN_REVIEW or NEEDS_FIXES

**CTA:** [See the full architecture →]  links to /how-it-works

---

## What This Proves

**Section heading:** What this project demonstrates.

**Three cards:**

**Card 1: AI Workflow Design Thinking**
Multi-step pipeline with separation of concerns. Each module does one thing.
The orchestrator calls them in sequence. The output is predictable and auditable.

**Card 2: Responsible AI Output Handling**
No AI output goes directly to the user without a structural check. The system
distinguishes between ERROR-level problems (block the package) and WARNING-level
notes (advisory only). Human judgment is the final gate.

**Card 3: Independent Technical Execution**
Built on Python's standard library — no external dependencies for the core
pipeline. 70 unit tests. Documented modules. Maintained in a public GitHub
repository.

---

## Footer

Sahid Attaf — AI Systems Builder — Willemstad, Curaçao
[GitHub] [LinkedIn] [Contact]

JobHunterGPT is a local prototype, not a commercial product.
It is not affiliated with any job board, ATS platform, or employer.
