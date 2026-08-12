---
name: write-manager-evaluation
description: Generates a structured manager evaluation for a direct report by synthesizing their self-evaluation and peer evaluation inputs. Use when a manager needs to write a performance review, manager assessment, or year-end evaluation for an employee, or when provided with a self-evaluation file and/or peer evaluation file.
---

# Write Manager Evaluation

Creates a manager evaluation by synthesizing the employee's self-assessment and peer feedback into a balanced, evidence-backed performance review. Employee details (name, period, role) are extracted from the self-evaluation file.

## Pre-Process

### Create the peer evaluation file
- Before running this skill, the manager should have collected peer feedback for the employee. This can be done using the [Peer Evaluation Template](templates/Peer_Eval_Template.md) and should be saved as a separate file.
- Also, the self-evaluation file should be prepared using the [Self-Evaluation Template](templates/Self_Eval_Template.md) if not already done by the employee.

## Process

### Step 1 — Load Source Files
If not provided, ask the user to provide:
- **Self-evaluation file** — contains employee name, period, role, achievements, behaviors, and growth.
- **Peer evaluation file** (optional but recommended) — contains feedback from colleagues.

Extract from the self-evaluation:
- `name` — employee name
- `period` — evaluation period (e.g., FY2026)
- `role` — job role (match to [ROLE_DESCRIPTOR.md](../write-self-evaluation/ROLE_DESCRIPTOR.md))

### Step 2 — Gather Manager Context

#### Step 2.1 - Evaluate the performance objectively (The WHAT)
1. Extract the THE WHAT of the employee's performance by providing key acomplishments using the self-evaluation.
   Show the summarized accomplishments to the manager in the following format:
   ```
    From Self-evaluation, the key accomplishments for {name} during {period} are:
    - [Accomplishment 1]
    - [Accomplishment 2]
    - [Accomplishment 3]
   ```
2. Extract the THE WHAT (each question is mapped to specific 'The WHAT', 'The HOW' and 'Your GROWTH') of the employee's performance by providing key accomplishments using the peer evaluation.
   Show the summarized accomplishments to the manager in the following format:
   ```
    From Peer evaluation, the key accomplishments for {name} during {period} are:
    - From [Provide the evaluators for the summarized feedback]: [Accomplishment 1]
    - From [Provide the evaluators for the summarized feedback]: [Accomplishment 2]
    - From [Provide the evaluators for the summarized feedback]: [Accomplishment 3]
   ```
3. Stop, pause. Ask the manager to provide their own observations on the key accomplishments and team/org impact of the employee's work. This will help to fill in any gaps and provide a more complete picture of the employee's performance.
> If the manager has limited input, derive the assessment primarily from the self-evaluation and peer feedback, clearly noting where gaps exist.

4. Synthesize the accomplishments from the self-evaluation, peer evaluation, and manager's observations to create a comprehensive summary of the employee's key achievements and overall performance during the period. Weight peer feedback as corroborating or qualifying evidence, not as the primary voice. Use this synthesis to inform the "The WHAT" section of the manager evaluation. Provide a draft of the "The WHAT" section to the manager for review and feedback before finalizing it in the manager evaluation. Reference [Manager_Eval_Guidelines.md](templates/Manager_Eval_Guidelines.md) for calibration guidance and tone.

#### Step 2.2 - Evaluate the behaviors (The HOW)
1. Extract the THE HOW of the employee's performance by providing key behaviors using the self-evaluation.
   Categorize the behaviors based on the Finastra behaviors defined in [BEHAVIORS.md](../write-self-evaluation/BEHAVIORS.md).
   Show the summarized behaviors to the manager in the following format:
   ```
    From Self-evaluation, the key behaviors demonstrated by {name} during {period} are:

    [Finastra Behavior 1]
    - [Behavior 1]
    - [Behavior 2]
    - [Behavior 3]

    [Finastra Behavior 2]
    - [Behavior 1]
    - [Behavior 2]
    - [Behavior 3]

    [Finastra Behavior 3]
    - [Behavior 1]
    - [Behavior 2]
    - [Behavior 3]
   ```
