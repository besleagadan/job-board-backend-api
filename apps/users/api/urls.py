from django.urls import path, include

from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from .views import (
    ListUsers,
    RegisterView,
    LoginView,
    ProfileView,
    VerifyEmailView,
    ForgotPasswordView,
    ResetPasswordView

)

app_name = "user"

urlpatterns = [
    path("", ListUsers.as_view(), name="list_users"),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('verify/', VerifyEmailView.as_view(), name='verify-email'),
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot-password'),
    path('reset-password/', ResetPasswordView.as_view(), name='reset-password'),
]
