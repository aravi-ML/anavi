from django.urls import path
from . import views

appname="hotel"
urlpatterns = [
     path("dashboard/<int:pk>",views.dashboard,name='dashboard')
 ]
 