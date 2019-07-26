import json
import datetime
import requests

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.views.decorators.http import require_http_methods

from .models import Checklist, ShoppingList
from .helper import Sum

# Global Variables
homePath = "http://127.0.0.1:8000/"

# Create your views here.
def Index(request):

    paths = {
        "Home": homePath,
        "Joke": "http://127.0.0.1:8000/joke",
        "Task": "http://127.0.0.1:8000/json",
        "List": "http://127.0.0.1:8000/list",
        "Helper": "http://127.0.0.1:8000/helper",
        "Fact": "http://127.0.0.1:8000/fact"
    }

    return JsonResponse(paths)

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


def Fact(request):
    URL = "https://uselessfacts.jsph.pl/random.json?language=en"
    HEADERS = { "content-type": "application/json", "accept": "application/json" }

    r = requests.get( url = URL, headers = HEADERS )
    data = r.json()

    response = { "Home": homePath, "Data": data }

    return JsonResponse(response)

def Json(request):
    taskTimeNow = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    task = { 
            "task": "Return JSON from api requests",
            "severity": "1",
            "complete": "0",
            "added": taskTimeNow
        }

    return JsonResponse(task)

def Joke(request):
    URL = "https://icanhazdadjoke.com/"
    HEADERS = { "content-type": "application/json", "accept": "application/json" }

    r = requests.get( url = URL, headers = HEADERS )
    data = r.json()

    response = { "Home": homePath, "Data": data }

    return JsonResponse(response)

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