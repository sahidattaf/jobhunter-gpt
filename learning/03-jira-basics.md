# Pack 03 — Jira Basics

**Status:** Not Started
**Honest starting position:** No Jira experience.

---

## Skill Goal

Understand Jira's core concepts — issue types, projects, workflows, statuses, sprints,
boards, and epics — well enough to speak about them in a technical interview and to
demonstrate you understand how project management data connects to AI platforms.

Build a mock Jira-style workflow for JobHunterGPT using a format you already know
(CSV or Notion) to demonstrate the concepts without needing Jira access.

---

## Why It Matters for Proofpoint-Style Roles

Proofpoint's JD named Jira alongside Salesforce as a system the AI Integration
Specialist must connect to:

  "Connect, shape, and manage data pipelines between business systems such as
   Salesforce, Totango, Jira, Redshift, and Snowflake and the AI platform."

In a Customer Office context, Jira typically tracks support tickets, service requests,
feature requests, and technical account management tasks. Understanding the data
model is required to design how an AI agent would query or surface Jira data.

---

## What Sahid Can Honestly Say Now

Nothing about Jira. Do not claim it until this pack is at Evidence Ready.

Adjacent experience that is honest:
- Built GitHub-based task tracking for personal projects (issues, branches, commits).
- Organized project workflows in Notion with status tracking.
- Managed JobHunterGPT as a structured multi-module project with task dependencies.

---

## What Sahid Cannot Claim Yet

- Any hands-on Jira experience (admin, user, or developer).
- Any Jira integration, API, or automation work.
- Any Jira certification or Atlassian experience.

---

## Three Learning Tasks

**Task 1: Learn Jira's core concepts.**
Study: Issue, Project, Board (Scrum vs. Kanban), Epic, Story, Task, Bug, Sprint,
Backlog, Status (To Do / In Progress / Done), Assignee, Reporter, Priority, Label.
Free resource: Atlassian documentation (atlassian.com/software/jira/guides) —
free to read, no account required.
Write a plain-English definition for each term (1 sentence each).
Save as: `learning/evidence/03-jira-concepts.txt`

**Task 2: Understand how AI connects to Jira.**
Research: What does it mean to pull Jira data into an AI workflow?
- What is the Jira REST API?
- What fields from a Jira issue would a Customer Success AI agent care about?
  (e.g. issue type, status, priority, assignee, created date, summary, description)
- What would a useful Jira-to-AI query look like?
  (e.g. "Show me all open P1 support tickets assigned to my accounts")
Write 5 bullet points summarizing what you learned.
Save as: `learning/evidence/03-jira-ai-integration-notes.txt`

**Task 3: Build a mock Jira-style task board for JobHunterGPT.**
Create a CSV or Notion database that tracks JobHunterGPT development tasks
in Jira format.

Required columns:
  Issue ID | Type (Task/Bug/Feature) | Summary | Status | Priority |
  Assignee | Sprint | Created | Updated | Labels | Notes

Populate with 10 real tasks from JobHunterGPT development (use git log or
your memory of what was built).
This demonstrates you understand Jira's data model.
Save as: `learning/evidence/03-mock-jira-board.csv`

---

## Mini Demo Task

In a practice interview setting, answer this question:
"Have you worked with Jira before?"

Honest answer to practice:
"I haven't used Jira professionally, but I understand its data model — issues,
epics, sprints, workflows, and the status transitions that move work through a
board. I've managed project workflows in GitHub and Notion that follow the same
structure. As a learning exercise I created a mock Jira board tracking my own
AI project tasks. I'm confident I can get productive on Jira quickly."

Practice until natural and not defensive.

---

## Evidence to Collect

- [ ] `learning/evidence/03-jira-concepts.txt` — definitions of core terms
- [ ] `learning/evidence/03-jira-ai-integration-notes.txt` — integration research
- [ ] `learning/evidence/03-mock-jira-board.csv` — mock task board for JobHunterGPT

---

## Completion Criteria

- Can name 10 core Jira terms and explain each in one sentence.
- Can explain how Jira data connects to an AI agent in 2 sentences.
- Mock Jira board exists with 10 real tasks in correct column structure.
- Can answer "Have you used Jira?" honestly and without stumbling.

---

## Interview Sentence After Completion

"I haven't used Jira in a professional role, but I understand its issue and
workflow model. I organized a mock Jira board for my own AI project as a learning
exercise and can speak to how Jira data would integrate with an AI platform's
knowledge base. I'd expect to be comfortable in Jira within a week of access."
