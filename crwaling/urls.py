
from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="crwallerhome"),
    path("<slug:hotel>",views.crwal,name="crwal_from_website")
]
