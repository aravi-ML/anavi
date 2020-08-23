from django.http import HttpResponse,Http404,HttpRequest
from django.shortcuts import render
from anaviuser.user_service import *

def index(request):
    user_session=UserService.is_authenticated(request)
    context={"title":"Anavi Home","session":user_session}
    return render(request,'anavibase/index.html',context)