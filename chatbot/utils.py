# # Add any helper functions you want to reuse. For now, empty or small utilities.
# def summarize_text(text, max_len=600):
#     return text[:max_len] + ("..." if len(text) > max_len else "")
# chatbot/utils.py

import os
import json
from datetime import datetime

def summarize_text(text, max_len=600):
    """Return a shortened version of text."""
    return text[:max_len] + ("..." if len(text) > max_len else "")

def save_chat_log(log: list[dict], filepath="chat_logs.json"):
    """
    Save chat history to a JSON file.
    log: list of dicts, e.g., [{"role": "user", "content": "..."}]
    """
    # Ensure the folder exists
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    
    # Add timestamp
    timestamp = datetime.now().isoformat()
    entry = {"timestamp": timestamp, "messages": log}

    # Load existing logs if any
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = []

    data.append(entry)

    # Save back to file
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