2. Extract the THE HOW of the employee's performance by providing key behaviors using the peer evaluation.
   Categorize the behaviors based on the Finastra behaviors defined in [BEHAVIORS.md](../write-self-evaluation/BEHAVIORS.md).
   Show the summarized behaviors to the manager in the following format:
   ```
    From Peer evaluation, the key behaviors demonstrated by {name} during {period} are:

    [Finastra Behavior 1]
    - From [Provide the evaluators for the summarized feedback]: [Behavior 1]
    - From [Provide the evaluators for the summarized feedback]: [Behavior 2]
    - From [Provide the evaluators for the summarized feedback]: [Behavior 3]

    [Finastra Behavior 2]
    - From [Provide the evaluators for the summarized feedback]: [Behavior 1]
    - From [Provide the evaluators for the summarized feedback]: [Behavior 2]
    - From [Provide the evaluators for the summarized feedback]: [Behavior 3]

    [Finastra Behavior 3]
    - From [Provide the evaluators for the summarized feedback]: [Behavior 1]
    - From [Provide the evaluators for the summarized feedback]: [Behavior 2]
    - From [Provide the evaluators for the summarized feedback]: [Behavior 3]
   ```
3. Stop, pause. Ask the manager to provide their own observations on the behaviors demonstrated by the employee. This will help to fill in any gaps and provide a more complete picture of the employee's performance. Ask the manager per Finastra behavior or can be skipped if the manager does not have specific observations on the behaviors. use the format to ask:
    ```
    Do you have any specific observations on {name}'s demonstration of [Finastra Behavior] during {period}?
    [Provide description of the behavior for the manager to understand better]
    ```
    > If the manager has limited input, derive the assessment primarily from the self-evaluation and peer feedback, clearly noting where gaps exist.

4. Synthesize the behaviors from the self-evaluation, peer evaluation, and manager's observations to create a comprehensive summary of the employee's key behaviors and how they were demonstrated during the period. Weight peer feedback as corroborating or qualifying evidence, not as the primary voice. Use this synthesis to inform the "The HOW" section of the manager evaluation. Provide a draft of the "The HOW" section to the manager for review and feedback before finalizing it in the manager evaluation. Use the following format
    ```
    [Finastra Behavior 1]
    [A short summary of how the employee demonstrated this behavior based on the synthesis of self-evaluation, peer evaluation, and manager's observations. 1 to 2 paragraphs]

    [Finastra Behavior 2]
    [A short summary of how the employee demonstrated this behavior based on the synthesis of self-evaluation, peer evaluation, and manager's observations. 1 to 2 paragraphs]

    [Finastra Behavior 3]
    [A short summary of how the employee demonstrated this behavior based on the synthesis of self-evaluation, peer evaluation, and manager's observations. 1 to 2 paragraphs]
   ```
  Reference [Manager_Eval_Guidelines.md](templates/Manager_Eval_Guidelines.md) for calibration guidance and tone.

#### Step 2.3 - Evaluate the development and growth (Your GROWTH)
1. Extract the Your GROWTH of the employee's performance by providing key development and growth areas using the self-evaluation.
   Show the summarized development and growth areas to the manager in the following format:
   ```
    From Self-evaluation, the key development and growth areas for {name} during {period} are:
    - [Development and Growth Area 1]
    - [Development and Growth Area 2]
    - [Development and Growth Area 3]
   ```
2. Extract the Your GROWTH of the employee's performance by providing key development and growth areas using the peer evaluation.
   Show the summarized development and growth areas to the manager in the following format:
   ```
    From Peer evaluation, the key development and growth areas for {name} during {period} are:
    - From [Provide the evaluators for the summarized feedback]: [Development and Growth Area 1]
    - From [Provide the evaluators for the summarized feedback]: [Development and Growth Area 2]
    - From [Provide the evaluators for the summarized feedback]: [Development and Growth Area 3]
   ```
