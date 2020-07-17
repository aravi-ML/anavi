from django.db import models
from django.contrib import admin

from anaviuser.model.user import *
class WebSite(models.Model):
    """represent the website where the comments are take"""
    link = models.URLField()
    name = models.CharField(max_length=100)
    add_date=models.DateTimeField(auto_now=True)
    state = models.BooleanField(default=False)
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)

    def if_exists(self):
        ws_exist=WebSite.objecs.filter(name__iexact=self.name)
        return len(ws_exist)>0
    
    def __str__(self):
        return self.name+"("+self.link+")"

class WebSiteAdmin(admin.ModelAdmin):
    list_display=['id','name','link']
    search_fields=['name']


admin.site.register(WebSite,WebSiteAdmin)