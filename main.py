import requests
from datetime import datetime


NUT_POST_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_POST_URL = "https://api.sheety.co/407a967edb3e231ee6c7f637d95bbfb6/myWorkouts/workouts"

# Nutritionix api
X_APP_ID = "d8e0ace9"
X_APP_KEY = "98500441f3841291bb93c41b7fc0205c"

headers = {
    "x-app-id": X_APP_ID,
    "x-app-key": X_APP_KEY
}

post_body = {
    "query": input("Tell me which execise you did: "),
    "gender": "male",
    "weight_kg": 85,
    "height_cm": 158,
    "age": 24
}

response = requests.post(url=NUT_POST_URL, headers=headers, json=post_body)
response.raise_for_status()
exercise_response = response.json()

# sheety api to record data in spreadsheet
today = datetime.now()
headers = {
    "Authorization": "Bearer asdfbearer1234myheartisstereoitbeatsforyousolistenclose988"
}

body = {
    "workout": {
        "date": today.strftime("%d/%m/%Y"),
        "time": today.strftime("%H:%M:%S"),
        "exercise": exercise_response["exercises"][0]["name"],
        "duration": exercise_response["exercises"][0]["duration_min"],
        "calories": exercise_response["exercises"][0]["nf_calories"]
    }
}

response = requests.post(url=SHEETY_POST_URL, json=body, headers=headers)
response.raise_for_status()

print(response.status_code)
print(response.text)
