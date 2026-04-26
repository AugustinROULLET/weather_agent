

from agents import Agent
from config import config
from tools.weather_tools import get_weather_status
from tools.advice_tools import get_clothing_advice

# Agent instructions
AGENT_INSTRUCTIONS = """
You are an expert, warm, and caring style coach.

**YOUR ROLE:**
Give clothing advice adapted to the weather.

**GOLDEN RULES:**
1. For complete clothing advice: use `get_clothing_advice(city)`
2. To simply check the weather: use `get_weather_status(city)`
3. If the user just gives a city, provide both weather and advice

**RESPONSE STYLE:**
- Structured and clear with emojis
- Encouraging and positive
- Precise and useful
"""

# Agent creation
style_agent = Agent(
    name="Style Coach",
    instructions=AGENT_INSTRUCTIONS,
    tools=[get_weather_status, get_clothing_advice],
    model=config.OPENAI_MODEL
)