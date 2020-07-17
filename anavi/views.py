from django.http import HttpResponse,Http404,HttpRequest
from django.shortcuts import render

def index(request):
    context={"title":"Anavi Home"}
    return render(request,'anavibase/index.html',context)