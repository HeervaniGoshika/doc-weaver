from pydantic import BaseModel, Field
from typing import List

class AgentRequest(BaseModel):
    request: str

class AgentResponse(BaseModel):
    status: str
    goal: str
    assumptions: List[str]
    plan: List[str]
    document: str
    message: str