import requests
api_key = ""
api_url = f"https://api.weatherstack.com/current?access_key={api_key}&query=New York"

def fetch_data():
    print("Fetching weather data from Weatherstack API...")
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        print("API response received successfully")
        # print(response.json())
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occured: {e}")
        raise


# fetch_data()

def mock_fetch_data():
    return {'request': {'type': 'City', 'query': 'New York, United States of America', 'language': 'en', 'unit': 'm'}, 'location': {'name': 'New York', 'country': 'United States of America', 'region': 'New York','lat': '40.714', 'lon': '-74.006', 'timezone_id': 'America/New_York', 'localtime': '2026-02-04 13:06', 'localtime_epoch': 1770210360, 'utc_offset': '-5.0'}, 'current': {'observation_time': '06:06 PM', 'temperature': -1, 'weather_code': 113, 'weather_icons': ['https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0001_sunny.png'], 'weather_descriptions': ['Sunny'], 'astro': {'sunrise': '07:03 AM', 'sunset': '05:18 PM', 'moonrise': '08:36 PM', 'moonset': '08:27 AM', 'moon_phase': 'Waning Gibbous', 'moon_illumination': 95}, 'air_quality': {'co': '420.85', 'no2': '60.65', 'o3': '16', 'so2': '8.55', 'pm2_5': '27.85', 'pm10': '28.15', 'us-epa-index': '2', 'gb-defra-index': '2'}, 'wind_speed': 15, 'wind_degree': 342, 'wind_dir': 'NNW', 'pressure': 1023, 'precip': 0, 'humidity': 37, 'cloudcover': 0, 'feelslike': -6, 'uv_index': 2, 'visibility': 16, 'is_day': 'yes'}}