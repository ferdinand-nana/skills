---
name: sr-interview-generator
description: Generate interview questions for senior software engineers based on their CV, focusing on real experience, decision-making, and measurable outcomes to validate **real experience**, not memorized knowledge.
---

## Categories

Generate **5 questions per category**, except Exploration (2-3 questions):

1. Exploration (HR Interview) — the candidate's most recent 2-4 years: role changes, current responsibilities, why they're looking to move
2. Technical Expertise (Java, Spring Boot, Backend Development)
3. Problem Solving, Debugging & Root Cause Analysis
4. Testing, Quality & Continuous Improvement
5. Agile Team Collaboration
6. Team Leading & Team Impact
   - Team Lead → leadership, mentoring, delivery ownership
   - Senior Engineer (non-lead) → technical ownership, influence, decision making
   - Mid-level/Junior → collaboration, teamwork, contribution

Use these exact labels as the keys inside `categories` in `answers.json`.
The generator normalizes them to the shorter placeholder names used by the docx template internally, so do not shorten or rename them in the payload.

### Recency Priority

Favor the candidate's **most recent role(s)** as the source of questions in every category. Only reach into older roles when the most recent role doesn't have enough material to fill 5 solid questions for a category.

### Team Leading Fallback

If the CV has no explicit team-leading experience:

1. First question: ask whether they've led a team or owned a feature end-to-end.
2. Remaining questions: follow up based on their answer, using whatever ownership/collaboration evidence the CV does support (e.g. driving a feature, mentoring, cross-team coordination).

---

## Question Requirements

Questions must:

- Be based on the candidate's actual experience in the CV
- Require real project examples
- Be difficult to answer using AI-generated generic responses
- Focus on decisions, tradeoffs, failures, lessons learned, and measurable outcomes
- Avoid textbook questions and definitions
- Avoid questions such as:
  - "What is Spring Boot?"
  - "Explain microservices"
  - "What is dependency injection?"
- Be concise and easy to understand — one sentence, one clear ask, plain wording, no jargon stacking, no run-on multi-part questions

---

## Good Question Patterns

Prefer patterns such as:

- Tell me about a time when...
- Walk me through a real example...
- What alternatives did you consider and reject?
- What made this problem difficult?
- How did you know your solution worked?
- What would you do differently today?
- How did you convince others?
- What evidence led you to the root cause?
- What tradeoff did you intentionally accept?

---

## Expected Answer Requirements

For each question, describe what a strong answer should contain:

- Context
- Technical reasoning
- Tradeoff analysis
- Evidence used
- Outcome
- Lessons learned
- Team and business impact

---

## Output Format

Output is a filled-in copy of the docx template in `template/`, not markdown. Use the `scripts/` helpers instead of hand-rolling docx XML:

- `scripts/read_docx.py <cv.docx>` / `scripts/read_pdf.py <cv.pdf>` — dump the candidate's CV to plain text for analysis (install deps once with `pip install -r scripts/requirements.txt`).
- `scripts/generate_interview_doc.py <answers.json> [output.docx]` — fills the template from a JSON file and writes the finished docx. It handles:
  1. Copying the template and replacing `[Name]` / `[Career Experience]` in the summary table.
  2. Replacing each `[<Category> Questions]` placeholder paragraph with a `Question` | `Expected Answer` table.
  3. Per question: the CV-derived context clause **bold italic**, the question clause **highlighted yellow**, and a bulleted notes row after every question row for interviewer note-taking.

### File Naming

When processing multiple candidates, name JSON files by lowercase surname:

- `answers_doe.json` → generates `Interview Notes - Senior Software Developer - Jane Doe.docx`
- `answers_smith.json` → generates `Interview Notes - Senior Software Developer - John Smith.docx`

This avoids overwriting when batch processing.

### Years of Experience

Calculate `years_experience` from the CV's earliest relevant software role to present. Round to nearest whole number. Exclude non-engineering roles (support, IT staff) unless they involved development.

`answers.json` should look like this:

