from django.http import JsonResponse
from hotel.hotel_service import Hotel
from anavimanager.models import AskManage
from anaviuser.models import User
def perform_ask_manage(request):
    """That function is for those who to become manager of an hotel which were crwaled
       By a anvi bot"""
    user=User(id=request.session["user"]["id"])
    h_name=request.POST.get("find-hotel-ask","")
    hotel=Hotel.objects.filter(name__iexact=h_name)
    result={"status":False}
    if(len(hotel)>0):
        hotel=hotel[0]
        result["status"]=True
        result["msg"]="Your demand is on process, you will receive an <b>Email about it</b>"
        askmanage=AskManage(user=user,hotel=hotel)
        askmanage.save()
    else:
        result["msg"]="Hotel doesn't exist on our platform <h2>Please add your own hotel</h2>"
    return JsonResponse(result)