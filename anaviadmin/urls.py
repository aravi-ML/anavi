from django.urls import path
from . import views, admin_api

app_name='anaviadmin'
urlpatterns = [
    path("",views.admin_dashboad, name='dashboard'),
    path("download",views.download,name='download'),
    path("pdownload",admin_api.download_data,name="pdownload"),
    path("askmanaging",views.ask_managing_list,name="askmanaging"),
    path("paskmanaging",admin_api.perfom_decision_ask_managing,name="paskmanaging")
]
