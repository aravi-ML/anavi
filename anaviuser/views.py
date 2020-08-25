from django.shortcuts import render
from anaviuser.models import User

# Create your views here.
def login(request):
    context={"title":"Sing In"}
    return render(request,'anaviuser/login.html',context)

def signup(request):
    context = {"title":"sign Up"}
    return render(request,'anaviuser/signup.html',context)

def reinitialiser(request):
    context = {"title":"reinitialise","reset":"Reset your password"}
    mail = request.POST["mail"]
    try: 
      check_mail = User.objects.get(email=mail)
      return render(request,'anaviuser/reinitialiser_pwd.html', context)
    except User.DoesNotExist:
      return render(request,'anaviuser/reinitialize_mail.html')

    


def reinitialise_mail(request):
    context  = {"title":"mail_reinitialise","reset":"Reinitialise your password"}

    return render(request,'anaviuser/reinitialize_mail.html',context)

def reinitialise_code(request,user):
    context = {"title":"code_reinitialize","reset":"Reinitialise your password"}
    password  = request.POST["password"]
    c_password = request.POST["c-password"]
    try:
        user = User.objects.get(email=user_email)
        user.password=password
        user.save()
        return render(request,'/',context)
    except User.DoesNotExist:
        return render (request,'anaviuser/reinitaliser_mail.html',context)


    