from django.shortcuts import render
from website.website_service import WebSiteService
from hotel.hotel_service import HotelService
from hotel.model.hotel import Hotel
from comment.comment_service import CommentService
from comment.model.comment import *
from anaviexpert.expert_service import Expert,ExpertService
from anaviexpert.models import AskExpert
from anaviuser.user_service import UserService
from anavisearcher.searcher_service import SearcherService
from anavimanager.models import Manager,AskManage

# Create your views here.


def admin_dashboad(request):
    context = {
        "nb": {
            "comment": CommentService().count(),
            "website": WebSiteService().count(),
            "user": UserService().count(),
            "searcher": SearcherService().count(),
            "expert": ExpertService().count(),
            "hotel": HotelService().count(),
        },
    }
    return render(request, "anaviadmin/dashboard.html", context)

def download(request):
    unique_hotel=Comment.objects.values("hotel").distinct()
    hotel_list=[]
    for hotel in unique_hotel:
        hotel_list.append(hotel["hotel"])
    hotel_listf=Hotel.objects.filter(id__in=hotel_list)
    context={"hotels":hotel_listf}
    return render(request,"anaviadmin/download_data.html",context)


def ask_managing_list(request):
    list_of_ask_managing=AskManage.objects.all().order_by("-add_date").filter(decision_by=None)
    context={"list_ask_manage":list_of_ask_managing}
    return render(request,"manager/admin/list_ask_managing.html",context)


def expert(request):
    context={}
    all_expert=Expert.objects.all()
    ask_demand=AskExpert.objects.filter(decision_by=None)
    ask_demand_rejected=AskExpert.objects.exclude(decision_by=None).filter(state=False)
    if(len(all_expert)>0):
        context["experts"]=all_expert
    if(len(ask_demand)>0):
        context["applies"]=ask_demand
    if(len(ask_demand_rejected)>0):
        context["rejected_applies"]=ask_demand_rejected

    return render(request,"anaviexpert/admin/expert.html",context)
