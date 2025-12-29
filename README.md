
[![Tests](https://github.com/aa-parky/pipeworks_entity_state_generation/actions/workflows/test.yml/badge.svg )](https://github.com/aa-parky/pipeworks_entity_state_generation/actions/workflows/test.yml ) [![Lint & Type Check](https://github.com/aa-parky/pipeworks_entity_state_generation/actions/workflows/lint.yml/badge.svg )](https://github.com/aa-parky/pipeworks_entity_state_generation/actions/workflows/lint.yml ) [![codecov](https://codecov.io/gh/aa-parky/pipeworks_entity_state_generation/branch/main/graph/badge.svg)](https://codecov.io/gh/aa-parky/pipeworks_entity_state_generation)[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

# 1 Pipeworks Entity State Generation

This repository contains **generation-time primitives** for producing structured, interpretable state for entities within the Pipeworks ecosystem.

It is not a rendering system, a simulation engine, or a narrative framework.

Its sole responsibility is to answer the question:

> **“What is the state of this thing, and where does it behave slightly off-pattern?”**

---

## 1.1 What Lives Here

This repository defines two orthogonal systems used during entity generation:

1. **Conditional Axes** — structured, population-weighted state
2. **Quirks** — persistent, localised irregularities

Together, they provide a stable foundation for generating characters, locations, items, documents, processes, and other entities **before** interpretation or presentation.

---

## 1.2 Conditional Axes

Conditional axes describe the **current lived state** of an entity.

They are:

- mutually exclusive within an axis
- population-weighted rather than uniform
- explainable and auditable
- resolved once during generation

Examples of conditional axes include:

- health
- wealth
- age
- physique
- demeanor
- occupation conditions (labour constraints, not job titles)

Conditional axes answer:

> **“What pressures is the world currently applying to this entity?”**

They do not encode:

- traits
- abilities
- progression
- optimisation
- heroism

Axes bias probability and interpretation, not outcomes.

---

## 1.3 Quirks

Quirks introduce **structured irregularity**.

They are not axes, traits, or modifiers.

A quirk is a small, persistent deviation that:

- remains local to an entity
- does not resolve into a system-wide rule
- biases attention and interpretation
- repeats without fully explaining itself

Quirks may apply to:

- characters
- locations
- items
- organisations
- documents
- processes

Quirks answer:

> **“Where does this entity fail to behave like a clean model?”**

They complicate situations but must never resolve them.

---

## 1.4 Relationship Between Axes and Quirks

Conditional axes and quirks are intentionally **orthogonal**.

- Axes resolve state
- Quirks annotate state
- Axes bias probability
- Quirks bias attention

Quirks must not:

- influence axis resolution
- affect axis weighting
- generate derived state upstream

Axes push the system toward coherence.

Quirks prevent it becoming too clean.

---

## 1.5 Repository Structure

```text

pipeworks_entity_state_generation/

├── README.md
│
├── axes/
│   ├── condition_axis_v_01.md
│   ├── condition_axis_v_02.md
│   ├── character_conditions.py
│   └── occupation_axis.py
│
├── quirks/
│   ├── quirks_overview.md
│   ├── quirk_registry.md        # (planned)
│   ├── quirk_schema.py          # (planned)
│   └── quirk_selection.py       # (planned)
│
└── common/
  ├── entity_scopes.py
  ├── tagging.py
  └── seed_utils.py

```

Folders represent **ontological boundaries**, not deployment units.

---

## 1.6 What This Repository Is Not

This repository does **not**:

- render text or images
- simulate behaviour over time
- implement progression systems
- resolve narrative outcomes
- balance gameplay
- define UI or player interaction

Those concerns belong downstream.

---

## 1.7 Design Principles

- Interpretation over prescription
- Bias over randomness
- Structure with room for failure
- Explainable state, inexplicable detail

Generated entities should feel *coherent*, not optimised.

---

## 1.8 Status

This repository is under active development.

Interfaces, schemas, and selection logic are expected to evolve, but the core separation between:

- state resolution (axes)
- state irregularity (quirks)

is considered foundational.

---

## 1.9 License

GPL-3.0

This repository is part of the broader Pipeworks project.