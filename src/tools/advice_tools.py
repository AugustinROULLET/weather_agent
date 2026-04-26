from agents import function_tool
from services.weather_services import WeatherService
from services.advice_services import AdviceService
from utils.formatter import ResponseFormatter

weather_service = WeatherService()
advice_service = AdviceService()
formatter = ResponseFormatter()


@function_tool
def get_clothing_advice(city: str) -> str:
    """Gives clothing advices based on weather and forcast"""

    forecast = weather_service.get_daily_forecast(city)

    if forecast["temp_min"] is None:
        return f"Can not gather forecast for {city}"
    
    morning_advice = advice_service.get_clothing_for_temp(forecast["morning_temp"])
    afternoon_advice = advice_service.get_clothing_for_temp(forecast["afternoon_temp"])
    evening_advice = advice_service.get_clothing_for_temp(forecast["evening_temp"])

    afternoon_temp = forecast["afternoon_temp"]
    bottom, shoes = advice_service.get_bottom_and_shoes(afternoon_temp)

    strategy = advice_service.get_strategy(
        forecast["temp_min"], 
        forecast["temp_max"],
        forecast["has_rain"]
    )
    
    special_advice = advice_service.get_special_advice(
        forecast["temp_min"],
        forecast["temp_max"],
        forecast["has_rain"],
        forecast["has_thunder"]
    )
    
    temps = {
        "min": forecast["temp_min"],
        "max": forecast["temp_max"],
        "actuelle": forecast["current_temp"],
        "morning": forecast["morning_temp"],
        "afternoon": forecast["afternoon_temp"],
        "evening": forecast["evening_temp"]
    }
    
    return formatter.format_clothing_advice(
        city=city,
        temps=temps,
        conditions=forecast["conditions"],
        morning_advice=morning_advice,
        afternoon_advice=afternoon_advice,
        evening_advice=evening_advice,
        bottom=bottom,
        shoes=shoes,
        strategy=strategy,
        special_advice=special_advice
    )