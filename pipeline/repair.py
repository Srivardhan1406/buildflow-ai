import os, json
from groq import Groq
from dotenv import load_dotenv
load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def repair_schema(schema):
    errors = schema.get("validation_errors", [])
    if not errors:
        return schema
    r = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role":"user","content":f"""Fix these errors in schema. Return corrected JSON only, no markdown:
Errors: {errors}
Schema: {json.dumps(schema)}"""}]
    )
    text = r.choices[0].message.content.strip().replace("```json","").replace("```","").strip()
    repaired = json.loads(text)
    repaired["validation_errors"] = []
    repaired["valid"] = True
    return repaired