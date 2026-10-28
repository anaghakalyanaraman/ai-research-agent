# AI Research Agent

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-green)
![LangGraph](https://img.shields.io/badge/LangGraph-ReAct-orange)
![LangSmith](https://img.shields.io/badge/LangSmith-Observability-purple)
![Tavily](https://img.shields.io/badge/Tavily-Web_Search-blue)

An autonomous AI research agent that searches the web in real-time, synthesizes findings, and returns a cited report grounded in actual sources — no hallucinated content.

**Demo:** [Watch Demo](https://youtu.be/ujEYGKfrP6M)  
**Live API:** https://ai-research-agent-jm6u.onrender.com/docs  
**Frontend:** https://ai-research-ui-six.vercel.app  
**GitHub (UI):** https://github.com/anaghakalyanaraman/ai-research-ui

---

## How It Works

1. User submits a topic
2. LangGraph ReAct Agent starts
3. **Loop:** LLM decides whether to search or answer
   - If search → Tavily API fetches real web results
   - LLM reads results and decides next action
   - Repeat until confident answer is ready
4. Final report with citations returned
5. LangSmith traces every step in production

---

## Key Engineering Decisions

**Why LangGraph ReAct instead of a simple chain?**  
A fixed chain always follows the same steps. ReAct lets the agent decide how many searches to run, what to search for next based on what it finds, and when it has enough information to answer. This produces better reports on complex topics.

**Why Tavily instead of Google Search API?**  
Tavily is purpose-built for LLM agents — it returns clean, structured content that fits in a context window rather than raw HTML. It also provides relevance scoring so the agent gets the most useful results.

**Why LangSmith?**  
Every agent run in production is traced — you can see exactly which tools were called, what the LLM was thinking at each step, token usage, and latency. This is what separates production AI systems from demos.

**Grounding over generation**  
The agent is instructed to only use facts from retrieved sources. This eliminates hallucinations — if Tavily doesn't return it, the agent doesn't say it.

---

## Tech Stack

| Component | Tool |
|---|---|
| Backend | Python, FastAPI |
| Agent Framework | LangGraph (ReAct) |
| LLM | Groq API |
| Web Search | Tavily API |
| Observability | LangSmith |
| Frontend | React, Vite, Tailwind CSS |
| Deployment | Render + Vercel |

---

## Running Locally

```bash
git clone https://github.com/anaghakalyanaraman/ai-research-agent
cd ai-research-agent
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt

# Create .env
GROQ_API_KEY=your_key
TAVILY_API_KEY=your_key
LANGCHAIN_API_KEY=your_key
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=ai-research-agent

uvicorn main:app --reload
```

API docs at `http://localhost:8000/docs`

---

## What I Would Do Next

**Streaming responses** — stream the agent's output token by token so users see progress in real-time instead of waiting 30 seconds.

**Multi-agent research** — spawn parallel subagents for different subtopics and synthesize their findings into one comprehensive report.

**Source quality scoring** — rank sources by domain authority and recency before passing to the LLM.

**Caching** — cache recent research results to avoid redundant API calls on similar topics.
