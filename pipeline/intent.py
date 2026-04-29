# pipeline/intent.py

def extract_intent(prompt):

    text = prompt.lower()

    intent = {
        "login": False,
        "admin": False,
        "payment": False,
        "dashboard": False,
        "crm": False,
        "ecommerce": False,
        "job_portal": False,
        "hospital": False,
        "edtech": False,
        "marketplace": False
    }

    # Core
    if "login" in text or "auth" in text:
        intent["login"] = True

    if "admin" in text or "analytics" in text:
        intent["admin"] = True

    if "payment" in text or "billing" in text or "subscription" in text:
        intent["payment"] = True

    if "dashboard" in text:
        intent["dashboard"] = True

    # Existing Domains
    if "crm" in text or "contacts" in text:
        intent["crm"] = True

    if "ecommerce" in text or "cart" in text or "products" in text:
        intent["ecommerce"] = True

    if "job" in text or "portal" in text or "recruitment" in text:
        intent["job_portal"] = True

    # New Domains
    if "hospital" in text or "doctor" in text or "patient" in text:
        intent["hospital"] = True

    if "course" in text or "student" in text or "quiz" in text or "edtech" in text:
        intent["edtech"] = True

    if "marketplace" in text or "seller" in text or "buyer" in text:
        intent["marketplace"] = True

    return intent