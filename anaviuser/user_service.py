from anaviuser.model.user import User
from  django.conf import settings
from django.contrib import admin
from django.db import models

class UserService:

    def count(self):
        """Return the total number of user in our system """
        return len(User.objects.all())
    @classmethod
    def add_user(cls,user):
    #we controls parameters after adding it in the data base if it begins with a 
        user.save()


    
    

