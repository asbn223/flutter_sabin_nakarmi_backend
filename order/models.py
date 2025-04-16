import uuid

from django.db import models

from product.models import Product
from user.models import User


# Create your models here.
class OrderRequest(models.Model):

    SIZE_CHOICES = [
        ('S', 'Small'), ('M', 'Medium'), ('L', 'Large'),
        ('XL', 'Extra Large'), ('2XL', '2XL'),
        ('3XL', '3XL'), ('4XL', '4XL')
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.CharField(max_length=4, choices=SIZE_CHOICES)
    color = models.CharField(max_length=20,)
    requested_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.product.name} - {self.size} - {self.color}"