3. Using the role of the employee, extract the expected development and growth areas based on the role criteria from [ROLE_DESCRIPTOR.md](../write-self-evaluation/ROLE_DESCRIPTOR.md) and the expected skill levels for the role from [TOP_REQUIRED_SKILLS.md](../write-self-evaluation/TOP_REQUIRED_SKILLS.md). Show the expected development and growth areas to the manager in the following format:
   ```
    Based on {name}'s role as a {role}, the expected development and growth areas based on the role criteria from ROLE_DESCRIPTOR.md and the expected skill levels for the role from TOP_REQUIRED_SKILLS.md are:
    - [Expected Development and Growth Area 1]
    - [Expected Development and Growth Area 2]
    - [Expected Development and Growth Area 3]
   ```
4. Stop, pause. Ask the manager to provide their own observations on the development and growth areas for the employee. This will help to fill in any gaps and provide a more complete picture of the employee's performance. Use the following format to ask:
    ```
    Do you have any specific observations on {name}'s development and growth during {period}?
    [Provide description of the expected development and growth areas for the manager to understand better]
    ```
    > If the manager has limited input, derive the assessment primarily from the self-evaluation and peer feedback, clearly noting where gaps exist.

5. Synthesize the development and growth areas from the self-evaluation, peer evaluation, expected development and growth areas based on the role criteria, and manager's observations to create a comprehensive summary of the employee's key development and growth areas during the period. Weight peer feedback as corroborating or qualifying evidence, not as the primary voice. Use this synthesis to inform the "Your GROWTH" section of the manager evaluation. Provide a draft of the "Your GROWTH" section to the manager for review and feedback before finalizing it in the manager evaluation. Use the following format:
    ```
    [Development and Growth Area 1]
    [A short summary of the development and growth area based on the synthesis of self-evaluation, peer evaluation, expected development and growth areas based on the role criteria, and manager's observations. 1 to 2 paragraphs]

    [Development and Growth Area 2]
    [A short summary of the development and growth area based on the synthesis of self-evaluation, peer evaluation, expected development and growth areas based on the role criteria, and manager's observations. 1 to 2 paragraphs]
    ```
    Provide 2 - 3 growth areas for the employee, making sure to tie them to the expected skill levels for the role from TOP_REQUIRED_SKILLS.md and the role criteria from ROLE_DESCRIPTOR.md.
    Reference [Manager_Eval_Guidelines.md](templates/Manager_Eval_Guidelines.md) for calibration guidance and tone.

### Step 3 — Write the Manager Evaluation
- Use [Manager_Eval_Template.md](templates/Manager_Eval_Template.md) as the output template.
- Populate the template with the synthesized content from Step 2 for "The WHAT", "The HOW", and "Your GROWTH" sections.
- If not provided, ask the user where to put the generated manager evaluation file and save it with filename in the format of `{Name}_Manager_Eval.md` where {Name} is the name of the employee being evaluated. For example, `Hazel_Mendoza_Manager_Eval.md`.
- At the last of the "Your GROWTH" section, add a "Looking Ahead" paragraph with 1 - 2 sentences by thanking the employee for their contributions and outlining goals or expectations for the next period. Align with the employee's stated growth aspirations where appropriate.


### Step 4 — Review
Present the draft to the manager and ask:
- Does this accurately reflect your assessment?
- Are there any sensitive topics to reframe?
- Should development areas be strengthened or softened?


## Notes
- The manager evaluation is the manager's voice — write in first person from the manager's perspective.
- Do not copy-paste from the self-evaluation; reframe achievements as observed outcomes.
- Keep it 2 - 3 paragraphs for "The WHAT", 2 - 3 paragraphs for "The HOW", and 3 - 4 paragraphs for "Your GROWTH".
- For Manager-role employees, weight leadership impact and team results more heavily than individual contributions.
- Balance recognition with honest development feedback — avoid pure praise or pure criticism.
- Use simple yet specific language to describe performance levels and development areas.
- Do not sound vague or generic; anchor statements in concrete examples and observed outcomes and should not be AI-generated sounding.
- STRICTLY DO NOT use "—" or dash or hypens in the paragraphs because it feels like AI generated; use "-" only for bullet points.
