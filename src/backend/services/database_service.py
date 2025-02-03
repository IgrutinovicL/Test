from datetime import datetime

from pymongo import MongoClient
from config import Config

client = MongoClient(Config.MONGO_URI)
db_collection = client['weather-app'].get_collection('weather-forecasts')


def fetch_user_mock_data(user_id):
    """
    Placeholder method to fetch user data from MongoDB.
    """

    mock_data = {
        "X1": {"user_id": "X1",
         "name": "John Doe",
         "location": {
             "city": "New York",
             "state": "NY",
             "lat": 40.776676,
             "long": -73.971321
         }
         },
        "X2": {"user_id": "X2",
         "name": "Jane Doe",
         "location": {
             "city": "San Francisco",
                "state": "CA",
             "lat": 37.809326,
             "long": -122.409981
         }
         }
    }

    return mock_data.get(user_id)

def save_weather_description(user_data, weather_data, description):
    """
    Placeholder method to save the weather description to MongoDB.
    """
    # TODO: Save the weather data from api and the generated description to MongoDB
    pass
