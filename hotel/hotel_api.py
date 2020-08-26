from django.http import JsonResponse
from .hotel_service import *
from countryapp.models import Country,City
def add_from_user(request):
    response= {"state":False}
    user=User(id=request.session["user"]["id"])
    hotel_name=request.POST.get("hotel-name","").strip()
    hotel_country=request.POST.get("hotel-country",0).strip()
    hotel_town=request.POST.get("hotel-town",0)
    hotel_description=request.POST.get("hotel-description","")
    hotel_phone=request.POST.get("hotel-phone","")
    hotel_email=request.POST.get("hotel-email","")

    hotel=Hotel(user=user,name=hotel_name,place="",state=False,add_from_user=True,description=hotel_description,country=Country(id=hotel_country),city=City(id=hotel_town),email=hotel_email,phone=hotel_phone)
    
    hotel.save()
    response['state']=True
    response["msg"]="Hotel add with success\n We will contact you nearly for confirmation \n<b>Check your mail box </b>"
    return JsonResponse(response)


def get_hotel_stat(request,token):
    hotel=Hotel.objects.get(token=token)
    group_stat=HotelService.get_group_aspect_stat(hotel)
    comment_by_web_site=HotelService.get_comment_by_website(hotel)

    to_return={"group_aspect":group_stat,"group_comment":comment_by_web_site}
    return JsonResponse(to_return)
