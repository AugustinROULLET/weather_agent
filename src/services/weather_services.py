import requests
from typing import Dict, Optional, Tuple
from config import config

class WeatherService:
    """Service to gather weather and forecast"""

    def __init__(self):
        self.base_url = config.WHEATHER_API_URL
        self.timeout = 10

    def get_weather_data(self, city: str) -> Optional[Dict]:
        """Gather complete weather data for a city"""
        try:
            url = self.base_url.format(city = city)
            response = requests.get(url, timeout=self.timeout)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error for {city}: {e}")
            return None
        
    
    def get_current_weather(self, city: str) -> Tuple[Optional[int], Optional[str]]:
        """Gather current weather (temperature, conditions)"""
        data = self.get_weather_data(city)
        if not data:
            return None, None
        
        try:
            current = data["current_condition"][0]
            temp = int(current["temp_C"])
            conditions = current["weatherDesc"][0]["value"]
            return temp, conditions
        except (KeyError, IndexError, ValueError):
            return None, None
        
    def get_daily_forecast(self, city: str) -> Dict:
        """Gather complete forecast for the day"""
        default = {"temp_min": None, "temp_max": None, "has_rain": False, "has_thunder": False, "hourly": {}}

        data = self.get_weather_data(city)
        if not data:
            return default
        
        try:
            current = data["current_condition"][0]
            current_temp = int(current["temp_C"])

            forecast = data["weather"][0]
            temp_min = int(forecast.get("mintempC", current_temp))
            temp_max = int(forecast.get("maxtempC", current_temp))
            conditions = forecast.get("weatherDesc", [{}])[0].get("value", "")

            hourly = data.get("hourly", [])
            has_rain, has_thunder = self._check_precipitations(hourly)

            temps_by_hour = self._get_temps_by_hour(hourly, current_temp, temp_min, temp_max)

            return {
                "temp_min": temp_min,
                "temp_max": temp_max,
                "current_temp": current_temp,
                "conditions": conditions,
                "has_rain": has_rain,
                "has_thunder": has_thunder,
                "morning_temp": temps_by_hour["morning"],
                "afternoon_temp": temps_by_hour["afternoon"],
                "evening_temp": temps_by_hour["evening"],
            }
        except (KeyError, IndexError, ValueError) as e:
            print(f"Error: {e}")
            return default
        
    def _check_precipitaitons(self, hourly: list) -> Tuple[bool, bool]:
        """Check occurence of rain and storm"""
        has_rain = False
        has_thunder = False

        for hour in hourly[:12]:
            desc = hour.get("weatherDesc", [{}])[0].get("value", "").lower()
            if "rain" in desc or "drizzle" in desc:
                has_rain = True
            if "thunder" in desc:
                has_thunder = True
        return has_rain, has_thunder
    
    def _get_temps_by_hour(self, hourly: list, current_temp: int, min_temp: int, max_temp: int) -> Dict:
        """gather temperature at some time of the day"""
        morning_temp = current_temp
        afternoon_temp = max_temp
        evening_temp = min_temp

        for hour in hourly:
            hour_time = hour.get("time", "")
            if hour_time == "900":
                morning_temp = int(hour.get("tempC", morning_temp))
            if hour_time == "1500":
                afternoon_temp = int(hour.get("tempC", afternoon_temp))
            if hour_time == "2100":
                evening_temp = int(hour.get("tempC", evening_temp))
        return {"morning": morning_temp, "afternoon": afternoon_temp, "evening": evening_temp}

