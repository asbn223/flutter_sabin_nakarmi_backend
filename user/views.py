from django.contrib.auth import login
from django.contrib.auth.hashers import make_password, check_password
from django.core.cache import cache
from django.utils.crypto import get_random_string
from knox.auth import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from main_utils.email_utils import send_account_forgot_password_email
from user.models import User
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


class ForgotPasswordView(APIView):
    def post(self, request):
        email = request.data.get('email')

        if not email:
            return Response({"error": "Email is required"}, status=400)

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({"error": "User with this email does not exist"}, status=400)

        # Generate OTP
        otp = get_random_string(length=6, allowed_chars='0123456789')

        cache.set(f'password_reset_{user.id}', otp, timeout=600)

        send_account_forgot_password_email(user=user, otp=otp)

        # Save OTP to user model or session for validation
        # Alternatively, use Django’s caching mechanism for short-lived OTP storage

        return Response({"message": "OTP sent to your email"}, status=200)


class ResetPasswordView(APIView):
    def post(self, request):
        email = request.data.get('email')
        otp = request.data.get('otp')
        new_password = request.data.get('new_password')

        if not email or not otp or not new_password:
            return Response({"error": "Email, OTP, and new password are required"},
                            status=400)

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({"error": "User with this email does not exist"}, status=400)

        # Retrieve the OTP from cache
        stored_otp = cache.get(f'password_reset_{user.id}')

        if stored_otp != otp:
            return Response({"error": "Invalid OTP"}, status=400)
        else:

            # Set the new password
            user.password = make_password(new_password)
            user.save()

            # Delete OTP from cache (it's no longer needed)
            cache.delete(f'password_reset_{user.id}')

            return Response({"message": "Password reset successfully"}, status=200)


class ProfileView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get(self, request, *args, **kwargs):
        user = self.request.user

        user_data = ListUserSerializer(user)

        return Response(user_data.data)


class ChangePasswordAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        current_password = request.data.get('current_password')
        new_password = request.data.get('new_password')
        confirm_password = request.data.get('confirm_password')

        # Validate required fields
        if not current_password or not new_password or not confirm_password:
            return Response(
                {"error": "All fields are required."},
                status=400,
            )

        # Check if current password matches
        if not check_password(current_password, user.password):
            return Response(
                {"error": "Current password is incorrect."},
                status=400
            )

        # Check if new password matches confirmation
        if new_password != confirm_password:
            return Response(
                {"error": "New password and confirm password do not match."},
                status=400
            )

        # Check if new password is same as old password
        if check_password(new_password, user.password):
            return Response(
                {"error": "New password cannot be the same as the old password."},
                status=400
            )

        # Change the password
        user.password = make_password(new_password)
        user.save()

        return Response(
            {"message": "Password changed successfully."},
            status=200
        )
