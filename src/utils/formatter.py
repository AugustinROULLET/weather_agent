from typing import Dict

class ResponseFormatter:
    @staticmethod
    def format_weather_response(city: str, temp: int, conditions: str) -> str:
        """Formats the simple weather response"""
        return f"""🌍 **Weather in {city.upper()}** 🌍
━━━━━━━━━━━━━━━━━━━━━━━

🌡️ Temperature: {temp}°C
☁️ Conditions: {conditions}"""
    
    @staticmethod
    def format_clothing_advice(
        city: str,
        temps: Dict,
        conditions: str,
        morning_advice: Dict,
        afternoon_advice: Dict,
        evening_advice: Dict,
        bottom: str,
        shoes: str,
        strategy: str,
        special_advice: str
    ) -> str:
        """Formats the complete clothing advice"""
        
        return f"""
🌍 **FORECAST - {city.upper()}** 🌍
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 **DAY OVERVIEW**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🌡️ {temps['min']}°C → {temps['max']}°C (current: {temps['actuelle']}°C)
☁️ {conditions}
📈 Range: {temps['max'] - temps['min']}°C

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⏰ **BY TIME OF DAY**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🌅 **Morning ({temps['morning']}°C)**
   👕 {morning_advice['haut']}
   🧣 {morning_advice['accessoires']}

☀️ **Afternoon ({temps['afternoon']}°C)**
   👕 {afternoon_advice['haut']}
   🧣 {afternoon_advice['accessoires']}

🌙 **Evening ({temps['evening']}°C)**
   👕 {evening_advice['haut']}
   🧣 {evening_advice['accessoires']}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
👖 **DAILY BASICS**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
👖 {bottom}
👟 {shoes}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💡 **TIPS**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{strategy if strategy else special_advice}
"""