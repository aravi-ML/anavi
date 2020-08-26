from django.http import HttpResponse
from django.shortcuts import render,loader
from anaviuser.models import User
from anavicontact.email_service import EmailService
import random

# Create your views here.
def login(request):
    context={"title":"Sing In"}
    return render(request,'anaviuser/login.html',context)

def logout(request):
    request.session.clear()
    context={"title":"Home"}
    return render(request,"anavibase/index.html",context)


def signup(request):
    context = {"title":"sign Up"}
    return render(request,'anaviuser/signup.html',context)

def reinitialiser(request):
    context = {"title":"reinitialise","reset":"Reset your password"}
    mail = request.GET.get("email","")
    code=request.GET.get("code","")
    try: 
      check_mail = User.objects.get(email=mail,renitialisation_code=code)
      
      return render(request,'anaviuser/reinitialiser_pwd.html', context)
    except User.DoesNotExist:
      return HttpResponse("Not matcihing between email and code")

    


def reinitialise_mail(request):
    context  = {"title":"mail_reinitialise","reset":"Reinitialise your password"}

    return render(request,'anaviuser/reinitialize_mail.html',context)

def reinitialise_code(request):
    context = {"title":"code_reinitialize","reset":"Reinitialise your password"}
    email=request.POST["mail"].strip()
    
    users=User.objects.filter(email=email)
    if(len(users)==1):
        user=users[0]
        context={"code":random.randint(10000,99999),"name":user.name,"email":user.email}
        user.renitialisation_code=context["code"]
        user.save()
        data={"msg":loader.render_to_string("anaviuser/email/email_password_reset.html",context),"subject":"Password renitialisation"}
        EmailService.send_email("anavi",[user.email],data)
        return render(request,"anaviuser/reinitialise_code.html",context)
    else:
        return HttpResponse("Cette addresse email n'existe pas")
    