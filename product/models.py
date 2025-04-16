import uuid

from django.db import models

# Create your models here.
class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    variants = models.JSONField(default=dict)  # {'colors': [...], 'sizes': [...]}
    budget_info = models.JSONField(default=dict)
    specifications = models.JSONField(default=dict)
    materials = models.TextField()
    images = models.JSONField(default=list)  # List of image URLs

    def __str__(self):
        return self.name
