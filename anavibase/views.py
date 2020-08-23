from django.shortcuts import render
from anaviuser.user_service import *

# Create your views here.

def error_404(request):
    context={"msg":"Nothtin"}
    return render(request,"error/error_404.html",context)

def error_500(request):
    context={"msg":"Nothtin"}
    return render(request,"error/error_500.html",context)

def email_sended(request):
    context={"data":{"name":"ANAVI","code":989838}}
    return render(request,"emails/email_confirm_code.html",context)


def team(request):
    user_session=UserService.is_authenticated(request)
    context={"session":user_session}
    return render(request,"about/about.html",context)