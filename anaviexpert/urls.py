from django.urls import path
from . import views

appname="expert"
urlpatterns = [
    path("tagdata",views.tag_data,name="tag_data")
]
