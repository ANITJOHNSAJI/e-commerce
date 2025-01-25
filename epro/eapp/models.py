from django.db import models
from django.contrib.auth.models import User
class Gallery(models.Model):
    feedimage=models.ImageField(upload_to='gallery_images/')
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title1=models.CharField(max_length=100)
    title2=models.CharField(max_length=100)
    title3=models.CharField(max_length=100)