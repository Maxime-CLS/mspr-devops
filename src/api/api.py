from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.llm.ollama_client import OllamaClient
from opentelemetry import trace
import os

app = FastAPI()
tracer = trace.get_tracer(__name__)

ollama = OllamaClient(
    model=os.getenv("OLLAMA_MODEL", "llama2"),
    base_url=os.getenv("OLLAMA_BASE_URL", "http://ollama:11434")
)

class AnalysisRequest(BaseModel):
    prompt: str
    user_id: str

@app.post("/analyze")
async def analyze(request: AnalysisRequest):
    with tracer.start_as_current_span("api_analyze"):
        try:
            response = ollama.generate(request.prompt, request.user_id)
            return {"response": response, "user_id": request.user_id}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    return {"status": "healthy"}