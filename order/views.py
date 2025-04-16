from knox.auth import TokenAuthentication
from rest_framework import generics, permissions
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

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)