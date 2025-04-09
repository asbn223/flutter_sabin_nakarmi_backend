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
        total_quote = 0
        quote = Quote.objects.all()
        for q in quote:
            total_quote += q.value
        quote_data = QuoteSerializer(quote, many=True)


        budget = Budget.objects.all()
        budget_data = BudgetSerializer(budget, many=True)

        total_order = 0
        order = Order.objects.all()
        for o in order:
            total_order += o.value
        order_data = OrderSerializer(order, many=True)

        order_tracking = OrderTracking.objects.all()
        order_tracking_data = OrderTrackingSerializer(order_tracking, many=True)

        return Response(data={
            'quote': quote_data.data,
            'total_quote': total_quote,
            'budget': budget_data.data,
            'order': order_data.data,
            'total_order': total_order,
            'order_tracking': order_tracking_data.data
        }, status=200)

