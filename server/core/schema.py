from pydantic import BaseModel, Field, validator
from typing import List, Literal
from datetime import datetime

class Citation(BaseModel):
    doc_id: str
    chunk_id: str
    snippet: str

class HitlInteraction(BaseModel):
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    type: Literal["clarification", "approval", "upload_request"]
    prompt: str
    response: str | None = None
    status: Literal["approved", "denied", "provided", "timeout"]

class Decision(BaseModel):
    decision: Literal["compliant", "non_compliant", "insufficient_evidence"]
    confidence: float = Field(ge=0.0, le=1.0)
    risk_score: float = Field(ge=0.0, le=1.0)
    rationale: str
    citations: List[Citation]
    open_questions: List[str]
    human_interactions: List[HitlInteraction]

    @validator("citations", "open_questions", "human_interactions")
    def non_empty(cls, v):        # guardrail: never empty arrays
        if not v:
            raise ValueError("must not be empty")
        return v
