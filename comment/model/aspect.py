from django.db import models
from django.contrib import admin
from .comment import Comment


class Aspect(models.Model):
    """When we detect some aspect on our comment, we save it on
    aspect term in the table aspect"""
    name=models.TextField(max_length=255)
    comment=models.ForeignKey(Comment,on_delete=models.CASCADE)
    start_to=models.PositiveIntegerField(default=0)
    end_to=models.PositiveIntegerField(default=0)

class AspectAdmin(admin.ModelAdmin):
    display_list=["name","comment",'start_to','end_to']
    search_fields=["name","comment"]

admin.site.register(Aspect,AspectAdmin)