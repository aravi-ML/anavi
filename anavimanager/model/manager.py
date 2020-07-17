from anaviuser.model.user import User
from django.contrib import admin

class Manager(User):
    """ class which represent the hotel manager of our system"""

admin.site.register(Manager)