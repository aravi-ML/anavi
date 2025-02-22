from django.db.models import Count
from hotel.model.hotel import *
from hotel.model.hotel_website import *
from .hotel_website_service import HotelWebSiteService

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
        return len(Hotel.objects.all())
    
    def count_comment(self,hotel):
        comment=hotel.comment_set.all()
        return len(comment)
    
    def get_website_have_most_comment(self,hotel):
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
        exist=self.if_exist_hotel(hotel);
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
        return hwservice.add(hotelwebsite);
    
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