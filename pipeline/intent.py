import os, json
from groq import Groq
from dotenv import load_dotenv
load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def extract_intent(prompt):
    r = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role":"user","content":f"""Extract app intent. Return JSON only, no markdown:
{{"app_name":"str","features":["str"],"entities":["str"],"roles":["str"],"has_payments":true,"auth_type":"email_password"}}
App: {prompt}"""}]
    )
    text = r.choices[0].message.content.strip().replace("```json","").replace("```","").strip()
    return json.loads(text)