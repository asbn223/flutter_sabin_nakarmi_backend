from knox.auth import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from metric.models import Quote, Budget, OrderTracking, Order
from metric.serializers import QuoteSerializer, BudgetSerializer, OrderSerializer, OrderTrackingSerializer


# Create your views here.
class MetricViewSet(ModelViewSet):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, ]

    def list(self, request, *args, **kwargs):
        quote = Quote.objects.all()
        quote_data = QuoteSerializer(quote, many=True)

        budget = Budget.objects.all()
        budget_data = BudgetSerializer(budget, many=True)

        order = Order.objects.all()
        order_data = OrderSerializer(order, many=True)

        order_tracking = OrderTracking.objects.all()
        order_tracking_data = OrderTrackingSerializer(order_tracking, many=True)

        return Response(data={
            'quote': quote_data.data,
            'budget': budget_data.data,
            'order': order_data.data,
            'order_tracking': order_tracking_data.data
        }, status=200)

