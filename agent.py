from langchain_groq import ChatGroq
from langchain_tavily import TavilySearch
from langgraph.prebuilt import create_react_agent
from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

# LLM
llm = ChatGroq(model="openai/gpt-oss-120b", api_key=os.getenv("GROQ_API_KEY"))

# Tools
search_tool = TavilySearch(max_results=2)
# Agent
agent = create_react_agent(llm, [search_tool])

def run_research(topic: str) -> dict:
    result = agent.invoke({
        "messages": [
            ("system", "You are a research agent. Search for information, then write a clear report with citations. Only use facts from search results."),
            ("human", f"Research this topic thoroughly and provide a comprehensive report with citations: {topic}")
        ]
    })
    
    # Extract final answer
    final_message = result["messages"][-1].content
    
    return {
        "topic": topic,
        "report": final_message,
        "message_count": len(result["messages"])
    }