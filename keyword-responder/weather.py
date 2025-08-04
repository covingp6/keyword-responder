import requests

weather_codes = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Depositing rime fog",
    51: "Light drizzle",
    53: "Moderate drizzle",
    55: "Dense drizzle",
    56: "Light freezing drizzle",
    57: "Dense freezing drizzle",
    61: "Slight rain",
    63: "Moderate rain",
    65: "Heavy rain",
    66: "Light freezing rain",
    67: "Heavy freezing rain",
    71: "Slight snow fall",
    73: "Moderate snow fall",
    75: "Heavy snow fall",
    77: "Snow grains",
    80: "Slight rain showers",
    81: "Moderate rain showers",
    82: "Violent rain showers",
    85: "Slight snow showers",
    86: "Heavy snow showers",
    95: "Thunderstorm",
    96: "Thunderstorm with slight hail",
    99: "Thunderstorm with heavy hail"
}

def get_weather(location):
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={location}"
    geo_response = requests.get(geo_url)
    geo_data = geo_response.json()

    if not geo_data.get('results'):
        raise ValueError("Location not found. Please try again.")

    latitude = geo_data['results'][0]['latitude']
    longitude = geo_data['results'][0]['longitude']

    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
    weather_response = requests.get(weather_url)
    weather_data = weather_response.json()

    temp_c = round((weather_data["current_weather"]["temperature"]), 1)
    temp_f = round((weather_data["current_weather"]["temperature"] * 9/5 + 32), 1)
    wind = weather_data["current_weather"]["windspeed"]
    code = weather_data["current_weather"]["weathercode"]
    condition = weather_codes.get(code, "Unknown weather condition")

    return f"The weather in {location.title()} is {condition.lower()} with a temperature of {temp_c}°C ({temp_f}°F) and wind speed of {wind} km/h."