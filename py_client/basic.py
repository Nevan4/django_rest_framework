import requests


endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/" #"http://127.0.0.1:8000/"

get_response = requests.get(endpoint, data={"query": "Hello Dog"}) # API -> Method

try:
    data = get_response.json()
    print(data)
except:
    print("Error from server: " + str(get_response.content))

print(get_response.status_code)

