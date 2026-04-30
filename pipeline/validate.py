# pipeline/validate.py

def validate_schema(data):

    errors = []

    # --- Basic keys ---
    required = ["pages", "database", "roles", "apis", "ui_schema", "api_schema", "db_schema", "auth_schema"]
    for key in required:
        if key not in data:
            data[key] = [] if key != "auth_schema" else {}
            errors.append(f"Missing key: {key}")

    # --- DB tables must have primary key ---
    for table in data.get("db_schema", []):
        has_pk = any(c.get("primary_key") for c in table.get("columns", []))
        if not has_pk:
            errors.append(f"Table '{table['table']}' missing primary key")

    # --- API roles must exist in auth ---
    defined_roles = {r["name"] for r in data.get("auth_schema", {}).get("roles", [])}
    for ep in data.get("api_schema", []):
        for role in ep.get("allowed_roles", []):
            if role not in defined_roles:
                errors.append(f"Role '{role}' in API '{ep['path']}' not in auth schema")

    # --- API response fields must exist in DB ---
    db_columns = set()
    for table in data.get("db_schema", []):
        for col in table.get("columns", []):
            db_columns.add(col["name"])

    skip_fields = {"token", "message", "status", "success", "total", "count", "data"}
    for ep in data.get("api_schema", []):
        for field in ep.get("response_fields", []):
            if field not in db_columns and field not in skip_fields:
                errors.append(f"API '{ep['path']}' response field '{field}' not in any DB table")

    data["validation_errors"] = errors
    data["valid"] = len(errors) == 0
    return data