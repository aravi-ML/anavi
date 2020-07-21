from django.db import models
from django.contrib import admin
from .comment import Comment
from anavibase.model.positive_big_int import *

class Aspect(models.Model):
    """When we detect some aspect on our comment, we save it on
    aspect term in the table aspect"""
    id=PositiveAutoBigInt(primary_key=True)
    name_fr=models.CharField(max_length=255, default="")
    name_en=models.CharField(max_length=255, default="")
    sentence_index=models.PositiveIntegerField(default=0,help_text="Field to know in wich sentence aspect was extracted")
    comment=models.ForeignKey(Comment,on_delete=models.CASCADE)
    start_to=models.PositiveIntegerField(default=0)
    end_to=models.PositiveIntegerField(default=0)

class AspectAdmin(admin.ModelAdmin):
    display_list=["name","comment",'start_to','end_to']
    search_fields=["name","comment"]

admin.site.register(Aspect,AspectAdmin)