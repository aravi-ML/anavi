
from django.shortcuts import render
from  django.conf import settings
from django.http import HttpResponse
from django.contrib import admin
from django.db import models
from anaviuser.models import * 
from anaviuser.model.user_service import *  
import string

"""
   this is user_api
   name = request.POST("name")
    print(name)
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


    

  
