from django.http import JsonResponse
from django.shortcuts import render
from .models import City,Country
# Create your views here.

def get_town_of_country(request):
    country_id=request.GET.get("country",0)
    city_list=City.objects.filter(country=Country(id=country_id))
    city_list_2=[city.to_dict() for city in city_list]

    return JsonResponse({"data":city_list_2})
