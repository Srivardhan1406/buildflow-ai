# pipeline/schema.py

def generate_schema(design):

    data = {
        "pages": design["pages"],
        "database": design["tables"],
        "roles": design["roles"],
        "apis": []
    }

    if "login" in data["pages"]:
        data["apis"].append("/login")

    if "admin" in data["pages"]:
        data["apis"].append("/admin")

    if "cart" in data["pages"]:
        data["apis"].append("/cart")

    if "products" in data["pages"] or "products" in data["database"]:
        data["apis"].append("/products")

    if "orders" in data["database"]:
        data["apis"].append("/orders")

    if "payments" in data["database"]:
        data["apis"].append("/payment")

    if "contacts" in data["database"]:
        data["apis"].append("/contacts")

    if "jobs" in data["database"]:
        data["apis"].append("/jobs")

    return data