# pipeline/intent.py

def extract_intent(prompt):
    text = prompt.lower()

    return {
        "raw_prompt": prompt,

        "needs_login": any(word in text for word in [
            "login", "signin", "sign in", "auth"
        ]),

        "needs_admin": any(word in text for word in [
            "admin", "administrator"
        ]),

        "needs_dashboard": any(word in text for word in [
            "dashboard", "analytics", "panel"
        ]),

        "needs_cart": "cart" in text,

        "needs_payment": any(word in text for word in [
            "payment", "payments", "checkout", "subscription", "premium"
        ]),

        "is_crm": any(word in text for word in [
            "crm", "contacts", "sales"
        ]),

        "is_ecommerce": any(word in text for word in [
            "ecommerce", "store", "shop", "product"
        ]),

        "is_job_portal": any(word in text for word in [
            "job", "jobs", "career", "recruitment", "portal"
        ])
    }