from django.shortcuts import render
from anavimanager.manager_service import *
from anavimanager.models import AskManage
from hotel.hotel_service import Hotel,HotelService
# Create your views here.


def manager_space(request):
    context={}
    user_id=request.session["user"]["id"]
    user=User(id=user_id)
    hotel_list=ManagerService.get_managed_hotel(user)
    #get demand in waiting
    ask_manage_list=AskManage.objects.filter(user=user,state=False,decision_by=None)

    add_hotel=Hotel.objects.filter(user=user,accept_by=None)
    if(len(ask_manage_list)>0):
        context["ask_manage_list"]=ask_manage_list
    if(len(hotel_list)!=0):
        context["hotel_list"]=hotel_list
    if(len(add_hotel)>0):
        context["hotel_add_list"]=add_hotel
    
    return render(request,"manager/manager_space.html",context)
