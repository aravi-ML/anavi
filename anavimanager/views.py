from django.shortcuts import render
from anavimanager.manager_service import *
from hotel.hotel_service import Hotel,HotelService
# Create your views here.


def manager_space(request):
    context={}
    user_id=request.session["user"]["id"]
    user=User(id=user_id)
    hotel_list=ManagerService.get_managed_hotel(user)
    if(len(hotel_list)!=0):
        context["hotel_list"]=hotel_list
    return render(request,"manager/manager_space.html",context)
