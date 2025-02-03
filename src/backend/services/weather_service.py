import json

import requests
from config import Config

def fetch_weather_data(lat, long):
    """
    Placeholder method to fetch weather data from OpenWeather API.
    """
    try:
        # TODO: Implement weather API integration
        # Feel free to sub out with any other weather API you prefer

        # Use the free weather from weather.gov API
        # No api key required. Just pass a user agent (any values
        # https://www.weather.gov/documentation/services-web-api
        # headers = {'User-Agent': '(my.heypinnacle.com, contact@heypinnacle.com)'}

        # Fetch the forecast Url for weather.gov API  via lat/long
        # https://api.weather.gov/points/39.7456,-97.0892""
        forecastURL = requests.get(f"https://api.weather.gov/points/{lat},{long}").json()["properties"]["forecast"]

        # extract the forecast URL from the properties->forecast key of the response
        # example: https://api.weather.gov/gridpoints/TOP/31,80/forecast
        data = requests.get(forecastURL)


        # return the weather data for use in the app.
        return data.json()["properties"]
    except:
        return None