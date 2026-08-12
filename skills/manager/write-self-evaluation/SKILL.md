---
name: write-self-evaluation
description: Generates a clear, structured self-evaluation from a user's provided achievements and context. Use when the user asks for a self-evaluation, performance review, year-end reflection, or provides achievements, goals, metrics, role, or desired tone.
---

# Write Self-Evaluation
Creates a structured self-evaluation from the provided information about achievements, challenges, learnings, and goals. This skill helps users articulate their performance and growth in a clear and concise manner, suitable for performance reviews or personal reflection.

## Process

### Gather basic information:
Ask the user for the following information to set the context for the self-evaluation:
- `name`: User's name
- `role`: User's job title or role (choose only from the roles defined in [ROLE_DESCRIPTOR.md](ROLE_DESCRIPTOR.md) to align the evaluation with the appropriate performance level)
- `period`: Timeframe for the evaluation (e.g., "2023", "Q1 2024")

For Manager role, ask the user for:
1. Team achievements and impact
2. Personal technical contributions (if applicable)


### Capture Achievements: The Business Aligned Goals
Collect achievements from user either in bullet form or as a list of items with action, context, result, and impact. Emphasize metrics and outcomes where possible. The user can also reference a file containing their achievements.

Needs to capture the key accomplishments​ and challenges faced when achieving the goals. Ask questions one by one to clarify the achievements and challenges, or allow the user to provide a file with this information.


### Capture the Behaviors: The Finastra Behaviors
Understand the core behaviors that Finastra values and expects from its employees, as defined in [BEHAVIORS.md](BEHAVIORS.md). These behaviors include Customer Centric, Stronger Together, Growth Mindset, and Shared Accountability. The self-evaluation should reflect how the user's achievements align with these behaviors.

Needs to capture the Behavior strengths and Behavior opportunities for development.
Ask questions one by one to capture the key behaviors that the user has demonstrated and areas for improvement. The user can also reference a file containing their behaviors.


### Capture the Growth: Personal Development Goals & Aspirations
Understand the user's personal development goals and aspirations. Ask the user for any skills they wish to develop, career aspirations, or areas they want to grow in. This information can be used to frame the self-evaluation in a way that highlights their commitment to growth and development. Use the information from [TOP_REQUIRED_SKILLS.md](TOP_REQUIRED_SKILLS.md) to understand the key skills that are relevant to the user's role and aspirations depending on their role.

Needs to capture the user's Opportunities taken to learn something new or do something different. Strengths that can be leveraged to support aspirations, also Areas of development and Short-term & long-term career aspirations for future discussion. Ask questions one by one to capture this information, or allow the user to provide a file with their personal development goals and aspirations.

### Iterate to Refine
- Clarify any ambiguous achievements, behaviors, or growth areas through follow-up questions.
- Ensure that the information is concise, evidence-based, and aligned with the user's role and aspirations.


### Write the Self-Evaluation
Use the information gathered to write a self-evaluation. Use the structure defined in [SELF_EVALUATION_FORMAT.md](SELF_EVALUATION_FORMAT.md) to ensure that the self-evaluation is well-organized and covers all necessary aspects. See the sample self-evaluation in [Examples Folder](examples/) for reference on how to structure the content and tone.


## How to use the role descriptor
- The overall role must reflect the balance of impact, consistency, and scope. When constructing the justification, reference concrete metric-driven achievements and behavior aligned to the role criteria in [ROLE_DESCRIPTOR.md](ROLE_DESCRIPTOR.md).


## Notes
- For Manager role, the achievements should be focused on leadership impact, team performance, and strategic contributions rather than individual technical accomplishments.
- For Manager role, the behaviors should focus on Customer Centric, Stronger Together, Growth Mindset.
- For other roles, the achievements should include focus technical contributions
- For Technical Leader and Senior Software Engineer roles, the achievements should include leadership impact, with a focus on how they contributed to team and organizational goals.
- For Technical Leader and Senior Software Engineer roles, the behaviors should focus on Customer Centric, Growth Mindset, Shared Accountability, and Stronger Together.
- For Software Engineer and Junior Software Engineer roles, the achievements should highlight technical contributions and how they supported team goals.