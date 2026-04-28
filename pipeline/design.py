# pipeline/design.py

def create_design(intent):

    design = {
        "pages": ["home"],
        "roles": ["user"],
        "tables": ["users"],
        "flows": []
    }

    if intent["needs_login"]:
        design["pages"].append("login")
        design["flows"].append("authentication")

    if intent["needs_dashboard"]:
        design["pages"].append("dashboard")

    if intent["needs_admin"]:
        design["pages"].append("admin")
        design["roles"].append("admin")

    if intent["needs_cart"]:
        design["pages"].append("cart")
        design["tables"].append("cart")

    if intent["needs_payment"]:
        design["pages"].append("pricing")
        design["tables"].append("payments")
        design["flows"].append("payment_gateway")

    if intent["is_crm"]:
        design["pages"].append("contacts")
        design["tables"].append("contacts")

    if intent["is_ecommerce"]:
        design["pages"].append("products")
        design["tables"].extend(["products", "orders"])

    if intent["is_job_portal"]:
        design["pages"].append("jobs")
        design["tables"].append("jobs")

    return design