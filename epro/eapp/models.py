from django.db import models

# Create your models here.
class Formdata(models.Model):
    feed=models.CharField(max_length=100)
