from django.shortcuts import render
from .models import Expert,User,AskExpert
# Create your views here.


def tag_data(request):
    return render(request,"comment/tag_data.html")

def expert_space(request):
    context={}
    #on va verifie si cet utilisateur est deja consider comme un expert
    user=User(id=request.session["user"]["id"])
    expert=Expert.objects.filter(user=user)
    if(len(expert)>0):
        expert=expert[0]
        return render(request,"anaviexpert/expert_choice.html",context)

    return render(request,"anaviexpert/expert_space.html",context)