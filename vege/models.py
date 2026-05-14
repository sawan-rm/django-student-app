from django.db import models

# Create your models here.
class Recepie(models.Model):
    receipe_name=models.CharField(max_length=100)
    receipe_descrioption=models.TextField()
    receipe_img = models.ImageField(upload_to='receipe')
    