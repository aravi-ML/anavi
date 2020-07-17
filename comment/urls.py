from django.urls import path
from . import views


appname="comment"

urlpatterns = [
    path('tagcomment',views.tag_data,name="tagdata")
]
