import os, json
from groq import Groq
from dotenv import load_dotenv
load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def create_design(intent):
    r = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role":"user","content":f"""Design app architecture. Return JSON only, no markdown:
{{"pages":[{{"name":"str","route":"str","auth_required":true,"roles":["str"]}}],
"apis":[{{"method":"GET","path":"str","roles":["str"],"inputs":["str"],"outputs":["str"]}}],
"database":[{{"table":"str","columns":[{{"name":"str","type":"str","primary_key":false}}]}}],
"roles":[{{"name":"str","permissions":["str"]}}]}}
Intent: {json.dumps(intent)}"""}]
    )
    text = r.choices[0].message.content.strip().replace("```json","").replace("```","").strip()
    return json.loads(text)