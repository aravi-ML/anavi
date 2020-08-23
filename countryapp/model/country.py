from django.db import models

class Country(models.Model):
    code =models.CharField(max_length=20)
    phone_code=models.CharField(max_length=20,null=True,blank=True)
    alpha2=models.CharField(max_length=4,null=True,default="",blank=True)
    alpha3=models.CharField(max_length=4,null=True,default="",blank=True)
    name_en=models.CharField(max_length=100)
    name_fr=models.CharField(max_length=100)
