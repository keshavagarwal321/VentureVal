import os
from google.genai import types, Client
from google.adk.agents import LlmAgent
from google.adk.models.google_llm import Gemini
from src.tools.search_tool import search_tool  # Import the tool we just made

# Simple config loader since we know config.py exists
try:
    from config import API_KEY
except ImportError:
    # Fallback if config.py isn't found in path
    from dotenv import load_dotenv

    load_dotenv()
    API_KEY = os.getenv("GOOGLE_API_KEY")


def get_model():
    """Auto-selects the best available Gemini model."""
    try:
        if not API_KEY:
            return "gemini-1.5-flash"

        client = Client(api_key=API_KEY)
        available = [m.name for m in client.models.list(config={"page_size": 100})]

        # Priority: 2.5 Flash Lite -> 1.5 Flash
        priorities = ["models/gemini-2.5-flash-lite", "models/gemini-1.5-flash"]

        for p in priorities:
            clean_p = p.replace("models/", "")
            if any(clean_p in m for m in available):
                return clean_p
    except:
        pass
    return "gemini-1.5-flash"


def create_agents():
    model_name = get_model()
    # Retry policy for robustness
    retry = types.HttpRetryOptions(
        attempts=3, exp_base=2, initial_delay=1, http_status_codes=[429, 500]
    )

    scout = LlmAgent(
        name="Scout",
        model=Gemini(model=model_name, retry_options=retry),
        instruction="You are a Market Researcher. Use the tool to find competitors, pricing, and risks.",
        tools=[search_tool],
    )

    critic = LlmAgent(
        name="Critic",
        model=Gemini(model=model_name, retry_options=retry),
        instruction="You are a VC. Review the data. Create a Markdown SWOT Analysis. End with '## Venture Score: [0-100]'",
    )

    return scout, critic
