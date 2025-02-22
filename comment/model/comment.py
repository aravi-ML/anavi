from django.db import models
from django.contrib import admin
from hotel.model.hotel import Hotel,HotelAdmin
from django.db.models import Q
from website.model.website import *
class Comment(models.Model):
    """ represent the comment of the structure on the website"""
    text = models.TextField()
    state = models.BooleanField(default=False)
    add_date = models.DateTimeField(null=True,blank=True)
    hotel = models.ForeignKey(Hotel, blank=True, on_delete=models.SET_NULL,null=True)
    website = models.ForeignKey(WebSite, blank=True, on_delete=models.SET_NULL,null=True)

    @property
    def to_dict(self):
        return {
            'comment': json.load(self.text),
            'date': self.date,
            'hotel':self.hotel.name
        }
    
    def __str__(self):
        return self.text+"("+str(self.id)+")"
    def if_exist(self):
        comment_list=Comment.objects.filter(text__iexact=self.text,hotel=self.hotel,website=self.website,add_date=self.add_date)
        lenght=len(comment_list)
        print("la taille est "+str(length))
        if(lenght>0):
            return True
        else:
            return False

class CommentAdmin(admin.ModelAdmin):
    fields=['text','hotel','website','state']
    list_display=['id','text','add_date','hotel','website','state']
    list_filter=['hotel','website','state']
    search_fields=['text']

admin.site.register(Comment,CommentAdmin)