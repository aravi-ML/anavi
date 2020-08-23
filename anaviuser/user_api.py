from django.http import HttpResponse, JsonResponse
from anaviuser.model.user import User
from anaviuser.user_service import UserService

def login(request):
    user_login=request.POST.get("email","").strip()
    user_password=request.POST.get("password","").strip()

    user=User(email=user_login,phone=user_login,password=user_password)
    state_authenticated=UserService.authenticate(user)
    if(state_authenticated["status"]==True):
        request.session["user"]=state_authenticated["user"]
        
    return JsonResponse(state_authenticated)