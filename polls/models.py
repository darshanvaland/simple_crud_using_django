from django.db import models

# Create your models here.
class crate(models.Model):
    name=models.CharField(max_length=100)
    mobile = models.IntegerField(max_length=10,default=0)
    email = models.CharField(max_length=100)
    birth=models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.name
