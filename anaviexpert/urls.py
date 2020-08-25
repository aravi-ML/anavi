from django.urls import path
from . import views,expert_api

app_name="expert"
urlpatterns = [
    path("tagdata",views.tag_data,name="tag_data"),
    path("expert-space",views.expert_space,name="space"),
    path("paskexepert",expert_api.perform_ask_exepert,name="paskexepert"),
    path("decideapply",expert_api.decide_apply_expert_demand,name="decideapply")
]
