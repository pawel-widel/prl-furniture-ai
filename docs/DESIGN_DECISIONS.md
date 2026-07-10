# Design Decisions

## Overview

This document summarizes the major architectural and technical decisions made during the development of PRL Furniture AI.

The project intentionally prioritizes simplicity, explainability and maintainability over architectural complexity.

---

# Why Streamlit?

The goal of the project was to validate an AI hypothesis rather than build a production-ready web application.

Streamlit allowed rapid iteration while keeping the focus on the identification pipeline instead of frontend development.

**Benefits**

- rapid prototyping
- minimal boilerplate
- excellent support for AI applications
- easy deployment

---

# Why SQLite?

The knowledge base currently contains a relatively small number of curated furniture models.

SQLite provides:

- zero infrastructure
- simple maintenance
- sufficient performance
- easy portability

A larger database system would introduce unnecessary complexity without providing meaningful benefits for the MVP.

---

# Why GPT-5.5 Vision?

The project required a Vision model capable of:

- extracting structured visual features
- comparing two furniture images
- producing consistent JSON outputs

The architecture was intentionally designed so that the Vision model can be replaced with another provider without changing the remaining pipeline.

---

# Why a Multi-Stage Pipeline?

Early experiments relied on direct furniture identification using Vision models.

Benchmark results showed that this approach frequently confused visually similar furniture models and produced overly confident incorrect answers.

The final architecture separates identification into distinct stages:

1. Feature Extraction
2. Candidate Search
3. AI Verification

This reduces hallucinations while making the reasoning process significantly more transparent.

---

# Why Feature Extraction Instead of Direct Classification?

Instead of asking the model:

> "What furniture is this?"

the application first asks:

> "What can you objectively observe?"

This separation encourages evidence-based reasoning and allows deterministic search before AI performs the final comparison.

---

# Why a Structured Knowledge Base?

Large language models already contain general knowledge about famous furniture designs.

However, they lack reliable knowledge about many Polish Mid-Century models.

A curated knowledge base provides:

- structured context
- consistent terminology
- deterministic retrieval
- explainable matching

The benchmark demonstrated that this component contributed more to overall performance than changing the Vision model itself.

---

# Why Top-5 Candidate Retrieval?

Searching the entire database during AI verification would increase cost and latency.

Instead, the retrieval stage narrows the search space to the five most relevant candidates.

This keeps the verification stage efficient while maintaining a high probability of including the correct model.

---

# Why AI Verification?

Candidate search is intentionally lightweight and heuristic-based.

Rather than relying solely on similarity scores, every candidate is verified using an independent Vision comparison.

This additional step reduces false-positive recommendations and provides greater confidence in the final result.

---

# Why Not Fine-Tuning?

Fine-tuning was intentionally excluded from the MVP.

The objective was to determine whether architecture alone could improve identification performance.

Keeping the models unchanged made it possible to isolate the impact of the pipeline itself.

---

# Why Not RAG?

Traditional Retrieval-Augmented Generation retrieves textual documents.

This project retrieves furniture models represented by structured visual attributes.

A normalized relational database proved simpler, more transparent and easier to maintain than a document-based RAG solution.

---

# Why Manual Knowledge Curation?

The project focuses on quality rather than scale.

Each furniture model was reviewed manually to ensure:

- consistent terminology
- comparable descriptions
- reliable reference sources
- high-quality search features

Although time-consuming, manual curation produced a cleaner benchmark dataset.

---

# Design Philosophy

Several principles guided the development of this project.

## Keep the architecture simple

Every component should have a single responsibility.

---

## Prefer deterministic logic where possible

AI should solve problems that require reasoning.

Everything else should remain deterministic and explainable.

---

## Optimize for transparency

Users should be able to inspect intermediate results rather than receiving only a final prediction.

---

## Validate assumptions with benchmarks

Architectural decisions should be supported by measurable results rather than intuition.

---

## Build an MVP first

The project intentionally avoids premature optimization and unnecessary complexity.

Each new component was introduced only after demonstrating its value through experimentation.

---

# Key Takeaway

The benchmark showed that the largest improvement did not come from using a larger AI model.

Instead, the improvement resulted from combining structured domain knowledge with a carefully designed multi-stage identification pipeline.

The project demonstrates that, in many AI systems, architecture can have a greater impact than the model itself.