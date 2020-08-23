from django.db import models
from django.contrib import admin

from anaviuser.model.user import User
from hotel.model.hotel import Hotel

class Manager(models.Model):
    """ class which represent the hotel manager of our system"""
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    hotel= models.ForeignKey(Hotel,on_delete=models.CASCADE,default=None)
    main_manager=models.BooleanField(default=False)
    state=models.BooleanField(default=True)

admin.site.register(Manager)