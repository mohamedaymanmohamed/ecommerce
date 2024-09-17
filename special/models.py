from django.db import models

# Create your models here.


class Specialy(models.Model):
   
    name= models.CharField(max_length=100)
    img= models.ImageField(upload_to='pics')
    des= models.TextField()
    price= models.IntegerField()
    special= models.BooleanField(default=False)