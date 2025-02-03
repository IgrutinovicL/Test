from flask import Flask, request, jsonify
from services.weather_service import fetch_weather_data
from services.openai_service import get_weather_description
from services.database_service import save_weather_description, fetch_user_mock_data
from pprint import pprint

app = Flask(__name__)


@app.route('/weather', methods=['POST'])
def get_weather():
    """
    Fetch weather data, generate a description using ChatGPT, and save to MongoDB.
    """
    try:
        data = request.json

        # extract the user_id from the request
        if "userId" not in data:
            return jsonify({
                "issue":"'userId' is mandatory"
            }),400
        user_id = data['userId']

        # fetch the user_data from the database
        user_data = fetch_user_mock_data(user_id)

        # If the user cannot be found, return a 404
        if not user_data:
            return jsonify({
                "issue":"User under the provided 'userId' does not exist."
            }),404

        # If user does not have location data which is necessairy
        if "location" not in user_data or "lat" not in user_data["location"] or "long" not in user_data["location"]:
            return jsonify({
                "issue":"User does not have location data."
            }),400

        #Fetch weather data
        weather_data = fetch_weather_data(user_data["location"]["lat"],user_data["location"]["long"])
        pprint(weather_data)
        if "periods" not in weather_data or weather_data == None:
            return jsonify({
                "issue":"Weather data does not exist for user's lat,long."
            }),404

        # Placeholder: Generate description from OpenAI API
        description = get_weather_description(None,None)
        print(description)

        # Placeholder: Save to MongoDB
        # save_weather_description

        # Return the fetched weather data and generated description
        return jsonify({
            "description": description
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)