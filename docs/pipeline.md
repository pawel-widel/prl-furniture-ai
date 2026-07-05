# AI Recognition Pipeline

## Goal

The goal of this project is to verify the following hypothesis:

> Adding a structured knowledge base and a multi-stage pipeline improves furniture recognition compared to using a Vision model alone.

The application is **not** intended to demonstrate a better AI model.

It demonstrates a **better AI workflow**.

---

# Current MVP Pipeline

```text
User Photo
      │
      ▼
Vision Feature Extraction
      │
      ▼
Structured Features
      │
      ▼
Knowledge Base Search
      │
      ▼
Top 5 Candidate Models
      │
      ▼
Visual Verification
      │
      ▼
Final Prediction
```

---

# Pipeline Stages

## Stage 1 — Vision Feature Extraction

Input:

- furniture photo

Output:

- structured JSON describing visible features

Example:

```json
{
  "category": "armchair",
  "armrests": true,
  "wooden_frame": true,
  "seat_type": "upholstered",
  "backrest_type": "upholstered",
  "leg_type": "tapered",
  "construction": "open wooden frame"
}
```

The Vision model **does not identify the furniture**.

It only extracts observable visual features.

---

## Stage 2 — Knowledge Base Search

Input:

- extracted features

Output:

- Top 5 candidate models

The search stage is deterministic.

No AI model is used.

---

## Stage 3 — Visual Verification

Input:

- user photo
- Top 5 candidate models
- reference images

Output:

- final prediction

The Vision model performs only visual comparison.

It does not use its own knowledge.

---

# Design Principles

- Keep each AI step focused on a single task.
- Use deterministic logic whenever possible.
- Minimize hallucinations.
- Reduce context size.
- Make every stage independently testable.
