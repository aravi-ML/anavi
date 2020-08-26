from django.urls import path
from . import views,hotel_api

app_name="hotel"
urlpatterns = [
     path("dashboard/<slug:token>",views.dashboard,name='dashboard'),
     path("add-user",views.hotel_add_user_side,name="addfromuser"),
     path("perfom-add-from-user",hotel_api.add_from_user,name="paddfromuser"),
     path("akhotelstat/<slug:token>",hotel_api.get_hotel_stat,name="hotelstat")
 ]
 