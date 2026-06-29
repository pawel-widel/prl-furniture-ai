# Decision Log

---

## 2026-06-29

### Decision

Use SQLite instead of PostgreSQL.

### Reason

SQLite is lightweight, requires no installation and is sufficient for validating the MVP hypothesis.

---

## 2026-06-29

### Decision

Use Excel as the source of truth.

### Reason

The knowledge base is easier to maintain in Excel during early development. SQLite is generated automatically from Excel.

---

## 2026-06-29

### Decision

Implement the MVP without embeddings.

### Reason

The primary goal is to verify whether a curated knowledge base improves GPT recognition accuracy. Embeddings will be considered after validating the hypothesis.
---

## 2026-06-29

### Decision

Separate the database access logic from the user interface.

### Reason

Keeping database operations in a dedicated module improves maintainability and allows changing the data source in the future without modifying the UI.

## D-005

### Decision

Use OpenAI Responses API instead of Chat Completions.

### Reason

Responses API is the current recommended OpenAI API, supports multimodal inputs, and is the foundation for future development.