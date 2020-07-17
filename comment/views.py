from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .comment_service import *
# Create your views here.

def add(request):
    response={"state":False}
    comment=Comment()
    comment.text=request.POST['text']
    comment.hotel=Hotel(pk=request.POST['hotel'])
    comment.website=WebSite(pk=request.POST['website'])
    comment_exist=Comment.objects.filter(text=comment.text)
    if(len(comment_exist)==0):
        response['state':True]
        comment.save()
    else:
        pass
    return JsonResponse(response)

def get_json_format(request):
    all_comment=Comment.objects.all()


def tag_data(request):
    comment_list=CommentService().get_comment_page_list()
    context={"comment_list":comment_list}
    return render(request,"comment/tag_data.html",context)
    
