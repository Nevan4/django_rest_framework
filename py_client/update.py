import requests


endpoint = "http://localhost:8000/api/products/1/update/"

data = {
    "title": "Hello world - you have been updated",
    "price": 399.99
}

get_response = requests.put(endpoint, json=data) # HTTP Request


print(get_response.json())
