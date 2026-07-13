# PRL Furniture AI

An AI-powered application for identifying Polish Mid-Century (PRL) furniture from a single photo.

The project explores whether combining Vision AI with a structured knowledge base and a multi-stage identification pipeline can improve identification accuracy compared to standalone Vision models.

---

## Project Goal

Modern Vision models can recognize many well-known furniture designs, but they often struggle with less common Polish Mid-Century models and tend to produce confident but incorrect answers.

The goal of this project was to verify the following hypothesis:

> A structured knowledge base and a multi-stage identification pipeline can significantly improve furniture identification compared to using a Vision model alone.

---

## Final Results

Final benchmark (20 furniture models)

| Solution | Top-1 Accuracy |
|-----------|---------------:|
| GPT-5.5 Vision | 5% |
| Gemini 3.5 Flash | 25% |
| PRL Furniture AI | **35%** |

Additional findings:

- Correct model appeared in **Top 3** for 3 additional cases.
- AI Verification correctly rejected **7 incorrect matches**, reducing false positive recommendations.
- The biggest improvement came from architecture and context engineering rather than switching AI models.

---

## How It Works

```text
User Photo
      │
      ▼
Vision Feature Extraction
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
Final Result
```

Instead of asking a Vision model to directly identify a furniture model, the application first extracts visible visual features, searches a structured knowledge base for the most similar candidates, and finally verifies those candidates using a second AI reasoning step.

---

## Features

- Furniture identification from a single image
- Vision-based feature extraction
- Structured SQLite knowledge base
- Candidate ranking
- AI verification stage
- Reference image comparison
- Transparent confidence reporting

---

## Technology Stack

### AI

- OpenAI GPT-5.5
- Vision API

### Backend

- Python
- SQLite

### Frontend

- Streamlit

### Data

- Curated knowledge base
- Reference image collection

---

## Project Structure

```text
app/
database/
docs/
models/
photos/
scripts/
services/
```

---

## Running the Project

Clone the repository

```bash
git clone https://github.com/pawel-widel/prl-furniture-ai.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Configure your environment

```text
OPENAI_API_KEY=your_api_key
```

Run the application

```bash
streamlit run app/main.py
```

---

## Documentation

Project documentation is available in the `/docs` directory.

- Architecture
- Benchmark methodology
- Knowledge Base
- Design Decisions
- Changelog

---

## Screenshots


- Main screen
 <img width="892" height="458" alt="Main_search" src="https://github.com/user-attachments/assets/4d4a9ded-f265-4560-bad3-4f9f520b3217" />
 
- Identification results
 <img width="894" height="794" alt="search_result" src="https://github.com/user-attachments/assets/c76ff95d-5831-4e50-9e9e-492d47771a70" />
 
- Pipeline and AI Verification:
  
 <img width="839" height="661" alt="pipeline_and_features" src="https://github.com/user-attachments/assets/816fbe86-be4f-4abf-a541-0bff66ee5462" />
  
 <img width="1048" height="822" alt="image" src="https://github.com/user-attachments/assets/0852c521-692e-45e4-be72-f540c7aedb29" />


---

## Roadmap

### Completed

- Initial benchmark
- Knowledge Base
- Multi-stage identification pipeline
- AI Verification
- Final benchmark

### Future Improvements

- Larger furniture database
- Automatic knowledge base generation
- Better candidate ranking
- Additional furniture categories
- Fine-tuned retrieval scoring

---

## Lessons Learned

The project demonstrated that improving AI systems is not always about choosing a larger or newer model.

In this experiment, the largest improvement came from combining Vision AI with structured domain knowledge and a carefully designed multi-stage workflow.

---

## Author

**Paweł Wideł**

Business Analyst exploring AI Engineering, Knowledge-Based Systems and AI-assisted software development.

LinkedIn:
https://www.linkedin.com/in/pawel-widel

GitHub:
https://github.com/pawel-widel
