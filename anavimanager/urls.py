from django.urls import path
from . import views,manager_api

app_name="amanager"

urlpatterns = [
    path("my-manage-space",views.manager_space,name="managespace"),
    path("perform-ask-managing",manager_api.perform_ask_manage,name="paskmanage")
]
