from anaviuser.model.user import User
from django.contrib import admin

class Searcher(User):
    """ class which represent the searcher of our system"""

admin.site.register(Searcher)