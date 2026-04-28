# pipeline/repair.py

def repair_schema(data):

    keys = ["pages", "database", "roles", "apis"]

    for key in keys:
        cleaned = []

        for item in data[key]:
            if item and item not in cleaned:
                cleaned.append(item)

        data[key] = cleaned

    if "home" not in data["pages"]:
        data["pages"].insert(0, "home")

    if "user" not in data["roles"]:
        data["roles"].append("user")

    if "/login" not in data["apis"] and "login" in data["pages"]:
        data["apis"].append("/login")

    if "/payment" not in data["apis"] and "payments" in data["database"]:
        data["apis"].append("/payment")

    return data