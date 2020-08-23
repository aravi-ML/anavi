from django.db import models
from .country import Country

class City(models.Model):
    country=models.ForeignKey(Country,on_delete=models.CASCADE,default=None,null=True,blank=True)
    name = models.CharField(max_length=200)
    name_fr=models.CharField(max_length=200,null=True,blank=True,default=None)
    name_en=models.CharField(max_length=200,null=True,blank=True,default=None)

    def to_dict(self):
        return {
            "name":self.name,
            "name_fr":self.name_fr,
            "name_en":self.name_en,
            "id":self.id,
            "country":self.country.id
        }
