from django.db import models
from django.contrib import admin
class User(models.Model):
    """ class which represent the user (hotel manager, data scientist, searcher) of our system"""
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=200)
    state = models.BooleanField(default=False)
    add_date = models.DateTimeField(auto_now_add=True)
    phone = models.IntegerField(null=True)

    def __str__(self):
        return self.name+" "+self.last_name+"("+str(self.pk)+")"

class UserAdmin(admin.ModelAdmin):
    list_display=['name','name','last_name','phone']
    search_fields=['name','last_name','phone']

admin.site.register(User,UserAdmin)