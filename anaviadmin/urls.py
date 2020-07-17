from django.urls import path
from . import views

appname='anaviadmin'
urlpatterns = [
    path("",views.admin_dashboad, name='dashboard')
]
