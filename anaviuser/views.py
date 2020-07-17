from django.shortcuts import render

# Create your views here.
def login(request):
    context={"title":"Singin"}
    return render(request,'anaviuser/login.html',context);