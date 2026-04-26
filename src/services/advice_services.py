from typing import Dict, Tuple
from config import config

class AdviceService:
    """Generate clothing advice based on weather"""

    def __init__(self): 
        self.temp_ranges = config.TEMP_RANGES

    def get_clothing_for_temp(self, temp: int) -> Dict:
        """Return clothes for a specific temperature"""
        if temp < self.temp_ranges["extreme_cold"]:
            return {
                "top": "Thick coat + sweater + thermal t-shirt",
                "accessories": "Hat, scarf, gloves (essential!)"
            }
        elif temp < self.temp_ranges["cold"]:
            return {
                "top": "Warm coat or puffer jacket + turtleneck sweater",
                "accessories": "Scarf and hat recommended"
            }
        elif temp < self.temp_ranges["cool"]:
            return {
                "top": "Light jacket or blazer + thin sweater or shirt",
                "accessories": "A light scarf can be useful"
            }
        elif temp < self.temp_ranges["warm"]:
            return {
                "top": "T-shirt, light shirt, or very thin sweater",
                "accessories": "Sunglasses, cap optional"
            }
        else:
            return {
                "top": "Breathable t-shirt, tank top, or linen shirt",
                "accessories": "Cap, sunglasses"
            }
        
    def get_bottom_and_shoes(self, temp: int) -> Tuple[str, str]:
        """Returns recommendations for bottoms and shoes"""
        if temp > 25:
            return "Shorts or light skirt", "Sandals or flip-flops"
        elif temp > 20:
            return "Light pants", "Light sneakers or espadrilles"
        elif temp < 10:
            return "Warm pants", "Boots"
        else:
            return "Jeans or classic pants", "Sneakers or closed-toe shoes"
        
    def get_strategy(self, temp_min: int, temp_max: int, has_rain: bool) -> str:
        """Determines the clothing strategy for the day"""
        if has_rain:
            return "☔ **Rain risk**: Plan for a raincoat or umbrella."
        elif temp_min < 15 and temp_max > 20:
            return "🔄 **Layering strategy**: Day that warms up. Prioritize removable layers."
        elif temp_min < 10 and temp_max < 15:
            return "🧥 **Cool day**: Stay well covered all day."
        elif temp_min > 20:
            return "☀️ **Hot day**: Light clothing all day."
        return ""
    

    def get_special_advice(self, temp_min: int, temp_max: int, has_rain: bool, has_thunder: bool) -> str:
        """Gives special advice based on conditions"""
        if temp_max - temp_min > 10:
            return f"🌡️ **Large temperature range**: {temp_min}°C → {temp_max}°C. Layering is essential!"
        elif has_thunder:
            return "⛈️ **Possible thunderstorms**: Stay alert and plan a backup."
        elif has_rain:
            return "☔ **Rain forecast**: Don't forget your umbrella or raincoat!"
        elif temp_max > 30:
            return "🔥 **Heatwave**: Stay hydrated and avoid sun between 12pm-4pm."
        elif temp_min < 0:
            return "❄️ **Freezing day**: Bundle up well, risk of frost."
        else:
            return f"💡 **Overview**: Temperature between {temp_min}°C and {temp_max}°C today."