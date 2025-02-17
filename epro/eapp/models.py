from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal

class Gallery(models.Model):
    feedimage = models.ImageField(upload_to='gallery_images/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title1 = models.CharField(max_length=100)
    title2 = models.CharField(max_length=100)
    title3 = models.CharField(max_length=100)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title1

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)  

    def __str__(self):
        return f'{self.quantity} of {self.product.title1}'


RuntimeError

