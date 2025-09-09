from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import ChatInput, ChatOutput, MessageAnalysis
from utils import preprocess_chat, analyze_message

app = FastAPI(title="Influence Detector API")

# Allow all origins for demo; restrict in production
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze", response_model=ChatOutput)
def analyze_chat(input: ChatInput):
    messages = preprocess_chat(input.chat)
    analyzed = []
    manipulative_count = 0
    for msg in messages:
        result = analyze_message(msg)
        # Demo: If label is not neutral, count as manipulative
        if result["label"] != "neutral":
            manipulative_count += 1
        analyzed.append(MessageAnalysis(
            speaker=msg["speaker"],
            text=msg["text"],
            label=result["label"],
            confidence=result["confidence"],
            explanation=result["explanation"]
        ))
    influence_score = round(manipulative_count / len(messages), 2) if messages else 0.0
    return ChatOutput(messages=analyzed, influence_score=influence_score)

# TODO: Integrate HuggingFace models for emotion, intent, and manipulation tactic classification
# TODO: Add causal reasoning for stance change detection
