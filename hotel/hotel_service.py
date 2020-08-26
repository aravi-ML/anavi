from django.db.models import Count
from hotel.model.hotel import *
from hotel.model.hotel_website import *
from .hotel_website_service import HotelWebSiteService
from comment.comment_service import Comment,CommentService
from comment.models import Aspect

import unidecode

class HotelService:
    """This class is to make all operation about hotel
    If you want to add, get, list, update find, is important to pass by this class"""
    def __init__(self):
        pass

    def if_exist_hotel(self,hotel):
        """That function verify if current hotel exist"""
        hotel_exist=Hotel.objects.filter(name__iexact=hotel.name)
        response={"hotel":None,"status":False}
        if(len(hotel_exist)>0):
            response["hotel"]=hotel_exist[0]
            response["status"]=True
        return response
    
    def count(self):
        """Function who return the number of saved hotel"""
        return Hotel.objects.aggregate(nb=models.Count("id"))["nb"]
   
    @classmethod
    def count_comment(cls,hotel):
        comment=hotel.comment_set.all()
        return len(comment)
    
    @classmethod
    def get_website_have_most_comment(cls,hotel):
        """Take hotel in parameter and return the website who have more
        feedback than others concerning it"""
        list_web_site=hotel.comment_set.all().values("website").annotate(nb=Count("text")).order_by("nb")
        lenght=len(list_web_site)
        if(lenght<=0):
            return None
        else:
            most=list_web_site[lenght-1]
            website=WebSite.objects.get(pk=most["website"])
            return {"website":website,"nb":most["nb"]}
    
    def add_hotel(self,hotel):
        response= {"status":False,"msg":"hotel add with success","hotel":None}
        exist=self.if_exist_hotel(hotel)
        if(exist["status"]==False):
            response['status']=True
            hotel.save()
            response['id']=hotel.pk
            response['hotel']=hotel
        else:
            response["msg"]="Another hotel already have a same name"
            response["hotel"]=exist["hotel"]
        return response
    
    def add_hotel_to_web_site(self,hotelwebsite):
        """That function is to add hotel to a website"""
        hwservice=HotelWebSiteService()
        return hwservice.add(hotelwebsite)
    
    def find_hotel_by_id(self,hotel):
        response={"hotel":None}
        try:
            hotel=Hotel.object.get(pk=hotel.id)
            response["hotel"]=hotel
        except:
            pass
        return response
    
    def find_hotel_by_name(self,hotel):
        response={"hotel":None}
        try:
            hotel=Hotel.objects.get(name__iexact=hotel.name)
            response["hotel"]=hotel
        except:
            pass
        return response
    
    @classmethod
    def get_comment_by_website(cls,hotel):
        """That method return all the website and the comment that are present
            for this hotel in every website"""
        comment_by_site=Comment.objects.filter(hotel=hotel).values("website").annotate(nb=models.Count("text")).order_by("nb")
        final_result={}
        for result in comment_by_site:
            website=WebSite.objects.get(id=result["website"])
            final_result[website.name]=result["nb"]
        return final_result
    
    @classmethod
    def get_aspect_stat(cls,hotel):
        """function all the stat by aspect on one hotel """
        comment_list=hotel.comment_set.all()
        all_aspect=Aspect.objects.filter(comment__in=comment_list).values("name_fr","polarity").annotate(nb=models.Count("polarity"))
        #maintenant nous devons regrouper les statistique par nom
        stata={}
        for aspect in all_aspect:
            #On essaye d'acceder a la cle si cela ne marche on cree un dictionnaire de la cle
            name_i=unidecode.unidecode(aspect["name_fr"])
            if(stata.get(name_i,None)==None):
                stata[name_i]={"negative":0,"positive":0,"neutral":0,"total":0,"name":aspect["name_fr"]}
            stata[name_i][aspect["polarity"]]=aspect["nb"]
            stata[name_i]["total"]+=aspect["nb"]
            stata[name_i]["pos_percent"]=round((stata[name_i]["positive"]*100)/stata[name_i]["total"],2)
            stata[name_i]["neg_percent"]=round((stata[name_i]["negative"]*100)/stata[name_i]["total"],2)
            stata[name_i]["neu_percent"]=round((stata[name_i]["neutral"]*100)/stata[name_i]["total"],2)
        return stata
    
    @classmethod
    def get_group_aspect_stat(cls,hotel):
        """return general stat of hotel by aspect category"""
        hotel=Hotel(id=hotel.id)
        comment_all=hotel.comment_set.all()
        aspect_stat=Aspect.objects.filter(comment__in=comment_all).values("category","polarity").annotate(nb=models.Count("polarity"))
        stata={}
        for aspect in aspect_stat:
            name_i=unidecode.unidecode(aspect["category"])
            if(stata.get(name_i,None)==None):
                stata[name_i]={"name_i":name_i,"name":aspect["category"],"positive":0,"neutral":0,"negative":0,"total":0}
            stata[name_i][aspect["polarity"]]=aspect["nb"]
            stata[name_i]["total"]+=aspect["nb"]
            stata[name_i]["pos_percent"]=round((stata[name_i]["positive"]*100)/stata[name_i]["total"],2)
            stata[name_i]["neg_percent"]=round((stata[name_i]["negative"]*100)/stata[name_i]["total"],2)
            stata[name_i]["neu_percent"]=round((stata[name_i]["neutral"]*100)/stata[name_i]["total"],2)

        return stata


        return aspect_stat