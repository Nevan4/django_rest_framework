import json
from django.forms.models import model_to_dict
# from django.http import JsonResponse

from rest_framework.response import Response

from rest_framework.decorators import api_view
from products.models import Product

@api_view(["GET"])
def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data = model_to_dict(model_data)
        # data = model_to_dict(model_data, fields=['id', 'title'])
    return Response(data)













#v2

# def api_home(request, *args, **kwargs):
#     model_data = Product.objects.all().order_by("?").first()
#     data = {}
#     if model_data:
#         data = model_to_dict(model_data)
#         # data = model_to_dict(model_data, fields=['id', 'title'])
#     return JsonResponse(data)




#v1
# def api_home(request, *args, **kwargs):
#     model_data = Product.objects.all().order_by("?").first()
#     data = {}
#     if model_data:
#         data['title'] = model_data.title
#         data['content'] = model_data.content
#         data['price'] = model_data.price
#     return JsonResponse(data)


    # return JsonResponse({"message": "Hello there, Django API response here!"})
