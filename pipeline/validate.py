# pipeline/validate.py

def validate_schema(data):

    required = ["pages", "database", "roles", "apis"]

    for key in required:
        if key not in data:
            data[key] = []

    for key in required:
        if not isinstance(data[key], list):
            data[key] = []

    if len(data["pages"]) == 0:
        data["pages"].append("home")

    if len(data["database"]) == 0:
        data["database"].append("users")

    if len(data["roles"]) == 0:
        data["roles"].append("user")

    return data