```json
{
  "name": "Jane Doe",
  "years_experience": "6",
  "categories": {
    "Exploration (HR Interview)": [...],
    "Technical Expertise (Java, Spring Boot, Backend Development)": [...],
    "Problem Solving, Debugging & Root Cause Analysis": [...],
    "Testing, Quality & Continuous Improvement": [...],
    "Agile Team Collaboration": [...],
    "Team Leading & Team Impact": [...]
  }
}
```

Legacy short-form category keys remain supported by the script for backwards compatibility, but prefer the exact labels above.

### Validation

Before finalizing the deliverable:

1. Run `python3 scripts/generate_interview_doc.py <answers.json> [output.docx]`.
2. If the script reports unknown or missing categories, treat that as a payload-contract problem and fix the JSON keys.
3. If the script reports a missing placeholder paragraph, treat that as a template-contract problem and fix the template or script mapping.
4. Keep `answers.json` until the generated docx has been checked.

Output filename defaults to `Interview Notes - Senior Software Developer - <Candidate Name>.docx`. See the attached reference screenshot for the exact table layout this produces.

### Cleanup

After verifying the generated docx is correct, delete the intermediate JSON file(s):

```bash
rm -f answers*.json
```

Run this in the skill directory to remove all generated answer files. The content is now embedded in the docx.

### Batch Processing

When processing multiple CVs in one session:

1. Create all `answers_<surname>.json` files first
2. Run `generate_interview_doc.py` for each
3. Verify all generated docx files
4. Run cleanup once: `rm -f answers*.json`

---

## Deep-Dive Follow-Ups

Generate probing follow-up questions such as:

- What was the exact root cause?
- What alternatives did you reject?
- How did you validate the fix?
- What metrics improved?
- What would you change today?
- How did this affect the team?
- How did you prevent recurrence?
- What was your personal contribution?
- What was the hardest part of the implementation?

---

## Evaluation Focus

| Area | What to Look For |
|--------|------------------|
| Technical Depth | Real implementation details |
| Ownership | Personal contribution clearly explained |
| Decision Making | Tradeoffs and rationale |
| Problem Solving | Structured investigation |
| Seniority | Influence and leadership without authority |
| Quality Mindset | Prevention vs reaction |
| Communication | Ability to explain complex topics clearly |

---

## CV Analysis Process

### Step 1: Identify Experience

Extract, ordered from most recent role to oldest:

- Roles
- Seniority level
- Technologies used
- Architecture experience
- Business domains
- Leadership responsibilities
- Cross-team collaboration examples

### Step 2: Apply Team Leading Fallback

If Team Leading responsibilities aren't explicit in the CV, use the Team Leading Fallback section above instead of skipping the category.

### Step 3: Generate Questions

Questions must be tied directly to:

- Technologies listed in the CV
- Projects described in the CV
- Responsibilities mentioned in the CV
- Achievements claimed in the CV

Avoid generating questions unsupported by the CV.

### Step 4: Generate Expected Answers

Expected answers should describe:

- What evidence demonstrates genuine experience
- What separates a strong answer from a weak answer
- Senior-level thinking and decision-making indicators

---

## Special Instructions

When reviewing a CV:

1. Identify technologies actually used.
2. Identify projects and responsibilities.
3. Determine seniority level.
4. Generate questions tied directly to those experiences.
5. Avoid generic industry questions not supported by the CV.
6. Prefer questions that expose whether the candidate genuinely performed the work.
7. Prefer questions requiring discussion of:
   - Tradeoffs
   - Failures
   - Debugging
   - Design decisions
   - Team influence
   - Production incidents
   - Quality improvements
8. Ensure questions cannot be answered effectively with memorized definitions.

---

## Senior Engineer Signals

Strong candidates should demonstrate:

- Ownership of technical outcomes
- Ability to make tradeoffs
- Real production experience
- Cross-team collaboration
- Root-cause driven problem solving
- Ability to mentor or influence others
- Quality and maintainability mindset
- Business awareness beyond coding

---

## Red Flags

Watch for answers that:

- Stay purely theoretical
- Lack specific examples
- Cannot explain decisions made
- Cannot discuss rejected alternatives
- Focus only on implementation details without business impact
- Claim ownership but cannot explain architecture or debugging approach
- Avoid discussing mistakes, failures, or lessons learned