from . import views
from django.contrib import admin
from django.urls import path,include
app_name = "anavi"
urlpatterns = [
    path('website/',include("website.urls")),
    path("admin/",include("anaviadmin.urls")),
    path('user/',include("anaviuser.urls")),
    path("crwal/",include("crwaling.urls")),
    path("hotel/",include("hotel.urls")),
    path("expert/",include("anaviexpert.urls")),
    path("comment/",include("comment.urls")),
    path('',views.index,name='home'),
    path("error/",include("anavibase.urls")),
    path("manager/",include("anavimanager.urls")),
    path("country/",include("countryapp.urls")),
    path('djangoadmin/', admin.site.urls),

]
