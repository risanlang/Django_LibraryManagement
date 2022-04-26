from django.db import models

# Create your models here.
class Book(models.Model):
    bname=models.CharField(max_length=70,blank=False,default='')
    author=models.CharField(max_length=100,blank=False,default='')
    description=models.CharField(max_length=200,blank=False,default='')
    price=models.CharField(max_length=30,default='')
    
    def __str__(self) -> str:
        return self.name