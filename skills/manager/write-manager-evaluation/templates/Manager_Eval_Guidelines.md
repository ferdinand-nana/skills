# Manager Evaluation Guidelines

Reference guide for calibration, synthesis, and tone decisions when writing a manager evaluation.

---

## Extracting Employee Details from Self-Evaluation

The self-evaluation file header typically follows this pattern:
```
# Self-evaluation — {period} — {name}, {role}
```

Extract:
- **name** — full name of the employee
- **period** — fiscal year or quarter (e.g., FY2026, Q1 2025)
- **role** — job title; match to one of the defined roles in ROLE_DESCRIPTOR.md:
  - Director, Manager, Technical Leader, Senior Software Engineer, Software Engineer, Junior Software Engineer

If the role is ambiguous, ask the manager to confirm before proceeding.

---

## Synthesizing Self-Evaluation and Peer Feedback

| Signal | How to use it |
|---|---|
| Self & peer **agree** on an achievement | Present as a confirmed strength with confidence |
| Self claims X, peer **corroborates** | Amplify the point — strong evidence of impact |
| Self claims X, peer **silent** | Include with softer language: "As noted in their self-assessment..." |
| Peer highlights something **not in self-eval** | Incorporate it — peers often surface team impact the employee undersells |
| Self & peer **disagree** | Flag to the manager privately; soften or omit from the written evaluation unless the manager wants to address it directly |

---

## Calibrating to Role Level

Cross-reference achievements and behaviors against ROLE_DESCRIPTOR.md criteria for the employee's role.

### Manager Role — Calibration Focus
- Team delivery results and business impact > individual technical contributions
- Evidence of leading others, setting direction, and removing blockers
- Behaviors: Customer Centric, Stronger Together, Growth Mindset
- Development skills: Leading Individuals, Leading Teams, Coaching & Mentoring, Communication, Strategic Thinking (see TOP_REQUIRED_SKILLS.md)

### Technical Leader / Senior SE — Calibration Focus
- Balance of individual technical contribution + leadership influence
- Evidence of mentorship, cross-team collaboration, architectural decisions
- Behaviors: all four Finastra behaviors apply

### Software Engineer / Junior SE — Calibration Focus
- Technical delivery quality and learning trajectory
- Behaviors: Growth Mindset, Shared Accountability

---

## Performance Level Language

Use these phrases to anchor the overall assessment:

| Performance Level | Example Phrases |
|---|---|
| Exceeds Expectations | "consistently delivered above what was asked", "raised the bar for the team", "demonstrated impact beyond their role" |
| Meets Expectations | "reliably delivered on commitments", "performed well within the scope of the role", "a consistent and dependable contributor" |
| Below Expectations | "struggled to meet key deliverables", "areas of concern were observed", "development is needed in core areas of the role" |

Avoid vague language like "did a good job" or "showed potential" without concrete examples.

---

## Common Pitfalls to Avoid

- **Copy-pasting from the self-evaluation** — reframe everything in the manager's voice and perspective
- **Pure praise with no development feedback** — every evaluation should include at least one honest development area
- **Vague development feedback** — "improve communication" is not actionable; be specific about what was observed and what better looks like
- **Over-relying on peer feedback** — peer input is corroborating evidence, not the primary assessment
- **Ignoring the role criteria** — always anchor the overall assessment to what is expected at the employee's level
