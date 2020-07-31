from django.urls import path
from . import views

app_name="anavi"

urlpatterns = [
    path("notfound",views.error_404,name="notfound"),
    path("error500",views.error_500,name="error500"),
    path("emailconfirmcode",views.email_sended,name="email_confirm_code")
]
