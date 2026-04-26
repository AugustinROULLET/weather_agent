import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Global configuration"""

    OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

    WHEATHER_API_URL = "https://wttr.in/{city}?format=j1"
    WEATHER_TIMEOUT = 10

    TEMP_RANGES = {
        "extreme_cold": 0,
        "cold": 10,
        "cool": 18,
        "warm": 25,
    }

    EXIT_COMMANDS = ['quit', 'exit', 'au revoir', 'bye', 'stop']
    
    WEATHER_EMOJIS = {
        "sunny": "☀️",
        "cloudy": "☁️",
        "rain": "🌧️",
        "snow": "❄️",
        "thunder": "⛈️",
        "default": "🌤️"
    }

config = Config()