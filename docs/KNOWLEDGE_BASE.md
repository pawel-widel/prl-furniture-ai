# Knowledge Base

## Overview

The knowledge base is the core component of the identification pipeline.

Instead of asking a Vision model to recognize furniture directly, the application first narrows the search space using structured domain knowledge.

Each furniture model is represented by a curated set of descriptive attributes rather than only a reference image.

This allows the search stage to compare objective visual characteristics before AI performs the final verification.

---

# Purpose

The knowledge base serves three purposes:

- reduce the search space,
- provide structured information for candidate retrieval,
- support explainable AI verification.

Without this layer, the application would rely entirely on the Vision model's internal knowledge.

---

# Data Model

Each furniture model contains structured metadata describing both historical information and visual appearance.

| Field | Purpose |
|--------|---------|
| Model | Official furniture model name |
| Common Name | Popular name used by collectors |
| Designer | Furniture designer |
| Manufacturer | Original manufacturer |
| Production Years | Historical production period |
| Category | Furniture category |
| Visual Features | Human-readable description of visible characteristics |
| Construction Features | Structural description of the furniture |
| Search Features | Normalized keywords used during candidate retrieval |
| Similar Models | Frequently confused furniture models |
| Sources | Reference materials used during curation |
| Confidence | Confidence in the stored information |

---

# Search Features

Search Features are the primary retrieval mechanism used during candidate search.

Unlike natural language descriptions, they consist of normalized keywords describing only observable characteristics.

Example:

```text
rounded shell
bucket seat
integrated armrests
metal frame
four metal legs
floating shell
organic shape
```

This representation improves consistency while reducing ambiguity during matching.

---

# Visual Features

Visual Features contain human-readable descriptions intended for AI verification.

They describe:

- silhouette
- proportions
- frame geometry
- armrests
- seat
- backrest
- visible structural elements

These descriptions provide additional context that cannot easily be represented using keywords alone.

---

# Construction Features

Construction Features describe the visible structural design of the furniture.

Typical information includes:

- frame construction
- support elements
- mounting points
- upholstery structure
- exposed joints
- load-bearing elements

These descriptions help distinguish visually similar furniture models.

---

# Reference Images

Each furniture model is linked to one or more carefully selected reference photographs.

Reference images are used only during the AI Verification stage.

They provide visual evidence for comparing the uploaded furniture against curated examples.

---

# Knowledge Base Curation

The knowledge base was created manually.

Information was collected from:

- historical furniture catalogues
- museum collections
- manufacturer documentation
- specialist publications
- verified auction listings
- expert reference materials

Each furniture entry was reviewed individually before being added to the database.

---

# Why Not Use RAG?

Traditional Retrieval-Augmented Generation focuses primarily on retrieving textual documents.

This project solves a different problem.

Instead of retrieving documents, the system retrieves furniture models described using structured visual characteristics.

A lightweight structured database proved sufficient for the project's scope while remaining easy to maintain and explain.

---

# Current Scope

The current version of the knowledge base contains:

- 20 furniture models
- manually curated descriptions
- normalized search keywords
- reference photographs
- historical metadata

The database was intentionally kept small to validate the project hypothesis before investing in larger-scale data collection.

---

# Future Improvements

Potential future enhancements include:

- larger furniture collections
- multiple reference images per model
- automatic feature generation
- semantic vector search
- confidence calibration
- automated data validation
- hybrid retrieval methods

---

# Key Takeaway

The benchmark demonstrated that the knowledge base is not merely a storage layer.

It is an active component of the identification pipeline that enables efficient candidate retrieval, improves transparency, and provides structured context for AI verification.

The project suggests that carefully designed domain knowledge can contribute more to overall system performance than simply switching to a larger Vision model.