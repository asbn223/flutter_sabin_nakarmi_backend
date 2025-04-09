import uuid

from django.db import models


# Create your models here.
class Quote(models.Model):
    value = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Quote - ${self.value}"

class Order(models.Model):
    value = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order - ${self.value}"

class Budget(models.Model):
    month = models.CharField(max_length=20)
    total_budget = models.DecimalField(max_digits=10, decimal_places=2)
    spent = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def remaining(self):
        return self.total_budget - self.spent

    def __str__(self):
        return f"{self.month} Budget"

class OrderTracking(models.Model):
    order_id = models.CharField(max_length=100, unique=True, default=uuid.uuid4)
    from_address = models.CharField(max_length=255)
    to_address = models.CharField(max_length=255)
    current_status = models.CharField(max_length=255)
    current_location_lat = models.FloatField()
    current_location_lon = models.FloatField()

    def __str__(self):
        return f"Tracking for {self.order_id}"

