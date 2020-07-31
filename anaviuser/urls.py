from django.urls import path
from . import views,user_api


app_name= "anaviuser"
urlpatterns = [
    path('login',views.login,name="login"),
    path('signup',views.signup, name="signup"),
    path('reinitialiser_pwd', views.reinitialiser,name="reinitialize"),
    path('reinitialize_mail',views.reinitialise_mail,name="reinitialze_mail"),
    path('reinitialise_code',views.reinitialise_code,name="reinitialise_code")
]
