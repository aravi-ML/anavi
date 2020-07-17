from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from anavibase.models import *
# Create your views here.

def add_api(request):
    response={"state":False}
    website=WebSite()
    website.name=request.POST['name']
    website.link=request.POST['link']
    website_exist=WebSite.objects.filter(name=website.name)
    if(len(website_exist)==0):
        response["state"]=True
        website.save()
    return response

def add_view(request):
    context={"title": "Ajouter un site web" }
    return render(request,"website/add_website.html",context)