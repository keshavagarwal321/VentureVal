from google.adk.tools.function_tool import FunctionTool
from duckduckgo_search import DDGS


def market_search(query: str) -> str:
    """
    Searches the web for real-time market data using DuckDuckGo.
    Args:
        query: The search string (e.g., "competitors for AI plant app")
    Returns:
        A formatted string of titles and snippets.
    """
    print(f"  🔎 [Tool] Searching for: {query}...")
    try:
        results = DDGS().text(query, max_results=4)
        if not results:
            return "No specific data found. Proceed with general knowledge."
        return "\n".join([f"- {r['title']}: {r['body']}" for r in results])
    except Exception as e:
        return f"Search Error: {e}"


# Export the tool object for the agents to use
search_tool = FunctionTool(func=market_search)
