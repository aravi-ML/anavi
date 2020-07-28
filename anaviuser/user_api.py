from django.http import HttpResponse, JsonResponse
from anaviuser.model.user import User
from anaviuser.user_service import UserService

def login(request):
    user_login=request.POST["email"]
    user_password=request.POST["password"]

    user=User(email=user_login,password=user_password)
    user_service=UserService()
    state_authenticated=user_service.authenticate(user)
    if(state_authenticated["status"]==True):
        request.session["user"]=state_authenticated["user"].to_dict()
        
    return JsonResponse(state_authenticated)