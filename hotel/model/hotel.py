from django.db import models
from django.contrib import admin
from anaviuser.model.user import *
from countryapp.models import City, Country
class Hotel(models.Model):
    """represent the structure of a manager"""
    name = models.CharField(max_length=255)
    place= models.CharField(max_length=255,default="",null=True,blank=True)
    state = models.BooleanField(default=False)
    #manager = models.ForeignKey(Manager, on_delete=models.CASCADE,null=True,blank=True)
    user=models.ForeignKey(User,on_delete=models.SET_NULL, null=True,default=None)
    add_date=models.DateTimeField(auto_now_add=True)
    add_from_user=models.BooleanField(default=False,help_text="Is to know if hotel was added by an admin or by user form space manager")
    description=models.TextField(default="",null=True,blank=True)
    country=models.ForeignKey(Country,on_delete=models.SET_NULL,null=True,default=None,blank=True)
    city=models.ForeignKey(City,on_delete=models.SET_NULL,null=True,blank=True,default=None)
    email=models.CharField(max_length=100,default="",null=True,blank=True)
    phone=models.CharField(max_length=100,null=True,default="",blank=True)
    accept=models.BooleanField(default=False)
    accept_by=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,default=None,related_name="accept_by")

    def __str__(self):
        return self.name+"("+str(self.pk)+")"
    
    def if_exist(self):
        hotel_exist=Hotel.objects.filter(name__iexact=self.name)
        return len(hotel_exist)>0 
    
    @property
    def to_dict(self):
        return {
            "id":self.pk,
            "state":self.state,
            "place":self.place,
            "add_date":self.add_date,
            "user":self.user
        }

class HotelAdmin(admin.ModelAdmin):
    list_display=['id','name','add_date','state']


admin.site.register(Hotel,HotelAdmin)
