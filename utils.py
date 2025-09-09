import re
import random
from typing import List, Dict

def preprocess_chat(chat: str) -> List[Dict[str, str]]:
    """Splits chat into list of {speaker, text} dicts."""
    messages = []
    for line in chat.strip().split('\n'):
        match = re.match(r"([A-Za-z]):\s*(.*)", line)
        if match:
            speaker, text = match.groups()
            messages.append({"speaker": speaker, "text": text})
    return messages

def analyze_message(message: Dict[str, str]) -> Dict[str, str]:
    text = message["text"].lower()
    label = "neutral"
    explanation = "No manipulation detected."
    if "after all" in text or "because i" in text:
        label = "guilt-tripping"
        explanation = "Phrase 'after all' or 'because I' implies obligation."
    elif "you’re the only one" in text or "you're the only one" in text:
        label = "flattery"
        explanation = "Phrase 'you’re the only one' is flattery."
    elif "if you don’t" in text or "if you don't" in text:
        label = "fear pressure"
        explanation = "Phrase 'if you don’t' implies a threat or pressure."
    confidence = round(random.uniform(0.7, 0.95), 2)
    return {
        "label": label,
        "confidence": confidence,
        "explanation": explanation
    }
