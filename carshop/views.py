from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import requests
import json
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from carshop.models import *
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
# Create your views here.

def index(request):
    return render(request,"home.html")

def contact(request):
    return render(request,"contact.html")

@csrf_exempt
def message(request):
    data = json.loads(request.body)
    text = data.get("text", "")
    email = data.get("email", "")
    object = Message(text=text , email=email , responded=False)
    object.save()
    return JsonResponse({"message": "Message sent successfully."}, status=201)

def about(request):
    return render(request,"about.html")

@csrf_exempt
def search(request):
    query = request.GET["search"]
    vector = SearchVector('make','model','year','milage','cost','description','new')
    query = SearchQuery(query)
    objects = car.objects.annotate(rank=SearchRank(vector, query)).order_by('-rank').filter(sold=False)
    return render(request,"search.html",{"carData":objects})

def carDisplay(request, carID):
    object = car.objects.get(id=carID)
    try:
        nextCar = car.objects.get(id=(carID+1))
    except:
        nextCar = None
    return render(request,"car.html",{"car":object, "nextCar":nextCar})
