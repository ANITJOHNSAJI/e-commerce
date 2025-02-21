from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal

class Gallery(models.Model):
    title1 = models.CharField(max_length=100)
    title2 = models.CharField(max_length=100)
    title3 = models.CharField(max_length=100)
    feedimage = models.ImageField(upload_to='gallery_images/')
    quantity = models.IntegerField(default=0)  # Add quantity field to track stock
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Seller user

    def __str__(self):
        return self.title1


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)  

    def __str__(self):
        return f'{self.quantity} of {self.product.title1}'


RuntimeError


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # The seller who will receive the notification
    message = models.TextField()  # The notification message
    timestamp = models.DateTimeField(auto_now_add=True)  # Timestamp when the notification is created

    def __str__(self):
        return f"Notification for {self.user.username} - {self.timestamp}"

