# Pack 04 — Cybersecurity Awareness

**Status:** Not Started
**Honest starting position:** No cybersecurity experience.
**Target level:** Awareness — not practitioner. Do not overclaim.

---

## Skill Goal

Understand the basic security concepts that matter in Proofpoint's domain well enough
to (a) speak intelligently in an interview without embarrassing yourself, and (b)
apply security-aware thinking to the AI workflows you build going forward.

This pack does not make you a cybersecurity professional. It makes you a non-specialist
who understands the landscape and applies responsible practices in your work.

---

## Why It Matters for Proofpoint-Style Roles

Proofpoint is a cybersecurity company. Even a non-security role requires understanding
why the company exists and what problems it solves. An AI Integration Specialist at
Proofpoint is building workflows that touch sensitive customer data, enterprise email
systems, and internal business tools.

Relevant awareness areas from the JD:
- The role involves "access controls and workspace organization."
- Platform administration includes "data connector setup" — which touches data security.
- Proofpoint protects against "threats, data loss, and email attacks."

An interviewer will expect you to understand what data loss prevention means and to
care about not building insecure AI workflows.

---

## What Sahid Can Honestly Say Now

Nothing about cybersecurity. Do not claim it until this pack is at Evidence Ready.

Adjacent experience that is honest:
- JobHunterGPT is designed with human-in-the-loop principles — no auto-submission.
- Secrets are stored in environment variables (.env), not source code.
- Private data (resume, profile, applications) is gitignored.
- The design philosophy prioritizes verified data over automation.

These are real, honest security-adjacent practices that can be described accurately.

---

## What Sahid Cannot Claim Yet

- Any cybersecurity certification (CompTIA Security+, CISSP, CEH, etc.).
- Any penetration testing, vulnerability assessment, or security engineering work.
- Any specific experience with Proofpoint's products.
- Any enterprise security incident handling or SOC work.

---

## Three Learning Tasks

**Task 1: Learn the five core Proofpoint-relevant security concepts.**

Research and write a 2-3 sentence plain-English explanation of each:

  a. Phishing — What is it? Why is it dangerous? How does Proofpoint address it?
  b. Data Loss Prevention (DLP) — What is it? What data is protected? How?
  c. Email Security — What threats does email security protect against?
  d. Access Control / Least Privilege — What does it mean? Why does it matter for AI?
  e. Secure Workflow Design — What makes an AI workflow "secure"? What are the risks?

Free resources:
  - Proofpoint's own blog (proofpoint.com/us/blog) — read 3 articles
  - SANS Internet Stormcast (free, 5 minutes per day)
  - NIST Cybersecurity Framework overview (free, csrc.nist.gov)

Save as: `learning/evidence/04-security-concepts.txt`

**Task 2: Apply security thinking to JobHunterGPT.**
Write a 1-page "Secure Workflow Checklist" for AI workflow systems based on what
you learn. Map each practice to something JobHunterGPT already does or should do.

Example format:
  Practice: Store API keys in environment variables, not source code.
  JobHunterGPT status: Done — .env is gitignored.

  Practice: Require human approval before any external action.
  JobHunterGPT status: Done — no auto-submission anywhere in the system.

  Practice: Log all AI-generated outputs before use.
  JobHunterGPT status: Partial — output files are created for review.

Save as: `learning/evidence/04-secure-workflow-checklist.txt`

**Task 3: Read one Proofpoint case study or product page.**
Read one page on proofpoint.com that describes how a customer uses Proofpoint's
products. Write 5 bullet points: what the customer's problem was, what Proofpoint
solved, and what data or workflows were involved.
Save as: `learning/evidence/04-proofpoint-product-notes.txt`

---

## Mini Demo Task

In a practice interview setting, answer this question:
"Why do you want to work at a cybersecurity company if you don't have a security
background?"

Honest answer to practice:
"I don't come from a security background, and I won't pretend otherwise. What
draws me to Proofpoint specifically is that the role is about AI integration and
business consulting within the customer office — applying AI to workflow problems.
The security context matters because it means the data and workflows I'd be building
on need to be handled responsibly. I've applied that principle in my own work —
keeping private data out of source control, requiring human approval before any
automated action, and building systems that don't make decisions the human hasn't
authorized. I'd expect to deepen my security knowledge significantly on the job."

---

## Evidence to Collect

- [ ] `learning/evidence/04-security-concepts.txt` — 5 core concepts explained
- [ ] `learning/evidence/04-secure-workflow-checklist.txt` — applied to JobHunterGPT
- [ ] `learning/evidence/04-proofpoint-product-notes.txt` — product research notes

---

## Completion Criteria

- Can explain phishing, DLP, email security, access control, and least privilege
  in plain English in under 30 seconds each.
- Can name two specific security practices already present in JobHunterGPT.
- Can answer "Why Proofpoint?" in a way that is honest about the lack of security
  background without sounding unprepared.

---

## Interview Sentence After Completion

"I don't have a cybersecurity background, but I understand the domain well enough
to know why Proofpoint's work matters. I've also applied security-aware practices in
my own AI work — private data stays out of source control, nothing is submitted
automatically, and human review is built into every workflow. I'd treat the same
principles at a much larger scale in this role."
