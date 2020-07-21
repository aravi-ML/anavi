from django.db import models
from django.contrib import admin
from .aspect import Aspect
from .polarity import Polarity
from anaviexpert.model.expert import Expert
from anavibase.model.positive_big_int import *
class AspectPolarity(models.Model):
    """That class is to mark some anotation make by user
        For example user can take some aspect and gave positive or negative or neutral
    """
    id=PositiveAutoBigInt(primary_key=True)
    aspect=models.ForeignKey(Aspect,on_delete=models.CASCADE)
    polarity=models.ForeignKey(Polarity,on_delete=models.CASCADE)
    expert=models.ForeignKey(Expert,on_delete=models.SET_NULL,null=True,blank=True)
    add_date=models.DateTimeField(auto_now=True)
    status=models.BooleanField(default=True)

class AspectPolarityAdmin(admin.ModelAdmin):
    list_display=["aspect","polarity","expert","add_date"]
    search_fields=["aspect","polarity","expert","add_date"]

admin.site.register(AspectPolarity,AspectPolarityAdmin)