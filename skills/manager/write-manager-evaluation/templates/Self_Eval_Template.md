# Self-Evaluation Template

This file defines the structure of the self-evaluation.
Self-evaluation is consist of 3 parts:
1. The WHAT: What were the key achievements and overall performance during the period?
- Highlights the key achievements in the period, with metrics and impact
- Provide a summary of the overall performance

2. The HOW: How were the achievements accomplished? What behaviors and skills were demonstrated?
- Maps the achievements to the behaviors defined in [BEHAVIORS.md](../../write-self-evaluation/BEHAVIORS.md) to demonstrate how the evaluator embodied the Finastra values in his work.

3. Your GROWTH: What personal development and growth occurred during the period?
- Reflect on the personal development goals and aspirations of the evaluator

Here's the self-evaluation template:
<self-evaluation-template>
```md
# Self-evaluation — {period} — {name}, {role}

---

## The WHAT
[Evaluation here]

---

## The HOW
[Evaluation here]

---

## Your GROWTH
[Evaluation here]
```
</self-evaluation-template>

---

Here's an example:

# Self-Evaluation — FY2026 — Juan dela Cruz, Senior Software Engineer

---

## The WHAT

This year was defined by meaningful contributions across feature delivery, collaborative design work, and taking ownership of an automation initiative that improved how we ship software.

### Feature Delivery

I delivered three key features — A, B, and C — that directly addressed user-facing pain points and expanded the capabilities of our product. Feature A introduced a new data processing workflow that reduced manual handling steps for end users, while Feature B extended our reporting surface to give clients better visibility into their transactions. Feature C added configurable alerting that allowed teams to respond to critical events more proactively.

Across all three, I worked closely with product, QA, and design to ensure requirements were well-understood before writing a single line of code. I also wrote comprehensive unit and integration tests to protect against regressions, which helped our team maintain a low rollback rate through the release cycle.

### Collaborative Design: XYZ Feature

I was part of the core group that designed and implemented XYZ, which was one of the more complex initiatives this year given it touched multiple services and required tight coordination across teams. My contribution was focused on the data layer — defining the schema, aligning on API contracts with downstream consumers, and reviewing integration points with the platform team. The implementation went live with minimal disruption, and the cross-team design process we followed became a reference point for future multi-team work.

### Deployment Automation: ABC Product

One of the most impactful things I did this year was leading the automation of our ABC product deployment pipeline using GitHub Actions. Before this, deployments required significant manual intervention, were inconsistent across environments, and were a source of anxiety for the team. I designed the workflow from scratch — covering environment-specific configurations, secret management, approval gates, and rollback triggers — and worked with the DevOps team to get it production-ready.

The result was a repeatable, auditable, and significantly faster deployment process. It also freed up time for the team and reduced the number of deployment-related incidents we had to respond to. I documented the entire setup and ran a walkthrough session so the team could maintain and extend it confidently.

---

## The HOW

### Shared Accountability

I took clear ownership this year, especially on the ABC deployment automation. I identified the problem, proposed the solution, and saw it through from design to documentation — without being asked to do so. When we hit edge cases mid-implementation (particularly around secrets management across environments), I raised them early, looped in the right people, and adjusted the design rather than pushing something fragile to production. I own what I ship.

### Stronger Together

XYZ was a good example of how I try to work: bringing people in early rather than designing in isolation. I facilitated alignment sessions between the backend and platform teams to resolve API contract ambiguities before they became blockers. I also shared what I learned from the GitHub Actions work with colleagues who were building adjacent pipelines, and I made a point to document decisions so knowledge didn't stay locked in my head or Slack threads.

### Growth Mindset

CI/CD automation at this depth was relatively new territory for me. Rather than defaulting to what I knew, I invested time in learning GitHub Actions best practices, studied how other teams handled secret scoping and approval workflows, and tested different approaches in a sandbox before committing to a design. I also asked for feedback during code review on the pipeline code itself, which is not something our team typically reviews with as much rigor as application code — and that turned into a useful conversation about how we treat infrastructure-as-code going forward.

---

## Your GROWTH

### Opportunities Taken

Leading the ABC deployment automation pushed me to develop hands-on expertise in GitHub Actions and release engineering practices that I hadn't had before. It was an opportunity to go beyond my usual development work and contribute at the infrastructure layer, and I'm glad I took it on. Participating in the XYZ design process also gave me exposure to system-level thinking across service boundaries, which stretched my architectural reasoning.

### Strengths to Build On

I'm effective at translating technical work into clear outcomes — whether that's in documentation, team walkthroughs, or design discussions. I want to use that strength more intentionally to help newer engineers navigate the kind of ambiguous, multi-team problems I worked through this year. I've started doing informal design reviews with a junior colleague on the team, and I'd like to make that a more consistent practice.

### Areas to Develop

I want to grow my strategic thinking around capacity and delivery planning. I sometimes start building before the full picture is clear, and this year there were a couple of moments — particularly early in the XYZ feature — where earlier alignment would have saved rework. I'm also working on making my communication more proactive with stakeholders, particularly when estimates change or risks surface mid-sprint.

### Short-term & Long-term Aspirations

**Short-term:** Build more depth in release engineering and DevSecOps practices. Formalize my informal mentoring into something more structured and repeatable for junior team members.

**Long-term:** I want to grow toward a Technical Leader or Staff Engineer track where I can influence system design decisions across a broader scope and help shape how the team approaches delivery quality and engineering practices — not just within my squad, but across the wider group.

