from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Phones,PhoneAdmin)
admin.site.register(Emails,EmailAdmin)