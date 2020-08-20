from django.urls import path
from . import views, admin_api

app_name='anaviadmin'
urlpatterns = [
    path("",views.admin_dashboad, name='dashboard'),
    path("download",views.download,name='download'),
    path("pdownload",admin_api.download_data,name="pdownload")
]
