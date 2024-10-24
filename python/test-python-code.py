import pyowm
from pyowm.utils.config import get_default_config

# Initialize the OpenWeatherMap API
owm = pyowm.OWM('you_api_key')  # Replace with your OpenWeatherMap API key
mgr = owm.weather_manager()

# Specify the location (e.g., New York, US)
location = "Multan, Pakistan"

observation = mgr.weather_at_place(location)
weather = observation.weather

# Get weather details
print(f"Location: {location}")
print(f"Status: {weather.detailed_status}")
print(f"Temperature: {weather.temperature('celsius')['temp']}°C")
print(f"Humidity: {weather.humidity}%")
print(f"Wind Speed: {weather.wind()['speed']} m/s")

# Get a 5-day forecast
forecast = mgr.forecast_at_place(location, '3h').forecast
for weather in forecast:
    print(f"Time: {weather.reference_time('iso')}, Status: {weather.detailed_status}")
    print(f"Temperature: {weather.temperature('celsius')['temp']}°C")
    print("-"*40)
