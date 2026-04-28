# 🚀 BuildFlow AI

BuildFlow AI is a compiler-style AI platform that transforms natural language product ideas into structured, validated, runtime-ready application schemas.

Unlike simple prompt wrappers, BuildFlow AI uses a multi-stage deterministic generation pipeline focused on reliability, control, and execution readiness.

---

# 🌐 Live Demo

[https://buildflow-ai-bepz.onrender.com](https://buildflow-ai-bepz.onrender.com)

---

# 🎯 Objective

Convert prompts like:

Build a CRM with login, contacts, dashboard, role-based access, and premium plan with payments. Admins can see analytics.

Into:

* UI Schema
* API Schema
* Database Schema
* Roles & Permissions
* Validation Checks
* Repair Logic
* Runtime-Ready Output

---

# 🧠 Core Architecture

Natural Language Prompt
↓
Intent Extraction
↓
System Design Layer
↓
Schema Generation
↓
Validation Engine
↓
Repair Engine
↓
Reliable JSON Output
↓
Metrics + Runtime Ready Response

---

# ⚙️ Multi-Stage Pipeline

## 1. Intent Extraction

Parses user prompt into structured intent signals.

Detects:

* login
* admin
* dashboard
* payments
* ecommerce
* CRM
* job portal
* cart
* premium plans

## 2. System Design Layer

Transforms intent into architecture:

* pages
* modules
* user roles
* data entities
* business flows

## 3. Schema Generation

Produces structured JSON:

{
"pages": [],
"apis": [],
"database": [],
"roles": []
}

## 4. Validation Engine

Guarantees:

* valid JSON
* required fields exist
* correct data types
* non-empty critical sections
* structural consistency

## 5. Repair Engine

Automatically fixes:

* duplicate values
* missing home page
* missing user role
* missing login API
* missing payment API

Without blindly regenerating the full output.

---

# 🛡️ Reliability Features

✅ Deterministic behavior
✅ Multi-stage modular pipeline
✅ Validation + repair
✅ Runtime usable output
✅ Metrics observability
✅ Handles vague prompts
✅ Production deployment ready

---

# 🤖 Clarification Handling

If input is vague:

Build app

System responds with:

* What type of app?
* Need login?
* Need payments?
* Need admin dashboard?
* Who are the users?

---

# 📊 Metrics Endpoint

Tracks:

* total requests
* successful generations
* clarifications
* failures
* repairs
* average latency

Endpoint:

/stats

---

# 🧪 Example Output

{
"pages": ["home", "login", "dashboard", "admin"],
"apis": ["/login", "/admin", "/payment"],
"database": ["users", "payments"],
"roles": ["user", "admin"],
"status": "success",
"runtime_ready": true
}

---

# 💻 Tech Stack

* Python
* Flask
* HTML
* CSS
* JavaScript
* Render
* GitHub

---

# 📁 Project Structure

buildflow-ai/
│── app.py
│── requirements.txt
│── README.md

├── pipeline/
│   ├── intent.py
│   ├── design.py
│   ├── schema.py
│   ├── validate.py
│   └── repair.py

├── templates/
│   └── index.html

└── static/
└── style.css

---

# ▶️ Run Locally

pip install -r requirements.txt
python app.py

Open:

[http://127.0.0.1:5000](http://127.0.0.1:5000)

---

# 🚀 Deployment

Hosted on Render using:

gunicorn app:app

---

# 📈 Future Improvements

* LLM-powered intent extraction
* SQL schema generator
* React UI generation
* Backend code export
* Full app scaffolding
* Agentic refinement loop

---

# 🧠 Why This Project Stands Out

This is not a basic prompt-to-JSON demo.

It is an engineered AI system emphasizing:

* control
* consistency
* reliability
* modular generation
* execution readiness
* measurable performance

---

# 👨‍💻 Author

Sri Vardhan
