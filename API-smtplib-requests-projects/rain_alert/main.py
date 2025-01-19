import requests
from twilio.rest import Client
# API from Openweathermap.org
weather_api_key = "API Key"
MY_LAT = "my latitude"
MY_LONG = "my longitude"
# Get those by registering for free in Twilio.com
account_sid = "account_sid"
auth_token = "auth_token"
twilio_number = "twilio_number"

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": weather_api_key,
    "units": "metric",
    "cnt": 4
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()
for current_weather in weather_data['list']:
    weather_id = current_weather['weather'][0]['id']
    if weather_id < 700:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body="Hello, if you received this message, this means that it will rain in the next 12 hours.",
            from_=twilio_number,
            to="Receiver",
        )
        break

