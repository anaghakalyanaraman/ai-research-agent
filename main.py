from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from agent import run_research
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
    "http://localhost:5173",
    "http://localhost:5174",
    "https://ai-research-ui-six.vercel.app"
],
)

class ResearchRequest(BaseModel):
    topic: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/research")
def research(request: ResearchRequest):
    result = run_research(request.topic)
    return result
