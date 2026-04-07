RAG_SOURCE_URL = "https://veterinary-clinic-teal.vercel.app/en/docs/instructions-before-operation"

PREOP_TEXT = """
Official pre-operative instructions for the clinic:

- Food must be stopped 8 to 12 hours before surgery.
- Water is allowed until 1 to 2 hours before surgery.
- Pets older than 6 years require a blood test before surgery.
- Dogs and cats should be vaccinated and dewormed.
- Female dogs in heat cannot be sterilised and should wait around 2 months after heat ends.
- Cats must come in a rigid carrier, one cat per carrier.
- Dogs must come with leash or harness, and muzzle if needed.
- Dog pick-up is around 12:00.
- Cat pick-up is around 15:00.

Important:
If the user asks about fasting, water, or pre-operative instructions, answer strictly from this retrieved context.
Do not invent extra medical rules.
If retrieved context says water is allowed until 1 to 2 hours before surgery, keep that rule exactly.
"""

def retrieve_preop_context(user_msg: str) -> str:
    msg = user_msg.lower()

    keywords = [
        "ayuno", "agua", "preoperatorio", "operación", "operacion",
        "antes de la cirugía", "antes de la cirugia", "blood test",
        "analítica", "analitica", "instructions", "pre-op"
    ]

    if any(k in msg for k in keywords):
        return PREOP_TEXT

    return ""