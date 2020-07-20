from django.db import models
from django.contrib import admin
from anavimanager.model.manager import Manager
from anaviuser.model.user import *

class Hotel(models.Model):
    """represent the structure of a manager"""
    name = models.CharField(max_length=255)
    place= models.CharField(max_length=255)
    state = models.BooleanField(default=False)
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE,null=True,blank=True)
    #user=models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    add_date=models.DateTimeField(auto_now_add=True)

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
            "manager":self.manager
        }

class HotelAdmin(admin.ModelAdmin):
    list_display=['id','name','add_date','state']


admin.site.register(Hotel,HotelAdmin)
