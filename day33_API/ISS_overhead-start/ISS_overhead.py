import requests
from datetime import datetime
import smtplib
import time


MY_LAT = 34.052235
MY_LONG = -118.243683
MY_EMAIL = "test@gmail.com"
PASSWORD = "password"


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()     # will tell us https status code if error
    data = response.json()          # Get data from API endpoint

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Compare if your position is within +5 or -5 degrees of the ISS position
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True


def is_night():
    # parameters to get specific data using dict
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    # Sunrise and sunset API
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])   # split to get specific time (hours)
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])     # split to get specific time (hours)

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()   # (TLS) - secures connection w/ email server
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Subject:Look Up!\n\nThe ISS is above you in thr sky "
        )

# -----------------------NOTES----------------------------

#TODO: Sunrise time broken down using .split() method
# print(sunrise)                                  # 2022-09-23T13:40:45+00:00
# print(sunrise.split("T"))                       # ['2022-09-23', '13:40:45+00:00']
# print(sunrise.split("T")[1])                    # 13:40:45+00:00
# print(sunrise.split("T")[1].split(":"))         # ['13', '40', '45+00', '00']
# print(sunrise.split("T")[1].split(":")[0])      # 13

