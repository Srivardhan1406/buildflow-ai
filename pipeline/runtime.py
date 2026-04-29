def simulate_runtime(schema):

    checks = {
        "pages_valid": len(schema.get("pages", [])) > 0,
        "apis_valid": True,
        "database_valid": True,
        "roles_valid": len(schema.get("roles", [])) > 0
    }

    apis = schema.get("apis", [])
    db = schema.get("database", [])
    pages = schema.get("pages", [])
    roles = schema.get("roles", [])

    # login needs users table
    if "/login" in apis and "users" not in db:
        checks["database_valid"] = False

    # payment needs payments table
    if "/payment" in apis and "payments" not in db:
        checks["database_valid"] = False

    # admin page needs admin role
    if "admin" in pages and "admin" not in roles:
        checks["roles_valid"] = False

    runtime_ready = all(checks.values())

    return {
        "runtime_ready": runtime_ready,
        "runtime_checks": checks
    }