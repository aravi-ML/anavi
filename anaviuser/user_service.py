from django.db.models import Q
from anaviuser.model.user import User
class UserService:
    def __init__(self):
        pass

    def count(self):
        """Return the total number of user in our system """
        return len(User.objects.all())
    
    @classmethod
    def authenticate(cls,user):
        user=User.objects.filter(Q(email=user.email) | Q(phone=user.email),password=user.password)
        response={"status":False,"msg":""}
        if(len(user)==1):
            user=user[0]
            if(user.state==False):
                response["msg"]="Votre compte a ete desactiver du systeme"
                return response
            elif(user.confirmed==False):
                response["msg"]="Votre compte n'est pas encore activé,veuillez terminez le processus d'inscription"

            elif(user.confirmed==True):
                response["status"]=True
                response["msg"]="Connexion effectue avec success"
                response["user"]=user.to_dict()
                return response
        else:
            response["msg"]="veuillez verifier votre addresse email et votre mot de passe"
        
        return response
    
    @classmethod
    def is_authenticated(cls,request):
        user_session=request.session.get("user",None)
        return user_session

