import requests


endpoint = "http://localhost:8000/api/products/"

data = {
    "title": "This field is done",
    "price": 240
}

get_response = requests.post(endpoint, json=data) # HTTP Request

print(get_response.json())