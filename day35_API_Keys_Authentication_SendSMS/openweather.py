# Pull API requests from openweathermap.org and send SMS messages if it's going to rain

import requests
from twilio.rest import Client

twilio_account_sid = os.environ["account_sid"]
twilio_auth_token = os.environ["Auth_Token"]

OWM_Endpoint = "https://api.openweathermap.org/data/3.0/onecall"
api_key = "47e9da846fdfb65bc19d1386305a8230"

# Los Angeles parameters
weather_parameters = {
    "lat": 34.052235,
    "lon": -118.243683,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_parameters)
response.raise_for_status()  # will tell us https status code if error
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]  # slice items from the beginning (0 hour) through stop (11th hour)

will_rain = False

for hour_data in weather_slice:
    weather_condition_code = hour_data["weather"][0]["id"]
    if int(weather_condition_code) < 700:  # weather code under 700 means raining
        will_rain = True

if will_rain:
    client = Client(twilio_account_sid, twilio_auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today! Bring an umbrella!☔️",
        from_="from number",
        to="to number"
    )
    print(message.sid)
