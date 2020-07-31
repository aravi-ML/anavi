from . import views
from django.contrib import admin
from django.urls import path,include
urlpatterns = [
    path('website/',include("website.urls")),
    path("admin/",include("anaviadmin.urls")),
    path('user/',include("anaviuser.urls")),
    path("crwal/",include("crwaling.urls")),
    path("hotel/",include("hotel.urls")),
    path("linguist/",include("anaviexpert.urls")),
    path("comment/",include("comment.urls")),
    path('',views.index,name='home_page'),
    path("error/",include("anavibase.urls")),
    path('djangoadmin/', admin.site.urls),

]
