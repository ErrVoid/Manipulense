from pydantic import BaseModel, Field
from typing import List, Optional

class MessageAnalysis(BaseModel):
    speaker: str
    text: str
    label: str
    confidence: float
    explanation: str

class ChatInput(BaseModel):
    chat: str = Field(..., example="A: Why don’t you help me, after all I helped you last time?\nB: Okay fine, I’ll do it.")

class ChatOutput(BaseModel):
    messages: List[MessageAnalysis]
    influence_score: float
