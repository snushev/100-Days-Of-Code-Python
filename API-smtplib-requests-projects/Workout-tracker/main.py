import requests
import datetime

current_date = datetime.datetime.now().date().strftime('%d/%m/%Y')
current_time = datetime.datetime.now().time().strftime("%X")

GENDER = "gender"
WEIGHT_KG = "weight"
HEIGHT_CM = "height"
AGE = "age"

APP_ID = "App ID"
API_KEY = 'API key'

nutritionx_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
sheety_endpoint = 'https://api.sheety.co/User_id/Project_name/sheet_name' # <- change user, project and sheet.

headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY
}

text_query = input('Tell me your exercise and duration: ')

nutritionx_params = {
    "query": text_query,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(nutritionx_endpoint, json=nutritionx_params, headers=headers)
exercise_data = response.json()

sheety_headers = {
    "Authorization": "username password"
}
for exercise in exercise_data["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": current_date,
            "time": current_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(url=sheety_endpoint, json=sheet_inputs, headers=sheety_headers)
    print(sheet_response.text)