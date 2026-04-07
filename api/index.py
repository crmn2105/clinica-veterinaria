from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import json
import os
from openai import OpenAI
from api.session_id import get_history, save_history

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

SYSTEM_PROMPT = """
You are a veterinary clinic assistant chatbot.

YOUR SCOPE:
- Help users with sterilisation/castration booking
- Provide pre-operative instructions
- Explain drop-off and pick-up logistics
- Explain basic clinic scheduling rules

STRICT RULES:
- Do NOT diagnose illnesses
- Do NOT prescribe medication
- Do NOT provide treatment advice
- If the user describes an emergency, tell them to contact an emergency veterinarian immediately
- If the user asks for general medical advice outside sterilisation logistics, tell them to contact a veterinarian directly

DOMAIN RULES:
- Blood test is mandatory if the pet is older than 6 years
- Female dogs in heat cannot be scheduled; they must wait around 2 months after heat ends
- Cat drop-off window: 08:00-09:00
- Dog drop-off window: 09:00-10:30
- Dog pick-up time: around 12:00
- Cat pick-up time: around 15:00
- Keep answers aligned with sterilisation, pre-op instructions, and logistics

STYLE:
- Short answers
- Clear and professional
- Helpful but strict with the rules
"""

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            parsed_url = urlparse(self.path)
            params = parse_qs(parsed_url.query)

            user_msg = params.get("msg", ["Hola"])[0].strip()
            session_id = params.get("session_id", ["default"])[0].strip()

            history = get_history(session_id)

            messages = [
                {"role": "system", "content": SYSTEM_PROMPT}
            ]

            for past_user_msg, past_bot_msg in history:
                messages.append({"role": "user", "content": past_user_msg})
                messages.append({"role": "assistant", "content": past_bot_msg})

            messages.append({"role": "user", "content": user_msg})

            completion = client.chat.completions.create(
                model=os.environ.get("OPENAI_MODEL", "gpt-4o-mini"),
                messages=messages,
                temperature=0
            )

            reply = completion.choices[0].message.content or "No response generated."

            save_history(session_id, user_msg, reply)

            self.send_response(200)
            self.send_header("Content-type", "application/json; charset=utf-8")
            self.end_headers()

            self.wfile.write(json.dumps({
                "session_id": session_id,
                "msg": user_msg,
                "respuesta": reply
            }, ensure_ascii=False).encode("utf-8"))

        except Exception as e:
            self.send_response(500)
            self.send_header("Content-type", "application/json; charset=utf-8")
            self.end_headers()

            self.wfile.write(json.dumps({
                "error": str(e)
            }, ensure_ascii=False).encode("utf-8"))