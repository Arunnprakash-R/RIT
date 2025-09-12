from fastapi import APIRouter, HTTPException, Body
from pydantic import BaseModel, Field
from typing import Dict, Any

# Create an API router
router = APIRouter()

# --- Data Models ---
class CallIngestionRequest(BaseModel):
    session_id: str = Field(..., description="Unique identifier for the call session.")
    transcript: str = Field(..., description="The transcribed text from the user.")

class Escalation(BaseModel):
    session_id: str
    reason: str
    transcript: str

# --- API Endpoints ---

@router.post("/ingest", summary="Ingest call data (text)", tags=["Call Handling"])
async def ingest_call(request: CallIngestionRequest):
    """
    Receives transcribed text from a call, processes it through the LLM agent,
    and returns the agent's response.

    This endpoint will eventually:
    1. Receive text from a voice-to-text service.
    2. Use the session_id to maintain conversation state.
    3. Invoke the LangGraph agent to get the next response.
    4. Log the interaction on the mock blockchain.
    """
    # Placeholder for LangGraph agent invocation
    # agent_response = await llm_agent.invoke(request.transcript)

    # Mock response
    agent_response = f"Received transcript for session {request.session_id}: '{request.transcript[:50]}...'"

    # Check for escalation keywords
    if "speak to a human" in request.transcript.lower():
        # In a real system, this would trigger an escalation workflow
        return {"response": "I understand you'd like to speak to a human. I am escalating your request now.", "escalated": True}

    return {"response": agent_response, "escalated": False}

@router.post("/escalate", summary="Manually escalate a call", tags=["Escalations"])
async def escalate_call(escalation: Escalation):
    """
    An endpoint to handle escalations, for example, from a supervisor dashboard.
    This would dispatch a notification (e.g., email) and log the event.
    """
    # Placeholder for dispatching an email or other notification
    # await email_dispatcher.send_escalation_email(escalation)
    print(f"Escalation for session {escalation.session_id} received. Reason: {escalation.reason}")
    return {"message": "Escalation has been processed."}

@router.get("/metrics", summary="Get performance metrics", tags=["Analytics"])
async def get_metrics() -> Dict[str, Any]:
    """
    Returns key performance indicators for the call center.

    In a real system, this data would be aggregated from MongoDB.
    """
    # Mock data
    mock_metrics = {
        "total_calls": 1250,
        "successful_self_service": 980,
        "escalation_rate": 0.216,
        "average_call_duration_seconds": 180,
        "customer_satisfaction_score": 4.5
    }
    return mock_metrics
