from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import ToolNode

def get_tools():
    """
    Return the list of tools to be used in the chatbot
    """
    tools=[TavilySearchResults(max_results=2)]
    return tools

def create_tool_node(tools):
    """
    creates and returns a tool node for the graph
    """
    return ToolNode(tools=tools)

# 📝 Explanation:
# •	✅ get_tools() — returns a list of tools (we're using Tavily now, but you can add Wiki, Arxiv, etc.)
# •	⚒️ create_tool_node() — converts tool into a Tool Node to be used in the LangGraph


