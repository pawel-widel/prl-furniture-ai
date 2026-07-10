# Architecture

## Overview

PRL Furniture AI is built around a multi-stage identification pipeline rather than relying on a single Vision model prediction.

Instead of asking an LLM to directly identify furniture, the application first extracts objective visual features, narrows the search space using a structured knowledge base, and only then performs AI-based verification.

This architecture improves transparency, reduces hallucinations, and allows the reasoning process to be inspected at every stage.

---

# Architecture Overview

```text
                User Photo
                     │
                     ▼
        Vision Feature Extraction
                     │
                     ▼
          Structured Visual Features
                     │
                     ▼
          Knowledge Base Search
                     │
                     ▼
            Top 5 Candidates
                     │
                     ▼
             AI Verification
                     │
                     ▼
              Final Ranking
                     │
                     ▼
           Identification Result
```

---

# Pipeline

## 1. User Photo

The identification process starts with a single photograph uploaded by the user.

The image may contain:

- furniture in use
- auction photos
- restored furniture
- partially visible furniture

No additional metadata is required.

---

## 2. Vision Feature Extraction

The Vision model does **not** identify the furniture.

Instead, it extracts structured visual attributes that can be directly observed.

Example:

```json
{
  "category": "armchair",
  "has_armrests": true,
  "wooden_frame": false,
  "seat_type": "upholstered",
  "backrest_shape": "bucket",
  "frame_geometry": "shell"
}
```

This step intentionally separates visual observation from identification.

---

## 3. Knowledge Base Search

Extracted features are compared against a manually curated furniture database.

Each furniture model contains:

- visual characteristics
- construction features
- search features
- designer
- manufacturer
- production years
- reference images
- confidence level

A lightweight scoring algorithm ranks the most similar candidates.

The output consists of the Top 5 most likely furniture models.

---

## 4. AI Verification

Instead of trusting the search result directly, each candidate is verified by a second AI reasoning step.

The Vision model receives:

- the user photo
- candidate reference photo
- structured furniture description

It compares both objects and decides whether they represent the same furniture model.

This stage significantly reduces false-positive identifications.

---

## 5. Final Ranking

The application combines:

- search score
- AI verification result
- confidence

to produce the final recommendation shown to the user.

The user can also inspect alternative candidates.

---

# Design Principles

The pipeline follows several design principles.

## Separation of Responsibilities

Feature extraction, candidate retrieval and verification are independent stages.

Each component solves a single problem.

---

## Explainability

Intermediate results remain visible.

The user can inspect:

- extracted visual features
- search candidates
- AI verification
- confidence

This makes the reasoning process significantly more transparent than a single LLM response.

---

## Knowledge-Guided AI

The application combines:

- Vision AI
- structured knowledge
- deterministic search
- LLM reasoning

instead of relying solely on a large language model.

---

## Modular Design

Each pipeline component can be replaced independently.

For example:

Vision Model

GPT-5.5

↓

Gemini

↓

Open Source Vision Model

without redesigning the remaining system.

---

# Project Structure

```text
User Interface (Streamlit)
            │
            ▼
Identification Service
            │
            ├───────────────┐
            ▼               ▼
Vision Service     Search Service
            │               │
            └───────┬───────┘
                    ▼
          Verification Service
                    │
                    ▼
              SQLite Database
```

---

# Why This Architecture?

The initial prototype relied almost entirely on a Vision model.

Benchmark results showed that this approach frequently confused visually similar furniture models.

The final architecture shifts the responsibility from a single AI decision to a structured multi-stage workflow:

1. Observe
2. Retrieve
3. Verify

This significantly improved identification accuracy while making the decision process easier to understand and debug.

---

# Future Improvements

Potential future enhancements include:

- semantic vector search
- hybrid retrieval
- larger knowledge base
- automatic feature generation
- multiple reference images per furniture model
- confidence calibration
- fine-tuned retrieval scoring