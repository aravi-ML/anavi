from anaviuser.model.user import User
from django.contrib import admin
class Expert(User):
    """ class which represent the Expert (the person who add label to world) of our system"""


admin.site.register(Expert)