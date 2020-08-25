from django.http import JsonResponse,HttpResponse
from hotel.hotel_service import *
from comment.comment_service import *
from anavi.utility import *
from anavimanager.models import AskManage, Manager,User

def download_data(request):
    hotel_id=request.GET.get("choose_hotel","").strip()
    format_data=request.GET.get("format","json")
    #Maintenant nous devons recuperer tous les commentaires de cet hotel
    if(hotel_id==""):
        comment_hotel=Comment.objects.all().exclude(Q(text="")|Q(text=None))
    else:
        comment_hotel=Comment.objects.filter(hotel=Hotel(id=hotel_id)).exclude(Q(text="")|Q(text=None))
    length=len(comment_hotel)
    comment_dump=[]
    json_all_comments=""
    file_name="comment/static/anavicomment/temp/"+get_random_string(15)+".json"
    with open(file_name,"w") as f:
        for i in list(range(length-1)):
           f.writelines("\t\t"+comment_hotel[i].to_json_string()+",\n")
    with open(file_name,"r") as f:
        json_all_comments=f.read()
    
    json_all_comments+="\t\t"+comment_hotel[length-1].to_json_string()+"\n"
    json_all_comments='{\n \t "comments":[\n'+json_all_comments+']\n}'
    
    #comment_dump={"data":comment_dump}
    #maintenant nous devons ecrire un nouveau fichiers avec un nom hazardeu
    random_name=get_random_string(20)+".json"
    content_type="application/json"
    response=HttpResponse(json_all_comments,content_type=content_type)
    response["Content-Disposition"]='attachment; filename="anavi_hotel_data.json"'

    #comment_dump["status"]=True
    return response

def perfom_decision_ask_managing(request):
    """When the demand of manage hotel is accepted, we will
    create a new manager for hotel. And he will""" 
    user=User(id=request.session["user"]["id"])
    askm_id=request.GET.get("askm",0)
    asmk_decision=request.GET.get("decision","i").lower().strip()
    askm=AskManage.objects.get(id=askm_id)
    askm.decision_by=user
    result={"status":True}
    if(asmk_decision=="a"):
        askm.state=True
        askm.save()
        #Now we create a new manager
        manager=Manager(user=askm.user,hotel=askm.hotel,state=True)
        manager.save()
        result["msg"]="Asking Confirm with successs"
    elif(asmk_decision=="r"):
        askm.state=False
        askm.save()
        result["msg"]="Asking was refuse with success"
    else:
        result["status"]=False
        result["msg"]="Error occured during presentation"

    return JsonResponse(result)