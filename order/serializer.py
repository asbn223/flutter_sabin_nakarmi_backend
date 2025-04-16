from rest_framework import serializers
from .models import OrderRequest

class OrderRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderRequest
        fields = ['id', 'user', 'product', 'size', 'color', 'requested_at']
        read_only_fields = ['requested_at']
        depth = 2
