from django.db import models
from django.contrib import admin
from anaviuser.model.user import User
from hotel.model.hotel import Hotel

class AskManage(models.Model):
    """
        That model is for allows user ask managemenet of one hotel 
        User can ask they management of many Hotel
    """
    hotel=models.ForeignKey(Hotel,on_delete=models.SET_NULL,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    add_date=models.DateTimeField(auto_now_add=True)
    decision_by=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True,related_name="decision_by")
    state=models.BooleanField(default=False)

class AskManageAdmin(admin.ModelAdmin):
    list_display=["hotel","user","state","add_date","decision_by"]
    search_fields=["hotel","user","decision_by","add_date"]

admin.site.register(AskManage,AskManageAdmin)
