from fastapi import APIRouter, HTTPException
from src.api.models import QueryRequest, QueryResponse
from src.rag.ai_service import get_agent_response

router = APIRouter()

@router.post("/chat", response_model=QueryResponse)
async def chat(request: QueryRequest):
    try:
        response = get_agent_response(request.query)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
