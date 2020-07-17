from .model.hotel_website import HotelWebSite

class HotelWebSiteService:
    def add(self,hotel_website):
        response={"status":False,"hotel_website":None}
        association_exist=HotelWebSite.objects.filter(hotel=hotel_website.hotel,website=hotel_website.website)
        if(len(association_exist)==0):
            hotel_website.save()
            response["status"]=True
            response["hotel_website"]=hotel_website
        return response