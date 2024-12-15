import requests
import yaml
def get_address_and_weather(city="Hanoi"):
    with open("config.yml", "r") as ymlfile:
        cfg = yaml.safe_load(ymlfile)
        api_key = cfg["weather"]["api_key"] 
    try:
        # Fetch weather data from OpenWeatherMap API
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        # Extract weather description and temperature
        weather_description = data['weather'][0]['main'].lower()
        temp_celsius = data['main']['temp']
        
        # Map weather conditions to emojis
        weather_emojis = {
            "clear": "☀️",
            "clouds": "☁️",
            "rain": "🌧️",
            "snow": "❄️",
            "thunderstorm": "⛈️",
            "drizzle": "🌦️",
            "mist": "🌫️",
            "fog": "🌫️",
            "haze": "🌫️",
        }
        emoji = weather_emojis.get(weather_description, "🌡️")  # Default to thermometer
        
        # Format temperature with emoji
        temp = f"{emoji}{temp_celsius}°C"
        return city, temp
    except Exception as e:
        return "Error", str(e)



