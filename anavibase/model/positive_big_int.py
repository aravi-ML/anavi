from django.db import models

class PositiveAutoBigInt(models.BigAutoField):
    description="return and usnigend big int class"
    
    def db_type(self,connection):
        return "BIGINT UNSIGNED AUTO_INCREMENT"
    def rel_db_type(self,connection):
        return "BIGINT UNSIGNED"