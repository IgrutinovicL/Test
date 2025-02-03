import json
from datetime import datetime

import openai
from config import Config

openai.api_key = Config.OPENAI_API_KEY

def get_weather_description(user_data, weather_data):
    """
    Placeholder method to get a weather description using OpenAI GPT API.
    """
    client = openai.OpenAI(api_key=openai.api_key)

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        store=True,
        messages=[{"role": "user", "content": "Write a weather forecast example"}]
    )
    print(completion.choices[0].message)
    return completion
