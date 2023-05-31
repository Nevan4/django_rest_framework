import json
from django.http import JsonResponse


def api_home(request, *args, **kwargs):
    #  request is from -> HttpRequest -> Django
    print(request.GET)
    body = request.body  # gives string of JSON data
    data = {}
    try:
        data = json.loads(body) #to convert the JSON string into python dict
    except:
        pass
    print(data)  # see in console on server side
    # print(data.keys())  # to see only keys from json
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    # data['content_type'] = request.content_type
    return JsonResponse(data)


    # return JsonResponse({"message": "Hello there, Django API response here!"})
