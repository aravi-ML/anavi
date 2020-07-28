from django.shortcuts import render

# Create your views here.
def login(request):
    context={"title":"Sing In"}
    return render(request,'anaviuser/login.html',context)

def signup(request):
    context = {"title":"sign Up"}
    return render(request,'anaviuser/signup.html',context)

def reinitialiser(request):
    context = {"title":"reinitialise","reset":"Reset your password"}
    return render(request,'anaviuser/reinitialiser_pwd.html', context)


def reinitialise_mail(request):
    context  = {"title":"mail_reinitialise","reset":"Reinitialise your password"}
    return render(request,'anaviuser/reinitialize_mail.html',context)

def reinitialise_code(request):
    context = {"title":"code_reinitialize","reset":"Reinitialise your password"}
    return render(request,'anaviuser/reinitialise_code.html',context)