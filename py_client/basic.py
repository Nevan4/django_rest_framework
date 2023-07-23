import requests


endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/" #"http://127.0.0.1:8000/"

# get_response = requests.get(endpoint, json={"query": "Hello Dog"}) # HTTP Request
get_response = requests.post(endpoint, json={"title": "SOme title", "content": None,
                                             "price": 100}) # HTTP Request

# try:
#     data = get_response.json()
#     print(data)
# except:
#     print("Error from server: " + str(get_response.content))

# print("status code: " + str(get_response.status_code))

print(get_response.json())
