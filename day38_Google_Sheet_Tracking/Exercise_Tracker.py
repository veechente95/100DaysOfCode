import requests
from datetime import datetime

GENDER = "male"
WEIGHT_KG = 88.5
HEIGHT_CM = 182
AGE = 26

NUTRITIONIX_APP_ID = "7079d448"
NUTRITIONIX_API_KEY = "19d138ed3abd7db26578daa770a75c2f"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/60c07e0c70f28470eed68124215e1ba1/workoutTracking/sheet1"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
result = response.json()

# POST command to add data to sheety
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }


sheet_response = requests.post(url=sheety_endpoint, json=sheet_inputs)
print(result)