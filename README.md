# 🚀 BuildFlow AI

BuildFlow AI is a compiler-style AI platform that transforms natural language product ideas into structured, validated, runtime-ready application schemas using a multi-stage LLM pipeline powered by Groq.

---

## 🌐 Live Demo

[https://buildflow-ai-bepz.onrender.com](https://buildflow-ai-bepz.onrender.com)

---

## 🎯 Objective

Convert prompts like:

> "Build a job portal with login, jobs, admin and payments"

Into complete structured schemas:

- UI Schema (pages, routes, components)
- API Schema (endpoints, methods, roles, fields)
- Database Schema (tables, columns, types, primary keys)
- Auth Schema (JWT, roles, permissions)
- Validation Report
- Runtime-Ready Output

---

## 🧠 Core Architecture

```
Natural Language Prompt
        ↓
Stage 1 — Intent Extraction      (LLM: features, entities, roles)
        ↓
Stage 2 — System Design          (LLM: pages, APIs, DB, roles)
        ↓
Stage 3 — Schema Generation      (LLM: UI + API + DB + Auth schemas)
        ↓
Stage 4 — Validation Engine      (rule-based cross-layer checks)
        ↓
Stage 5 — Repair Engine          (LLM: fixes only broken parts)
        ↓
Stage 6 — Runtime Simulation     (verifies output is executable)
        ↓
Final Validated JSON Output
```

---

## ⚙️ Multi-Stage Pipeline

### Stage 1 — Intent Extraction
LLM parses the prompt into structured intent:
- app name, features, entities, roles
- has_payments, auth_type

### Stage 2 — System Design
LLM converts intent into architecture:
- pages with routes and auth rules
- API endpoints with methods and roles
- database tables with columns
- role definitions with permissions

### Stage 3 — Schema Generation
LLM produces 4 detailed schemas:

```json
{
  "ui_schema":   [...],
  "api_schema":  [...],
  "db_schema":   [...],
  "auth_schema": {...}
}
```

### Stage 4 — Validation Engine
Rule-based checks across all layers:
- Every DB table has a primary key
- All API roles exist in auth schema
- Response fields match DB columns
- No empty schemas

### Stage 5 — Repair Engine
LLM fixes only the broken parts — no full retry:
- Targeted repair using exact error messages
- Preserves correct schemas untouched

### Stage 6 — Runtime Simulation
Verifies the output is executable:
- All schema keys present and non-empty
- No validation errors remaining
- Returns `runtime_ready: true`

---

## 🛡️ Reliability Features

✅ Multi-stage LLM pipeline (not a single prompt)  
✅ Cross-layer validation (API ↔ DB ↔ Auth ↔ UI)  
✅ Intelligent repair (fixes only what's broken)  
✅ Deterministic structure (same input → consistent output)  
✅ Runtime-ready output (no manual fixes needed)  
✅ Metrics observability  
✅ Production deployment ready  

---

## 📊 Metrics

Tracked at `/stats`:

- Total requests
- Successful generations
- Failures
- Repairs triggered
- Average latency (ms)

---

## 🧪 Example Output

```json
{
  "ui_schema": [
    {"page": "Login", "route": "/login", "auth_required": false, "components": [...]}
  ],
  "api_schema": [
    {"method": "POST", "path": "/api/login", "roles": ["user", "admin"], "response": {"fields": ["token"]}}
  ],
  "db_schema": [
    {"table": "users", "columns": [{"name": "id", "type": "UUID", "primary_key": true}]}
  ],
  "auth_schema": {
    "method": "jwt",
    "token_expiry_hours": 24,
    "roles": [{"name": "admin", "permissions": ["read:all", "write:all"]}]
  },
  "valid": true,
  "validation_errors": [],
  "runtime_ready": true,
  "latency_ms": 7529
}
```

---

## 💻 Tech Stack

- Python + Flask
- Groq API (Llama 3.3 70B) — free, fast inference
- Rule-based validation engine
- Render (deployment)
- GitHub

---

## 📁 Project Structure

```
buildflow-ai/
├── app.py
├── requirements.txt
├── README.md
├── pipeline/
│   ├── intent.py      Stage 1: intent extraction
│   ├── design.py      Stage 2: system design
│   ├── schema.py      Stage 3: schema generation
│   ├── validate.py    Stage 4: validation engine
│   ├── repair.py      Stage 5: repair engine
│   └── runtime.py     Stage 6: runtime simulation
├── templates/
│   └── index.html
└── static/
    └── style.css
```

---

## ▶️ Run Locally

```
pip install -r requirements.txt
```

Create `.env` file:
```
GROQ_API_KEY
```

Run:
```
python app.py
```

Open: http://127.0.0.1:5000

---

## 🚀 Deployment

Hosted on Render using:
```
gunicorn app:app
```

---

## 📈 Tradeoffs

| Factor | Decision |
|--------|----------|
| Latency | ~7s for 4 LLM calls — acceptable for schema generation |
| Cost | Free using Groq |
| Quality | Detailed schemas with cross-layer consistency |
| Reliability | Auto-repair ensures valid output always returned |

---

## 📈 Future Improvements

- SQL migration file export
- React component generation
- Backend code scaffolding
- Agentic refinement loop
- Support for more domains

---

## 🧠 Why This Stands Out

This is not a basic prompt-to-JSON demo.

It is an engineered AI system emphasizing:
- LLM control and structured output
- Cross-layer schema consistency
- Intelligent targeted repair
- Measurable reliability metrics
- Execution-ready output

---

## 👨‍💻 Author

Sri Vardhan