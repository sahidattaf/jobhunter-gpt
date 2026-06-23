# Interview Demo Answers — JobHunterGPT

Six practice answers for questions an interviewer will ask during or after
the JobHunterGPT demo. These are honest, specific, and rehearsable.

**Practice each answer out loud. Goal: under 60 seconds per answer.
Adjust to your own voice. Do not read from a script.**

---

## Question 1: "Can you show me what you built?"

**Answer:**

"Yes — let me share my screen. This is JobHunterGPT, a local Python prototype
I built to automate the preparation side of a job search while keeping a human
in the loop at every step. I'll show you the structure, run the test suite,
and then run the package reviewer on a generated output. That's about five
minutes. Ready?"

**Then run the demo script.**

**Why this works:**
It is direct. It gives the interviewer a clear preview of what they're about
to see. The phrase "local Python prototype" sets honest expectations before
anything runs.

---

## Question 2: "What problem does JobHunterGPT solve?"

**Answer:**

"The problem it solves is that job applications are time-consuming to prepare
honestly. The default temptation is to either over-claim or under-sell, and
both hurt. JobHunterGPT helps a candidate prepare material that is anchored
to verified facts — it extracts keywords from the job description, scores how
well the candidate's profile matches, generates a cover letter draft from the
resume text rather than from thin air, and then runs a structural reviewer
before any file gets used. At every step, the human makes the decision. The
system flags issues. It never submits anything.

The fit scorer is an example of the honest design: when I ran it on a real
Proofpoint job description, the score came back 35 out of 100. That is the
correct result given my current keyword match — and the system reporting that
honestly is more useful than a system that inflates the score to feel
encouraging."

**Why this works:**
It names the problem, explains the design, and uses a real, honest outcome
as evidence. The 35/100 Proofpoint score demonstrates the system is calibrated
for accuracy, not validation.

---

## Question 3: "What did you personally build?"

**Answer:**

"Everything in the repository. There are eight Python modules — I designed
and wrote each one. `keyword_extractor.py` uses regex and frequency analysis
to pull ATS terms from job descriptions. `fit_scorer.py` calculates a
0-to-100 score across keyword overlap, verified skills, location, and remote
preference. `coverletter_generator.py` extracts the Professional Summary
from the resume and builds a structured letter with verified strengths only —
no invented claims. `package_reviewer.py` runs ten structural checks and
returns either READY_FOR_HUMAN_REVIEW or NEEDS_FIXES. `job_search_agent.py`
orchestrates all of them. The test suite has 70 tests covering all modules.

I used Python's standard library throughout — no external dependencies for
the core pipeline. I built it while actively job searching, which meant each
module had to actually work before I moved to the next one."

**Why this works:**
Module names and design decisions are specific. "No external dependencies"
is a technical choice that demonstrates judgment. "Each module had to actually
work" explains the test-driven approach without the jargon.

---

## Question 4: "How do you test it?"

**Answer:**

"There are 70 unit tests in `tests/test_core.py`, organized by module. The
profile validation tests check that invalid emails, placeholder names, and
missing required fields all raise the right errors. The cover letter tests
verify the generator never produces raw keyword dumps — that was a real bug
in version one that I caught with a test. The package reviewer tests cover
all ten checks independently, including the separation between ERROR-level
issues that block the package and WARNING-level issues that are advisory.

I run the full suite before and after any change. I ran it just now — 70
tests, all passing. If a test fails, I fix the code, not the test."

**Why this works:**
"That was a real bug in version one that I caught with a test" is a concrete
example of test-driven development in practice. "I fix the code, not the test"
is a statement of professional judgment.

---

## Question 5: "How does this relate to AI integration?"

**Answer:**

"It demonstrates the core pattern of AI integration work at a small scale:
you have structured input data, a set of business rules about what is and
isn't acceptable in the output, a generation step that produces a draft,
and a validation layer that checks the draft before it goes anywhere.

In an enterprise context — say, an AI platform like Amazon Q connected to
Salesforce and a knowledge base — the same pattern applies at much larger
scale. The data comes from CRM records and document stores instead of a
resume and job description. The business rules are about what the AI can
and cannot say to a customer instead of what the cover letter can claim.
The validation layer is more sophisticated, but the principle is the same.

What this project shows is that I think about AI workflows in terms of
inputs, rules, generation, validation, and human decision points — which
is the design pattern enterprise AI integration roles require. I haven't
built that at enterprise scale. I've built it here, at a level I can show
you directly."

**Why this works:**
It maps the local prototype to the enterprise pattern honestly. It names
Amazon Q and Salesforce as the enterprise analogs without claiming experience
with them. The closing sentence is honest about scale while still asserting
the transferable insight.

---

## Question 6: "What would you improve next?"

**Answer:**

"A few things, in order of impact.

First, the cover letter generator. Right now it builds from the resume text
and profile skills, but it doesn't have access to the Claude API in the core
pipeline — everything runs on Python's standard library. Adding a Claude API
call for the drafting step would produce significantly stronger letter text
while keeping the same verification and review logic.

Second, the data layer. The tracker currently writes to a CSV file. Migrating
it to a Supabase or PostgreSQL backend would make the data queryable and would
let an AI agent answer questions like 'which applications are still pending?'
— which is a natural extension of the workflow.

Third, the fit scorer. The current keyword extractor is regex-based, which
works but misses semantic matches. A company like Proofpoint uses 'independently
drive AI solution delivery' in their JD — that maps to my founder experience,
but the regex doesn't know that. A semantic similarity layer would produce
much more useful scores.

What I'd improve last is the UI — the system currently runs in a terminal.
That is fine for me. It would not be fine for a non-technical user."

**Why this works:**
Each improvement is specific, grounded in the actual system, and demonstrates
forward thinking. The Claude API extension shows understanding of how to use
LLMs appropriately. The Supabase/database mention maps to Pack 05. The fit
scorer limitation is honest and technically precise. The UI comment at the end
is honest without being self-deprecating.
