---
name: app-builder
description: Use when turning a business idea into a structured app MVP, especially for SaaS, CRM, ERP, operations systems, AI-assisted products, or apps that may be prototyped in Antigravity before deeper implementation. Helps define scope, modules, data models, screens, rules, prompts for builders, and iteration workflow.
---

# App Builder

Use this skill when Alex wants to create an app, SaaS, internal system, CRM, ERP, operations panel, agent-assisted product, or business software idea and needs structure before or during execution.

## Core purpose

Turn a rough app idea into a clear MVP that can be:
- prototyped in Antigravity
- handed to a development agent
- turned into product documentation
- iterated with less chaos

## What this skill should produce

Depending on the situation, produce some or all of these:
- product definition
- MVP scope
- user roles
- modules
- screens
- entities and fields
- workflows
- business rules
- technical direction
- Antigravity prompt
- iteration prompt for refinement
- handoff spec for development agents

## Standard operating sequence

### 1. Clarify the business goal
Before talking about features, identify:
- what problem the app solves
- who uses it
- what business value it creates
- what must work first

If the user starts with a loose idea, structure it before proposing implementation.

### 2. Define the MVP
Prefer the smallest version that creates real operational value.

Always identify:
- must-have features
- nice-to-have features
- what can wait
- what creates immediate business leverage

## 3. Structure the app
When mapping the app, define:
- main modules
- core screens
- user actions
- key data records
- reports or dashboards
- operational flows

## 4. Define the data model
At minimum, identify:
- main entities
- key fields for each entity
- relationships between entities
- metrics needed for dashboards or reports

## 5. Define rules and calculations
Capture logic such as:
- statuses
- transitions
- alerts
- profit calculations
- inventory effects
- CRM stages
- payment/tax logic
- time-based triggers

## 6. Choose execution path
Recommend the best path among:
- Antigravity first for fast prototype and interface
- development agent for serious implementation
- both, with Antigravity for shape and dev agent for production

Default recommendation:
- Antigravity for first visual/product pass
- development agent for consolidation when business logic becomes important

## 7. Build the right artifact
Choose the best output format for the moment:
- `app-<name>-mvp.md` for structured product definition
- a direct Antigravity prompt for rapid prototyping
- a technical handoff spec for implementation
- a backlog or module plan for phased execution

## Output pattern
When useful, structure the result in this order:
1. what this app really is
2. business objective
3. MVP scope
4. modules
5. screens
6. entities and fields
7. rules and automations
8. recommended build path
9. next step

## Antigravity prompt guidance
When generating prompts for Antigravity:
- describe the product clearly
- state the objective of the system
- define modules and screens explicitly
- include key data fields
- include business rules that affect calculations or workflow
- ask for a professional, operational, production-feeling interface
- prefer two-step prompting when complexity is high:
  1. structure and UI
  2. rules, refinements, and operational logic

## Development handoff guidance
When handing off to a dev agent, include:
- product objective
- users
- MVP scope
- modules
- entities
- workflows
- business rules
- calculations
- statuses
- constraints
- what not to overbuild yet

## Decision rules
Prefer the option that is:
1. clearer
2. faster to validate
3. easier to operate
4. more useful in the real business
5. simpler to maintain
6. expandable later

## Things to avoid
Do not:
- jump into coding before product clarity exists
- inflate the MVP with unnecessary complexity
- confuse operational features with future nice-to-haves
- give generic app advice without structuring the product
- ignore business rules like profit, stock, payment, or status logic

## Good fit examples
Use this skill for requests like:
- build an app for my business
- help me create a CRM or ERP
- structure an MVP for Antigravity
- turn this idea into a system
- define modules, screens, and entities
- prepare a handoff for a dev agent

## Recommended companion outputs
For recurring work, also create or update:
- `MAPA.md`
- business-area docs under `cerebro/empresa/` or `cerebro/areas/`
- a product document like `app-<name>-mvp.md`
- `TASKS.md` or `PRIORITIES.md` if execution should continue
