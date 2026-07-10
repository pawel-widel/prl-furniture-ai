# Benchmark

## Overview

This project was created to answer a single question:

> Can a structured knowledge base and a multi-stage AI pipeline improve furniture identification compared to standalone Vision models?

Rather than comparing different prompts or larger language models, the benchmark evaluates whether system architecture has a measurable impact on identification accuracy.

---

# Hypothesis

The project assumes that combining:

- Vision-based feature extraction,
- a structured knowledge base,
- deterministic candidate retrieval,
- and AI verification

produces more accurate and more reliable results than using a Vision model alone.

---

# Benchmark Design

## Dataset

The benchmark consists of:

- 20 Polish Mid-Century furniture models
- 20 real-world photographs
- one image per furniture model

The dataset contains both popular and less common furniture designs to reduce bias toward well-known objects.

---

## Compared Solutions

Three independent approaches were evaluated.

### GPT-5.5 Vision

Direct furniture identification from a single image.

No external knowledge.

---

### Gemini 2.5 Flash

Direct furniture identification from a single image.

No external knowledge.

---

### PRL Furniture AI

Custom multi-stage pipeline consisting of:

1. Vision Feature Extraction
2. Knowledge Base Search
3. Top-5 Candidate Ranking
4. AI Verification
5. Final Recommendation

---

# Evaluation Metrics

## Top-1 Accuracy

Percentage of correctly identified furniture models.

---

## Top-3 Accuracy

Whether the correct furniture model appeared within the three highest-ranked candidates.

This metric evaluates retrieval quality independently of the final ranking.

---

## AI Verification

Whether the verification stage correctly rejected incorrect candidate matches.

This metric evaluates the ability to reduce false-positive identifications.

---

# Results

| Solution | Top-1 Accuracy |
|-----------|---------------:|
| GPT-5.5 Vision | **5%** |
| Gemini 2.5 Flash | **25%** |
| PRL Furniture AI | **35%** |

---

## Top-3 Retrieval

For cases where the final prediction was incorrect:

| Solution | Correct model in Top 3 |
|-----------|-----------------------:|
| GPT-5.5 Vision | 0 |
| Gemini 2.5 Flash | 0 |
| PRL Furniture AI | **3** |

This indicates that the retrieval stage frequently selected the correct candidate even when the final ranking was imperfect.

---

## AI Verification

Among incorrect search results:

- AI Verification rejected **7 incorrect candidates**
- preventing them from being presented as confident matches

This demonstrates that the verification stage can reduce false-positive recommendations and improve system transparency.

---

# Discussion

The benchmark shows that the largest performance improvement did not come from switching to a more capable Vision model.

Instead, the improvement resulted from introducing structure into the identification process.

Breaking the task into multiple stages allowed the system to:

- reduce the search space,
- compare only the most relevant candidates,
- separate feature extraction from reasoning,
- explicitly verify the final prediction.

This architecture outperformed both standalone Vision models tested during the benchmark.

---

# Limitations

This benchmark represents a proof of concept rather than a production-scale evaluation.

Current limitations include:

- only 20 furniture models,
- one benchmark image per model,
- manually curated knowledge base,
- heuristic candidate scoring,
- no semantic retrieval,
- no fine-tuning.

The reported results should therefore be interpreted as evidence supporting the architectural hypothesis rather than absolute performance measurements.

---

# Future Work

Potential improvements include:

- expanding the knowledge base,
- larger benchmark datasets,
- semantic retrieval,
- hybrid search,
- retrieval optimization,
- confidence calibration,
- automatic feature generation,
- multiple reference images per furniture model.

---

# Conclusion

The benchmark supports the original project hypothesis.

A carefully designed multi-stage pipeline combining Vision AI with structured domain knowledge achieved higher identification accuracy than standalone Vision models.

More importantly, the architecture not only improved retrieval quality but also demonstrated the ability to recognize when no reliable match was available, reducing false-positive recommendations.