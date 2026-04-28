from flask import Flask, render_template, jsonify, request
import time

app = Flask(__name__)

# --------------------
# Metrics Storage
# --------------------
stats = {
    "requests": 0,
    "success": 0,
    "failures": 0,
    "total_latency_ms": 0,
    "last_prompt": ""
}

# --------------------
# Home Page
# --------------------
@app.route('/')
def home():
    return render_template("index.html")

# --------------------
# Validation
# --------------------
def validate(data):
    required = ["pages", "database", "apis", "roles"]

    for key in required:
        if key not in data:
            data[key] = []

    return data

# --------------------
# Generate Schema
# --------------------
@app.route('/generate', methods=['POST'])
def generate():

    start = time.time()
    stats["requests"] += 1

    try:
        prompt = request.json["prompt"].lower()
        stats["last_prompt"] = prompt

        data = {
            "pages": ["home"],
            "database": ["users"],
            "apis": [],
            "roles": ["user"]
        }

        if "login" in prompt:
            data["pages"].append("login")
            data["apis"].append("/login")

        if "dashboard" in prompt:
            data["pages"].append("dashboard")

        if "admin" in prompt:
            data["pages"].append("admin")
            data["roles"].append("admin")

        if "cart" in prompt:
            data["pages"].append("cart")
            data["database"].append("cart")
            data["apis"].append("/cart")

        if "payment" in prompt or "payments" in prompt:
            data["database"].append("payments")
            data["apis"].append("/payment")

        if "crm" in prompt:
            data["database"].append("contacts")
            data["apis"].append("/contacts")

        if "ecommerce" in prompt:
            data["database"].append("products")
            data["database"].append("orders")
            data["apis"].append("/products")
            data["apis"].append("/orders")

        data = validate(data)

        data["pages"] = list(set(data["pages"]))
        data["database"] = list(set(data["database"]))
        data["apis"] = list(set(data["apis"]))
        data["roles"] = list(set(data["roles"]))

        data["status"] = "validated"
        data["pipeline"] = [
            "intent_extraction",
            "schema_generation",
            "validation",
            "deduplication"
        ]

        stats["success"] += 1

        latency = int((time.time() - start) * 1000)
        stats["total_latency_ms"] += latency

        return jsonify(data)

    except Exception as e:
        stats["failures"] += 1
        return jsonify({"error": str(e)}), 500


# --------------------
# Stats Route
# --------------------
@app.route('/stats')
def get_stats():

    avg = 0

    if stats["requests"] > 0:
        avg = int(stats["total_latency_ms"] / stats["requests"])

    return jsonify({
        "requests": stats["requests"],
        "success": stats["success"],
        "failures": stats["failures"],
        "avg_latency_ms": avg,
        "last_prompt": stats["last_prompt"]
    })

# --------------------
# Run App
# --------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)