from django.http import JsonResponse
from .models import AskExpert,User,Expert

def perform_ask_exepert(request):
    language=request.POST.get("expert-lang","")
    language=language+","+request.POST.get("other-expert-lang","")
    user=User(id=request.session["user"]["id"])
    ask_expert=AskExpert(user=user,language=language)
    ask_expert.save()
    result={"status":True,"msg":"Your demand is on process, you will receive notification, \n <b>Please check constaly your email</b>"}
    return JsonResponse(result)


#cette fonction doit etre accesible uniquement par un administrateur

def decide_apply_expert_demand(request):
    result={"status":True}
    decision=request.GET.get("decision","").strip()
    ask_id=request.GET.get("ask","").strip()
    askexpert=AskExpert.objects.get(id=ask_id)
    user=User(id=request.session["user"]["id"])
    askexpert.decision_by=user
    if(decision=="r"):
        askexpert.state=False
        result["msg"]="Apply rejected with success"
        askexpert.save()
    elif(decision=="a"):
        expert=Expert(user=askexpert.user,state=True,add_by=user)
        askexpert.state=True
        askexpert.save()
        expert.save()
        result["msg"]="Apply accepted with success"
    else:
        result["msg"]="Error occured during process"
        result["status"]=False
    return JsonResponse(result)