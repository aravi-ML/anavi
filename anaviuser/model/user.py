from django.conf import settings
from django.db import models
from django.contrib import admin
class User(models.Model):
    """ class which represent the user (hotel manager, data scientist, searcher) of our system"""
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100,null=True,)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=200)
    state = models.BooleanField(default=True)
    add_date = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(null=True,blank=True,max_length=25)
    confirm_code=models.PositiveIntegerField(default=0)
    renitialisation_code=models.CharField(max_length=20,default="")
    confirmed=models.BooleanField(default=False)
    is_admin=models.BooleanField(default=False)


    def __str__(self):
        return self.name+" "+self.last_name+"("+str(self.pk)+")"
    
    def to_dict(self):
        return {
            "name":self.name,
            "phone":self.phone,
            "email":self.email,
            "id":self.id,
            "state":self.state,
            "is_admin":self.is_admin
        }

class UserAdmin(admin.ModelAdmin):
    list_display=['name','name','last_name','phone']
    search_fields=['name','last_name','phone']

admin.site.register(User,UserAdmin)