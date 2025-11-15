def get_weather_emoji(weather_code: int) -> str:
    """Get emoji based on weather code"""
    if weather_code in [61, 63, 65, 80, 81, 82]:
        return "🌧️"
    elif weather_code in [71, 73, 75, 77, 85, 86]:
        return "❄️"
    elif weather_code in [95, 96, 99]:
        return "⛈️"
    elif weather_code in [45, 48]:
        return "🌫️"
    elif weather_code == 0:
        return "☀️"
    elif weather_code in [1, 2]:
        return "🌤️"
    else:
        return "☁️"
