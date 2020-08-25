from django.http import JsonResponse
from django.shortcuts import render
from django.contrib import admin
from anaviuser.models import * 
from .user_service import *

def login(request):
    user_login=request.POST.get("email","").strip()
    user_password=request.POST.get("password","").strip()

    user=User(email=user_login,phone=user_login,password=user_password)
    state_authenticated=UserService.authenticate(user)
    if(state_authenticated["status"]==True):
        request.session["user"]=state_authenticated["user"]
        
    return JsonResponse(state_authenticated)

"""
before adding a user we check if he enter the correct password else we ak him to re
"""
def addUser(request):
    name = request.POST["name"]
    print(name)
    email = request.POST["mail"]
    password = request.POST["password"]
    c_password = request.POST["c-password"]
    phone= 0
    last_name = ""
    state = False
    if ((name != "") & (email != "") & (len(password)>= 8 ) & (password == c_password)):
#check if the account exit by findin the email input
         try:
             check_mail = User.objects.get(email=email)
         except User.DoesNotExist: 
             check_mail = None
         if (check_mail == None):
             user = User(name=name,last_name=last_name,email=email,password=password)
             user_add = UserService.add_user(user)
             return render(request,'anavibase/index.html')
         else:
            return render(request,'anaviuser/login.html')
    else:
        return render(request,'anaviuser/signup.html')

