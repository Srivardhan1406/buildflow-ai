# pipeline/schema.py

def generate_schema(design):

    schema = {
        "pages": list(set(design["pages"])),
        "apis": list(set(design["apis"])),
        "database": list(set(design["database"])),
        "roles": list(set(design["roles"]))
    }

    schema["pages"].sort()
    schema["apis"].sort()
    schema["database"].sort()
    schema["roles"].sort()

    return schema