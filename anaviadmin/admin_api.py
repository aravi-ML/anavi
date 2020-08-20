from django.http import JsonResponse,HttpResponse
from hotel.hotel_service import *
from comment.comment_service import *
from anavi.utility import *

def download_data(request):
    hotel_id=request.GET.get("choose_hotel",0)
    format_data=request.GET.get("format","json")
    #Maintenant nous devons recuperer tous les commentaires de cet hotel
    comment_hotel=Comment.objects.filter(hotel=Hotel(id=hotel_id))
    length=len(comment_hotel)
    comment_dump=[]
    json_all_comments=""
    for i in list(range(length-1)):
        comment_dump.append(comment_hotel[i].to_dict())
        json_all_comments+=json_all_comments+"\t\t"+comment_hotel[i].to_json_string()+",\n"
    
    json_all_comments+="\t\t"+comment_hotel[length-1].to_json_string()+"\n"
    json_all_comments='{\n \t "comments":[\n'+json_all_comments+']\n}'
    
    comment_dump={"data":comment_dump}
    #maintenant nous devons ecrire un nouveau fichiers avec un nom hazardeu
    random_name=get_random_string(20)+".json"
    content_type="application/json"
    response=HttpResponse(json_all_comments,content_type=content_type)
    response["Content-Disposition"]='attachment; filename="anavi_hotel_data.json"'

    comment_dump["status"]=True
    return response