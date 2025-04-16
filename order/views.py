from knox.auth import TokenAuthentication
from rest_framework import generics, permissions
from rest_framework.response import Response

from product.models import Product
from .models import OrderRequest
from .serializer import OrderRequestSerializer

class OrderRequestListView(generics.ListAPIView):
    serializer_class = OrderRequestSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (TokenAuthentication, )

    def get_queryset(self):
        if self.request.user.is_admin:
            return OrderRequest.objects.all().order_by('-requested_at')
        return OrderRequest.objects.filter(user=self.request.user).order_by('-requested_at')

class OrderRequestCreateView(generics.CreateAPIView):
    queryset = OrderRequest.objects.all()
    serializer_class = OrderRequestSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (TokenAuthentication,)

    def create(self, request, *args, **kwargs):
        data = request.data
        size = data.get('size')
        color = data.get('color')
        product_id = data.get('product')
        user = request.user

        try:
            product_exists = Product.objects.filter(id=product_id).exists()

            if product_exists:
                product = Product.objects.get(id=product_id)

                OrderRequest.objects.create(user=user, product=product, size=size, color=color)

                return Response(
                    data=
                    {
                        'message': 'Order request has been sent successfully',
                    },
                    status=201
                )

            else:
                return Response(
                    data=
                    {
                        'message': 'Product not found'
                    },
                    status=404
                )

        except Exception as e:
            return Response(
                data=
                {
                'message': 'Order request cannot be sent'
            },
                status=400
            )
