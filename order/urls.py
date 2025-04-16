from django.urls import path
from .views import OrderRequestCreateView, OrderRequestListView

urlpatterns = [
    path('send-order-request/', OrderRequestCreateView.as_view(), name='order-request'),
    path('order-requests/', OrderRequestListView.as_view(), name='order-request-list'),
]
