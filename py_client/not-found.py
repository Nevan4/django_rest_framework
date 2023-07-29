import requests


endpoint = "http://localhost:8000/api/products/12323232232323233/"


get_response = requests.get(endpoint) # HTTP Request


print(get_response.json())
