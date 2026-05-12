---
name: to-issues-local
description: Break a plan, spec, or PRD into independently-grabbable issues as local markdown files using tracer-bullet vertical slices. Creates an issues-list.md index file with links to each issue. Use when user wants to convert a plan into issues, create implementation tickets, or break down work into issues.
---

# To Issues (Local)

Break a plan into independently-grabbable issues using vertical slices (tracer bullets), saved as local markdown files.

## Process

### 1. Gather context

Work from whatever is already in the conversation context. If the user passes a document reference, file, or plan, use that as the source material.

### 2. Explore the codebase (optional)

If you have not already explored the codebase, do so to understand the current state of the code. Issue titles and descriptions should use the project's domain glossary vocabulary, and respect ADRs in the area you're touching.

### 3. Draft vertical slices

Break the plan into **tracer bullet** issues. Each issue is a thin vertical slice that cuts through ALL integration layers end-to-end, NOT a horizontal slice of one layer.

Slices may be 'HITL' or 'AFK'. HITL slices require human interaction, such as an architectural decision or a design review. AFK slices can be implemented and merged without human interaction. Prefer AFK over HITL where possible.

<vertical-slice-rules>
- Each slice delivers a narrow but COMPLETE path through every layer (schema, API, UI, tests)
- A completed slice is demoable or verifiable on its own
- Prefer many thin slices over few thick ones
- Each slice should be independently testable and deployable
</vertical-slice-rules>

### 4. Create local markdown files

Analyze the plan and immediately create the optimal breakdown. Use your best judgment for:
- Appropriate granularity (prefer thin slices)
- Correct dependency relationships
- Proper HITL vs AFK classification
- Complete acceptance criteria and implementation details

For each slice, create a markdown file named `<title>.md` where `<title>` is a kebab-case version of the issue title.

Use the issue template below for each file.

<issue-template>
# <Issue Title>

## Type

HITL / AFK

## What to build

A concise description of this vertical slice. Describe the end-to-end behavior, not layer-by-layer implementation.

## Implementation Details

A list of detailed tasks to complete this issue based on the vertical slice determined. Use the format:

- [ ] **<Task 1 Summary>**
  - <Bulleted implementation details for Task 1>
  - <Additional context or considerations>
- [ ] **<Task 2 Summary>**
  - <Bulleted implementation details for Task 2>
  - <Additional context or considerations>
- [ ] **<Task 3 Summary>**
  - <Bulleted implementation details for Task 3>
  - <Additional context or considerations>

## Acceptance Criteria

- [ ] Criterion 1 (specific, measurable outcome)
- [ ] Criterion 2 (specific, measurable outcome)
- [ ] Criterion 3 (specific, measurable outcome)

## Blocked By

- Link to blocking issue file (if any): [Issue Title](./blocking-issue.md)

Or "None - can start immediately" if no blockers.

## User Stories Covered

- User story 1 (if applicable)
- User story 2 (if applicable)

## Notes

Any additional context, edge cases, or considerations for implementation.

</issue-template>

### 5. Create issues-list.md

Create an `issues-list.md` file that serves as the main index. This file should contain:

- A brief description of the plan/project
- A table of all issues with:
  - Link to the issue markdown file
  - Type (HITL/AFK)
  - Status (e.g., "Not Started", "In Progress", "Completed")
  - Dependencies
  - Brief description

<issues-list-template>
# Issues List: <Project/Plan Name>

## Overview

Brief description of the plan or project these issues implement.

## Issues

| # | Issue | Type | Status | Blocked By | Description |
|---|-------|------|--------|------------|-------------|
| 1 | [Issue Title 1](./issue-title-1.md) | AFK | Not Started | None | Brief description |
| 2 | [Issue Title 2](./issue-title-2.md) | HITL | Not Started | #1 | Brief description |
| 3 | [Issue Title 3](./issue-title-3.md) | AFK | Not Started | #1 | Brief description |

## Dependency Graph

issue-title-1
├── issue-title-2
└── issue-title-3
└── issue-title-4

## Issues per User Story

| User Story # | User Story | Issue | Issue Description |
|--------------|------------|-------|-------------------|
| 1 | <User Story> | [Issue Title 1](./issue-title-1.md) | <Issue 1 Description> |
| 1 | <User Story> | [Issue Title 2](./issue-title-2.md) | <Issue 2 Description> |
| 2 | <User Story> | [Issue Title 3](./issue-title-3.md) | <Issue 3 Description> |

## Progress

- **Total issues**: X
- **Completed**: 0
- **In Progress**: 0
- **Not Started**: X

## Quick Start

1. Start with issues marked "None" in the "Blocked By" column
2. Update issue status by editing this file
3. Check off acceptance criteria in individual issue files as you complete them

</issues-list-template>

List issues in dependency order (blockers first) so dependencies are clear.

### 6. Adjustments

If the user requests changes to any issue (granularity, dependencies, descriptions, acceptance criteria, etc.), update the relevant markdown files directly without re-creating the entire breakdown.

When updating:
- Preserve existing checkmarks and status
- Update dependency links if issue titles change
- Regenerate the dependency graph in issues-list.md if dependencies change