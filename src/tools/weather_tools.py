from agents import function_tool
from services.weather_services import WeatherService
from utils.formatter import ResponseFormatter

weatherService = WeatherService()
formatter = ResponseFormatter


@function_tool
def get_weather_status(city: str) -> str:
    """Return current weather for a given city"""
    temp, conditions = weatherService.get_current_weather(city)

    if temp is None:
        return f"No weather found for {city}"
    
    return formatter.format_weather_response(city, temp, conditions)