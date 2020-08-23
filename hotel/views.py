from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from hotel.hotel_service import *
from countryapp.models import Country
# Create your views here.

def add(request):
    response= {"state":False}
    hotel_name=request.POST['name']
    hotel_link=request.POST['link']
    hotel_state=True if request.POST['state']==1 else False
    hotel=Hotel(name=hotel_name,link=hotel_link,state=hotel_state)
    hotel_exist=Hotel.objects.filter(name=hotel_name)
    if(len(hotel_exist)==0):
        response['state']=True
        return JsonResponse(response)
    else:
        response["msg"]="Another hotel already have a same name"
        return JsonResponse(response)

def get_list(request):
    list_hotel=Hotel.objects.all().order_by("name")


def link_to_web_site(request):
    """That function take hotel and website and save it to a database"""
    response={"state":False}
    hotel=Hotel(pk=request.POST['hotel'])
    website=WebSite(pk=request.POST['website'])
    hotel_website=HotelWebSite()
    hotel_website.hotel=hotel
    hotel_website.website=website
    already_match=HotelWebSite.objects.filter(hotel=hotel,website=website)
    if(len(already_match)==0):
        response['state']=True
        hotel_website.save()
    return response

def dashboard(request,pk):
    hotel=Hotel(id=pk)
    info_most_comment=HotelService().get_website_have_most_comment(hotel)
    nb_comment=HotelService().count_comment(hotel)
    context={"id":pk,"nb_comment":nb_comment}
    if(info_most_comment!=None):
        context["web"]=info_most_comment

    return render(request,"hotel/dashboard_hotel.html",context)

def hotel_add_user_side(request):
    country_list=Country.objects.all().order_by("name_en")
    hotel_list=Hotel.objects.all().exclude(add_from_user=True,accept=False)
    context={"country_list":country_list,"hotel_list":hotel_list}
    return render(request,"hotel/hotel_add_user_side.html",context)
