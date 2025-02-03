 # Pinnacle Take home test
 
## Backend Engineer
### Problem Statement
Implement the REST API endpoint under src/backend/app.py to provide a custom weather forecast for a user.
Save the user's forecast to a mongodb collection and return the forecast to the user.
To achieve this:

- Retrieve the user's `userId` from the request payload
- Use the provided `fetch_user_mock_data` function to retrieve the user's data
- Use the location data from the user's data to retrieve the weather forecast from the `fetch_weather_forecast` function
- Use an LLM to create a custom forecast for the user based on their profile
- Save the forecast to a mongodb collection by the user_id
- Return the forecast to the calling user

Include unit tests as necessary.


## Installation

1. Clone the repository.
2. Install dependencies:
```bash
   pip install -r requirements.txt
```

## Project Structure
```
weather_api_project/
├── app.py
├── config.py
├── services/
│   ├── weather_service.py
│   ├── openai_service.py
│   ├── database_service.py
├── requirements.txt
└── README.md
```

config.py expects the following environment variables:

- OPENAI_API_KEY: Your OpenAI API key (but you are free to use any LLM)
- MONGODB_URI: Your MongoDB URI (defaults to localhost)