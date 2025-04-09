from django.contrib import admin

# Register your models here.
# Register your models here.
from .models import Quote, OrderTracking, Order, Budget

# Register your models here.
admin.site.register(Quote)
admin.site.register(Order)
admin.site.register(OrderTracking)
admin.site.register(Budget)