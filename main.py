import requests
from requests.api import head

URL = "https://trackapi.nutritionix.com/v2/natural/exercise"
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

response = requests.post(url=URL, headers=headers, json=post_body)
print(response.json())