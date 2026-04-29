from flask import Flask, render_template, request, jsonify
from pipeline.intent import extract_intent
from pipeline.design import create_design
from pipeline.schema import generate_schema
from pipeline.validate import validate_schema
from pipeline.repair import repair_schema
from pipeline.runtime import simulate_runtime
import time
import os

app = Flask(__name__)

# ---------------------------------
# Metrics Storage
# ---------------------------------
stats = {
    "requests": 0,
    "success": 0,
    "clarifications": 0,
    "failures": 0,
    "repairs": 0,
    "total_latency_ms": 0
}


# ---------------------------------
# Home Route
# ---------------------------------
@app.route("/")
def home():
    return render_template("index.html")


# ---------------------------------
# Generate Route
# ---------------------------------
@app.route("/generate", methods=["POST"])
def generate():

    start = time.time()
    stats["requests"] += 1

    try:
        body = request.get_json()

        if not body or "prompt" not in body:
            stats["failures"] += 1
            return jsonify({
                "status": "failed",
                "error": "Prompt is required"
            }), 400

        prompt = body["prompt"].strip()

        # ---------------------------------
        # Clarification Handling
        # ---------------------------------
        vague_inputs = [
            "build app",
            "make app",
            "create app",
            "build website",
            "create platform"
        ]

        if len(prompt) < 8 or prompt.lower() in vague_inputs:

            stats["clarifications"] += 1

            latency = int((time.time() - start) * 1000)
            stats["total_latency_ms"] += latency

            return jsonify({
                "status": "clarification_required",
                "needs_clarification": True,
                "questions": [
                    "What type of app do you want?",
                    "Do you need login/authentication?",
                    "Do you need admin dashboard?",
                    "Do you need payments?",
                    "Who are the users?"
                ]
            })

        # ---------------------------------
        # Stage 1: Intent Extraction
        # ---------------------------------
        intent = extract_intent(prompt)

        # ---------------------------------
        # Stage 2: System Design
        # ---------------------------------
        design = create_design(intent)

        # ---------------------------------
        # Stage 3: Schema Generation
        # ---------------------------------
        schema = generate_schema(design)

        # ---------------------------------
        # Stage 4: Validation
        # ---------------------------------
        schema = validate_schema(schema)

        # ---------------------------------
        # Stage 5: Repair
        # ---------------------------------
        before_pages = len(schema["pages"])

        schema = repair_schema(schema)

        after_pages = len(schema["pages"])

        if before_pages != after_pages:
            stats["repairs"] += 1

        # ---------------------------------
        # Stage 6: Runtime Simulation
        # ---------------------------------
        runtime = simulate_runtime(schema)

        # ---------------------------------
        # Final Metadata
        # ---------------------------------
        schema["status"] = "success"
        schema["deterministic"] = True
        schema["runtime_ready"] = runtime["runtime_ready"]
        schema["runtime_checks"] = runtime["runtime_checks"]

        schema["pipeline_trace"] = {
            "stage_1": "intent_extraction",
            "stage_2": "system_design",
            "stage_3": "schema_generation",
            "stage_4": "validation",
            "stage_5": "repair",
            "stage_6": "runtime_simulation"
        }

        # ---------------------------------
        # Metrics Update
        # ---------------------------------
        stats["success"] += 1

        latency = int((time.time() - start) * 1000)
        stats["total_latency_ms"] += latency

        schema["latency_ms"] = latency

        return jsonify(schema)

    except Exception as e:

        stats["failures"] += 1

        latency = int((time.time() - start) * 1000)
        stats["total_latency_ms"] += latency

        return jsonify({
            "status": "failed",
            "error": str(e)
        }), 500


# ---------------------------------
# Stats Route
# ---------------------------------
@app.route("/stats")
def get_stats():

    avg = 0

    if stats["requests"] > 0:
        avg = int(stats["total_latency_ms"] / stats["requests"])

    success_rate = 0

    if stats["requests"] > 0:
        success_rate = round(
            (stats["success"] / stats["requests"]) * 100, 2
        )

    return jsonify({
        "requests": stats["requests"],
        "success": stats["success"],
        "clarifications": stats["clarifications"],
        "failures": stats["failures"],
        "repairs": stats["repairs"],
        "avg_latency_ms": avg,
        "success_rate_percent": success_rate
    })


# ---------------------------------
# Run App
# ---------------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)