memory = {}

def get_history(session_id):
    return memory.get(session_id, [])

def save_history(session_id, user_msg, bot_msg):
    if session_id not in memory:
        memory[session_id] = []
    memory[session_id].append((user_msg, bot_msg))