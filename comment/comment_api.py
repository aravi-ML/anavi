from django.http import HttpResponse, JsonResponse
import json

from .model.comment import Comment
from .model.expert_comment import ExpertComment
from .model.aspect_en import AspectEn
def tag_comment(request):
    try:
        comments=json.loads(request.POST["comment_to_tag"])
        for comment in comments:
            #print(comment)
            ncomment=Comment(id=comment["id"])
            expert_comment=ExpertComment(comment=ncomment,label=comment["polarity"])
            #verifions si l'utilisateur n'a pas encore etiquetter l'aspect
            #exist_etiquette=ExpertComment.objects.filter(aspect=aspect,comment=ncomment)
            expert_comment.save()

            for aspect in comment["aspects"]:
                aspect=AspectEn()
                aspect.id=aspect.id
                #aspect
        #bonjour=json.JSONDecoder(comment)
        return JsonResponse(comments[0])
    except KeyError as e:
        return JsonResponse(request.POST)