from django.urls import path
from . import views,user_api

app_name="anaviuser"
urlpatterns = [
    path('login',views.login,name="login"),
    path("performlogin",user_api.login,name="performlogin")
]
