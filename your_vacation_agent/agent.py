from google.adk.agents.llm_agent import Agent
from dotenv import load_dotenv
from google.genai import types
from google.adk.agents import LlmAgent
from google.adk.tools import FunctionTool
from google.adk.models.lite_llm import LiteLlm

from .prompts import SYSTEM
from .tools import get_weather, get_current_time, convert_currency, get_travel_advisory


root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge',
)

from .tools import get_weather, get_current_time, convert_currency, get_travel_advisory


load_dotenv()

root_agent = LlmAgent(
    name="your_vacation_agent",
    instruction=SYSTEM,
    model=LiteLlm("gemini/gemini-2.5-flash-lite"),
    tools=[
        FunctionTool(get_weather),
        FunctionTool(get_current_time),
        FunctionTool(convert_currency),
        FunctionTool(get_travel_advisory),
    ],
    generate_content_config=types.GenerateContentConfig(
        temperature=0.1,
    ),
)