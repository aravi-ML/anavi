from django.urls import path
from . import views,user_api


app_name= "anaviuser"
urlpatterns = [
    path('login',views.login,name="login"),
    path("logout",views.logout,name="logout"),
    path("performlogin",user_api.login,name="plogin"),
    path('signup',views.signup, name="signup"),
    path('login',views.login,name="userlogin"),
    path('signup_ok',user_api.addUser,name="Psignup"),
    path('signup',views.signup, name="userSignup"),
    path('reinitialiser_pwd', views.reinitialiser,name="Reinitialize"),
    path('reinitialize_mail',views.reinitialise_mail,name="Reinitialze_mail"),
    path('reinitialise_code',views.reinitialise_code,name="Reinitialise_code"),
    path("performpaswordreset",user_api.perform_change_password,name="ppasswordchange")
]
