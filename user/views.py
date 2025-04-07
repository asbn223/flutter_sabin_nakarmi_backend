from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from user.serializers import ListUserSerializer
from knox.views import LoginView as KnoxLoginView



# Create your views here.
class LoginView(KnoxLoginView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        # exists = FCMDevice.objects.filter(user__id=user.id).exists()
        # if exists:
        #     if not request.data.get('fcm_id') is None:
        #         device = FCMDevice.objects.get(user__id=user.id)
        #         device.registration_id = request.data.get('fcm_id')
        #         device.save()
        # else:
        #     if not request.data.get('fcm_id') is None:
        #         device = FCMDevice.objects.create(
        #             user=user, registration_id=request.data.get('fcm_id'),
        #         )
        #
        #         device.save()

        login(request, user)
        new_user = ListUserSerializer(user).data
        response = super(LoginView, self).post(request, format=None)
        response.data['user'] = new_user
        return Response(data=response.data, status=200)