from django.urls import path
from . import views
app_name="countryapp"

urlpatterns = [
    path("get-country-cities",views.get_town_of_country,name="cities-of-country")
]
