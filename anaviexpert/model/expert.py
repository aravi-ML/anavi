from django.db import models
from anaviuser.model.user import User
from django.contrib import admin
class Expert(models.Model):
    """ class which represent the Expert (the person who add label to world) of our system"""
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    add_date=models.DateTimeField(auto_now_add=True)
    state=models.BooleanField(default=True)
    add_by=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name="expert_add_by")
    
    def user_inf(self):
        return {
            "name":self.user.name,
            "phone":self.user.phone,
            "email":self.user.email,
            "id":self.user.id,
            "state":self.user.state,
            "is_admin":self.user.is_admin
        }

admin.site.register(Expert)