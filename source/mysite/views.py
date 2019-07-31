import json
import datetime
import requests

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.views.decorators.http import require_http_methods

from .models import Routine
from .helper import Sum
from .pushups import Test

# Global Variables
homePath = "http://127.0.0.1:8000/"

# Create your views here.
def Index(request):

    paths = {
        "a) [GET]": "http://127.0.0.1:8000/",
        "b) [GET]": "http://127.0.0.1:8000/pushups"
    }

    return JsonResponse(paths)

# /pushups
@require_http_methods(["GET"])
def GetRoutineData(request):
    everything = Routine.objects.all()
    print(everything[0])
    return JsonResponse({ "": "" })



# Example of saving values from POST request to DB
@require_http_methods(["GET", "POST"])
def ShoppingList(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        item = body['item']
        cost = body['cost']

        shoppingItem = ShoppingList(item="item", cost="cost")
        shoppingItem.save()

        response = { "Home": homePath, "Data": shoppingItem.json() }
    elif request.method == 'GET':
        response = { "Home": homePath, "Data": shoppingItem.json() }

    return JsonResponse(response)

# Example of making a request to a 3rd party API
def Joke(request):
    URL = "https://icanhazdadjoke.com/"
    HEADERS = { "content-type": "application/json", "accept": "application/json" }

    r = requests.get( url = URL, headers = HEADERS )
    data = r.json()

    response = { "Home": homePath, "Data": data }

    return JsonResponse(response)

# Example of taking values from a POST request
@require_http_methods(["POST"])
def Helper(request):
    response = {}

    # Need to setup CRSF cookies - https://docs.djangoproject.com/en/2.2/ref/csrf/ - Or just disable the middleware
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)

    a = body['a']
    b = body['b']

    result = Sum(a, b)
    response = {
        "Home": "http://127.0.0.1:8000/",
        "Result": result
    }

    return JsonResponse(response)
