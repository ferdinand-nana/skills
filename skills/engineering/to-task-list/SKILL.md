---
name: to-task-list
description: Break a plan, spec, or PRD into independently-grabbable tasks as local markdown files using tracer-bullet vertical slices. Creates an task-list.md index file with links to each task. Use when user wants to convert a plan into tasks, create implementation tickets, or break down work into tasks.
---

# To Tasks (Local)

Break a plan into independently-grabbable tasks using vertical slices (tracer bullets), saved as local markdown files.

## Process

### 1. Gather context

Work from whatever is already in the conversation context. If the user passes a document reference, file, or plan, use that as the source material.

### 2. Explore the codebase (optional)

If you have not already explored the codebase, do so to understand the current state of the code. Task titles and descriptions should use the project's domain glossary vocabulary.

### 3. Draft vertical slices

Break the plan into **tracer bullet** tasks. Each task is a thin vertical slice that cuts through ALL integration layers end-to-end, NOT a horizontal slice of one layer.

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

For each slice, create a markdown file named `<title>.md` where `<title>` is a kebab-case version of the task title.

Use the task template below for each file.

<task-template>
# <Task Title>

## Type

HITL / AFK

## What to build

A concise description of this vertical slice. Describe the end-to-end behavior, not layer-by-layer implementation.

## User Story

Provide the user story that this task addresses, if applicable. If the source material has user stories, reference the relevant one here.


## Implementation Details

A list of detailed sub-tasks to complete this issue based on the vertical slice determined. Use the format:

- [ ] **<Sub-Task 1 Summary>**
  - <Bulleted implementation details for Sub-Task 1>
  - <Additional context or considerations>
- [ ] **<Sub-Task 2 Summary>**
  - <Bulleted implementation details for Sub-Task 2>
  - <Additional context or considerations>
- [ ] **<Sub-Task 3 Summary>**
  - <Bulleted implementation details for Sub-Task 3>
  - <Additional context or considerations>

## Acceptance Criteria

- [ ] Criterion 1 (specific, measurable outcome)
- [ ] Criterion 2 (specific, measurable outcome)
- [ ] Criterion 3 (specific, measurable outcome)

## Blocked By

- Link to blocking task file (if any): [Task Title](./blocking-task.md)

Or "None - can start immediately" if no blockers.


## Notes

Any additional context, edge cases, or considerations for implementation.

</task-template>

### 5. Create tasks-list.md

Create an `tasks-list.md` file that serves as the main index. This file should contain:

- A brief description of the plan/project
- A table of all tasks with:
  - Link to the task markdown file
  - Type (HITL/AFK)
  - Status (e.g., "Not Started", "In Progress", "Completed")
  - Dependencies
  - Brief description

<tasks-list-template>
# Tasks List: <Project/Plan Name>

## Overview

Brief description of the plan or project these tasks implement.

## Tasks

| # | Task | Type | Status | Blocked By | Description |
|---|-------|------|--------|------------|-------------|
| 1 | [Task Title 1](./task-title-1.md) | AFK | Not Started | None | Brief description |
| 2 | [Task Title 2](./task-title-2.md) | HITL | Not Started | #1 | Brief description |
| 3 | [Task Title 3](./task-title-3.md) | AFK | Not Started | #1 | Brief description |

## Dependency Graph

task-title-1
├── task-title-2
└── task-title-3
└── task-title-4

## Progress

- **Total issues**: X
- **Completed**: 0
- **In Progress**: 0
- **Not Started**: X

## Quick Start

1. Start with issues marked "None" in the "Blocked By" column
2. Update issue status by editing this file
3. Check off acceptance criteria in individual task files as you complete them

</tasks-list-template>

List tasks in dependency order (blockers first) so dependencies are clear.

### 6. Adjustments

If the user requests changes to any task (granularity, dependencies, descriptions, acceptance criteria, etc.), update the relevant markdown files directly without re-creating the entire breakdown.

When updating:
- Preserve existing checkmarks and status
- Update dependency links if task titles change
- Regenerate the dependency graph in tasks-list.md if dependencies change