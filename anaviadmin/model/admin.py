from anaviuser.model.user import User
from django.contrib import admin

class Admin(User):
    """ class which represent the admin of our system"""

admin.site.register(Admin)