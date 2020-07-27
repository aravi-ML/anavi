from django.urls import path
from . import views,comment_api


app_name="comment"

urlpatterns = [
    path('tagcomment',views.tag_data,name="tagdata"),
    path("performtagcomment",comment_api.tag_comment,name="performtagcomment")
]
