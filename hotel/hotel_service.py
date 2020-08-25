from django.db.models import Count
from hotel.model.hotel import *
from hotel.model.hotel_website import *
from .hotel_website_service import HotelWebSiteService
from comment.comment_service import Comment,CommentService

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
            