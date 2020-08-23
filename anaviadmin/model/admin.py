from django.db import models
from anaviuser.model.user import User
from django.contrib import admin

class Admin(models.Model):
    """ class which represent the admin of our system"""
    user=models.ForeignKey(User,on_delete=models.CASCADE)

admin.site.register(Admin)