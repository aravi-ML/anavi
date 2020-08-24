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

    def hotel_inf(self):
        return {
            "name":self.hotel.name,
            "id":self.hotel.id,
            "place":self.hotel.place,
            "phone":self.hotel.phone,
            "email":self.hotel.email,
            "token":self.hotel.token
        }
    def user_inf(self):
        return {
            "name":self.user.name,
            "phone":self.user.phone,
            "email":self.user.email,
            "id":self.user.id,
            "state":self.user.state,
            "is_admin":self.user.is_admin
        }

admin.site.register(Manager)