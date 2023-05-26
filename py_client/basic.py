import requests


endpoint = "https://httpbin.org/anything"

get_response = requests.get(endpoint) # API -> Method

try:
    data = get_response.json()
    print(data)
except:
    print("Error from server: " + str(get_response.content))

