from django.db import models
from django.contrib import admin


class Polarity(models.Model):
    """here we save different polarity from who will be used on 
    the aspect polarity"""
    name=models.TextField(max_length=255)
    status=models.BooleanField(default=True)
    add_date=models.DateTimeField(auto_now_add=True)

class PolarityAdmin(admin.ModelAdmin):
    list_display=['name','status','add_date']
    search_fields=['name','status','add_date']

admin.site.register(Polarity,PolarityAdmin)