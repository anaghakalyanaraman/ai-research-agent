from langchain_groq import ChatGroq
from langchain_tavily import TavilySearch
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGroq(model="openai/gpt-oss-20b", api_key=os.getenv("GROQ_API_KEY"))
search_tool = TavilySearch(max_results=1)
agent = create_react_agent(llm, [search_tool])

def run_research(topic: str) -> dict:
    result = agent.invoke(
        {
            "messages": [
                ("system", "Search the web and write a cited report. Only use facts from search results."),
                ("human", f"Research: {topic}")
            ]
        },
        config={"recursion_limit": 10}
    )
    
    final_message = result["messages"][-1].content
    
    return {
        "topic": topic,
        "report": final_message,
        "message_count": len(result["messages"])
    }
