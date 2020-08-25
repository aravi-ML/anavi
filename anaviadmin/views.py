from django.shortcuts import render
from website.website_service import WebSiteService
from hotel.hotel_service import HotelService
from comment.comment_service import CommentService
from anaviexpert.expert_service import ExpertService
from anaviuser.model.user_service import UserService
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
