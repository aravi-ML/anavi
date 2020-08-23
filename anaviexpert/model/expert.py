from django.db import models
from anaviuser.model.user import User
from django.contrib import admin
class Expert(models.Model):
    """ class which represent the Expert (the person who add label to world) of our system"""
    user=models.ForeignKey(User,on_delete=models.CASCADE)

admin.site.register(Expert)