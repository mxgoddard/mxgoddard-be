import json
from datetime import date, datetime, timedelta
import requests

from django.core import serializers
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
    
    routine = []
    
    for dayObj in everything:
        obj = { "day": dayObj.day, "date": dayObj.date, "pushups": dayObj.pushups, "notes": dayObj.notes }
        routine.append(obj)

    return JsonResponse({ "Routine": routine })

# /pushups/update
@require_http_methods(["POST"])
def UpdateDay(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)

    date = body['date']
    pushups = body['pushups']

    t = Routine.objects.get(date=date)
    t.pushups = pushups
    t.save()

    return JsonResponse({ "Date": date, "Pushups": pushups })

# /pushups/failed
@require_http_methods(["GET"])
def FailedDay(request):
    # Failed day method should only be called after the day is over - Is there a way to automate this?
    # Need to add 2 days onto the routine on failure
    # Need some error handling - day can 
    # Try to call this method as little as possible

    startDate = "2019-07-27"
    originalFinalDate = "2019-08-26"
    numDaysInRoutine = 31

    # Query DB for all days prior where pushups != 200
    # Can use raw sql, need to come up with a query for this
    todayDate = datetime.today().strftime("%Y-%m-%d")
    extraDays = 0

    for dayObj in Routine.objects.raw("SELECT * FROM mysite_routine WHERE pushups != 200 AND date < %s;", [todayDate]):
        extraDays += 1

    # Extra days = 2 * failedDays
    extraDays *= 2

    # Check if newFinalDate is in DB - Add extraDays onto date
    tempOriginalDate = datetime.strptime(originalFinalDate, "%Y-%m-%d")
    newFinalDate = tempOriginalDate + timedelta(days=extraDays)
    print(newFinalDate)

    # If not find the latest date and create records up to the newFinalDate

    return JsonResponse({ "a": "b", "c": "d" })


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
