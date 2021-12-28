import requests
from datetime import datetime
import os

# Nutritionix api
NUT_POST_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"
headers = {
    "x-app-id": os.environ["APP_ID"],
    "x-app-key": os.environ["API_KEY"]
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
token = os.environ["TOKEN"]
headers = {
    "Authorization": f"Bearer {token}"
}

body = {
    "workout": {
        "date": today.strftime("%d/%m/%Y"),
        "time": today.strftime("%H:%M:%S"),
        "exercise": exercise_response["exercises"][0]["name"].title(),
        "duration": exercise_response["exercises"][0]["duration_min"],
        "calories": exercise_response["exercises"][0]["nf_calories"]
    }
}

response = requests.post(url=os.environ["SHEET_ENDPOINT"], json=body, headers=headers)
response.raise_for_status()

print(response.status_code)
print(response.text)
