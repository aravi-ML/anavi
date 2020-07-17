from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .anaviselenium.hotels_crawler import HotelsCrawler
# Create your views here.

def home(request):
    context={"title":"Crwalling"}
    return render(request,"crwaling/index.html",context)

def crwal(request,hotel):
    hcrwaler=HotelsCrawler()
    hcrwaler.parse()
    return HttpResponse("Your want to crwal "+hotel)


