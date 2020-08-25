from django.db import models
from django.contrib import admin
from anaviuser.model.user import User
from hotel.model.hotel import Hotel

class AskExpert(models.Model):
    """
        That model is for allows user ask become an exeprt language of in our website
    """
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    add_date=models.DateTimeField(auto_now_add=True)
    decision_by=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True,related_name="exepert_decision_by")
    language=models.CharField(max_length=255)
    state=models.BooleanField(default=False)

    def user_inf(self):
        return {
            "name":self.user.name,
            "phone":self.user.phone,
            "email":self.user.email,
            "id":self.user.id,
            "state":self.user.state,
            "is_admin":self.user.is_admin
        }
    def decision_by_inf(self):
        return {
            "name":self.decision_by.name,
            "phone":self.decision_by.phone,
            "email":self.decision_by.email,
            "id":self.decision_by.id,
            "state":self.decision_by.state,
            "is_admin":self.decision_by.is_admin
        }

class AskExpertAdmin(admin.ModelAdmin):
    list_display=["user","language","state","add_date","decision_by"]
    search_fields=["user","language","decision_by","add_date"]

admin.site.register(AskExpert,AskExpertAdmin)
