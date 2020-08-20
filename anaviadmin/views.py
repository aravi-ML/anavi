from django.shortcuts import render
from website.website_service import WebSiteService
from hotel.hotel_service import HotelService
from hotel.model.hotel import Hotel
from comment.comment_service import CommentService
from comment.model.comment import *
from anaviexpert.expert_service import ExpertService
from anaviuser.user_service import UserService
from anavisearcher.searcher_service import SearcherService
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
        hotel_list.append(Hotel.objects.get(pk=hotel["hotel"]))
    context={"hotels":hotel_list}
    return render(request,"anaviadmin/download_data.html",context)
