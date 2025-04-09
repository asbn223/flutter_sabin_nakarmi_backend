from django.urls import path
from knox import views as knox_views

from user.views import LoginView, ForgotPasswordView, ResetPasswordView, ChangePasswordAPIView

app_name = 'user'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('forgot_password/', ForgotPasswordView.as_view(), name='forgot_password'),
    path('reset_password/', ResetPasswordView.as_view(), name='reset_password'),
    path('change_password/', ChangePasswordAPIView.as_view(), name='change_password'),
]
