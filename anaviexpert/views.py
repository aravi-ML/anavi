from django.shortcuts import render

# Create your views here.


def tag_data(request):
    return render(request,"comment/tag_data.html")