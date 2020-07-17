from django.db import models
from django.contrib import admin

from hotel.model.hotel import Hotel,HotelAdmin
from website.model.website import WebSite,WebSiteAdmin


class HotelWebSite(models.Model):
    """this class is to know if hotel is present in a website or not"""
    hotel=models.ForeignKey(Hotel,on_delete=models.SET_NULL,null=True)
    website=models.ForeignKey(WebSite,on_delete=models.SET_NULL,null=True)
    hotel_id_in_website=models.CharField(null=True,max_length=160)
    add_date=models.DateTimeField(auto_now_add=True)

    def if_exist(self):
        hotel_website=Hotel.objects.filter(hotel=self.hotel,website=self.website)
        return len(hotel_website)>0

admin.site.register(HotelWebSite)
    