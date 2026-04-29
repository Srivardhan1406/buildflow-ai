# pipeline/design.py

def create_design(intent):

    design = {
        "pages": ["home"],
        "apis": [],
        "database": [],
        "roles": ["user"]
    }

    # Core
    if intent["login"]:
        design["pages"].append("login")
        design["apis"].append("/login")
        design["database"].append("users")

    if intent["dashboard"]:
        design["pages"].append("dashboard")

    if intent["admin"]:
        design["pages"].append("admin")
        design["apis"].append("/admin")
        design["roles"].append("admin")

    if intent["payment"]:
        design["apis"].append("/payment")
        design["database"].append("payments")

    # CRM
    if intent["crm"]:
        design["pages"].append("contacts")
        design["apis"].append("/contacts")
        design["database"].append("contacts")

    # Ecommerce
    if intent["ecommerce"]:
        design["pages"].append("products")
        design["pages"].append("cart")
        design["apis"].append("/products")
        design["apis"].append("/cart")
        design["database"].append("products")
        design["database"].append("cart")

    # Job Portal
    if intent["job_portal"]:
        design["pages"].append("jobs")
        design["apis"].append("/jobs")
        design["database"].append("jobs")

    # Hospital
    if intent["hospital"]:
        design["pages"].append("patients")
        design["pages"].append("appointments")
        design["apis"].append("/patients")
        design["apis"].append("/appointments")
        design["database"].append("patients")
        design["database"].append("appointments")
        design["roles"].append("doctor")

    # Edtech
    if intent["edtech"]:
        design["pages"].append("courses")
        design["pages"].append("progress")
        design["apis"].append("/courses")
        design["apis"].append("/progress")
        design["database"].append("courses")
        design["database"].append("progress")

    # Marketplace
    if intent["marketplace"]:
        design["pages"].append("listings")
        design["apis"].append("/listings")
        design["database"].append("listings")
        design["roles"].append("seller")

    return design