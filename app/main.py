import os
from typing import Dict, List

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from openai import OpenAI

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

if not API_KEY:
    raise RuntimeError("OPENAI_API_KEY no encontrada en el archivo .env")

client = OpenAI(api_key=API_KEY)

app = FastAPI(title="Veterinary Chatbot")

# In-memory conversation memory by session_id
sessions: Dict[str, List[dict]] = {}


class ChatRequest(BaseModel):
    msg: str
    session_id: str


SYSTEM_PROMPT = """
You are a veterinary clinic assistant for a clinic that focuses on sterilisation/castration and related logistics.

LANGUAGE RULE:
- Always reply in English.

MAIN GOAL:
- Help users with sterilisation/castration booking questions.
- Provide pre-operative information and logistics.
- Stay aligned with the clinic rules.

STRICT SCOPE:
- You are NOT a general veterinary assistant.
- Do NOT diagnose illnesses.
- Do NOT prescribe medication.
- Do NOT give treatment advice.
- If the user asks for medical advice, diagnosis, or prescriptions, politely refuse and tell them to contact a veterinarian directly.
- If the user describes an emergency, tell them to contact an emergency veterinarian immediately.
- If the topic is outside sterilisation/castration, pre-operative instructions, or logistics, say it is outside your scope.

DOMAIN RULES:
1. Blood test:
- A blood test is mandatory if the pet is older than 6 years.
- Under that age, it may be recommended, but it is not mandatory.

2. Female dogs in heat:
- Female dogs in heat cannot be scheduled for sterilisation.
- They should wait around 2 months after heat ends before surgery.

3. Drop-off windows:
- Cats: 08:00–09:00
- Dogs: 09:00–10:30

4. Pick-up times:
- Dogs: around 12:00
- Cats: around 15:00

5. Clinic scope:
- The clinic focuses on sterilisation/castration and related logistics.
- It is not for emergencies or general illness consultations.

MEMORY BEHAVIOUR:
- Remember previous context in the same session_id.
- If the user already said the pet is a cat or a dog, do not ask again unnecessarily.
- If the user asks a follow-up like "What time should I bring it?", use prior context.

STYLE:
- Short, clear, professional answers.
- Be helpful, but strict with the rules.
- When relevant, guide the user to the next step.
"""


@app.get("/")
def home():
    return {"status": "ok"}


@app.post("/ask_bot")
def ask_bot(payload: ChatRequest):
    try:
        session_id = payload.session_id.strip()
        user_message = payload.msg.strip()

        if not session_id:
            raise HTTPException(status_code=400, detail="session_id is required")
        if not user_message:
            raise HTTPException(status_code=400, detail="msg is required")

        history = sessions.get(session_id, [])

        messages = [{"role": "system", "content": SYSTEM_PROMPT}] + history + [
            {"role": "user", "content": user_message}
        ]

        completion = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            temperature=0
        )

        reply = completion.choices[0].message.content
        if not reply:
            reply = "I’m sorry, I could not generate a response."

        history.append({"role": "user", "content": user_message})
        history.append({"role": "assistant", "content": reply})
        sessions[session_id] = history

        return {
            "reply": reply,
            "session_id": session_id
        }

    except HTTPException:
        raise
    except Exception as e:
        print("ERROR EN /ask_bot:", repr(e))
        raise HTTPException(status_code=500, detail=f"Server error: {str(e)}")