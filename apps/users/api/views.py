from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string
from django.conf import settings
from django.core.mail import send_mail

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, status
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework.exceptions import ValidationError

from apps.users.models import User
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer

RESET_TOKENS = {}  # In-memory. Use Redis or DB for production.

class ForgotPasswordView(APIView):

    def post(self, request):
        email = request.data.get("email")
        try:
            user = get_user_model().objects.get(email=email)
            token = get_random_string(length=32)
            self.RESET_TOKENS[token] = user.id
            reset_link = f"http://localhost:8000/api/v1/users/reset-password/?token={token}"
            send_mail(
                "Reset Your Password",
                f"Click here to reset your password: {reset_link}",
                settings.DEFAULT_FROM_EMAIL,
                [email],
            )
            return Response({'detail': 'Reset email sent'})
        except get_user_model().DoesNotExist:
            return Response({'error': 'User not found'}, status=404)


class ResetPasswordView(APIView):
    def post(self, request):
        token = request.GET.get("token")
        new_password = request.data.get("password")
        user_id = RESET_TOKENS.get(token)
        if not user_id:
            return Response({'error': 'Invalid token'}, status=400)
        user = get_user_model().objects.get(id=user_id)
        user.set_password(new_password)
        user.save()
        del RESET_TOKENS[token]
        return Response({'detail': 'Password reset successful'})


class VerifyEmailView(APIView):
    def get(self, request):
        token = request.GET.get("token")
        try:
            access_token = AccessToken(token)
            user_id = access_token['user_id']
            user = get_user_model().objects.get(id=user_id)
            if user.is_verified:
                return Response({'detail': 'Already verified.'})
            user.is_verified = True
            user.save()
            return Response({'detail': 'Email verified successfully.'})
        except Exception as e:
            raise ValidationError("Invalid or expired token.")


class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'user': UserSerializer(user).data,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            refresh = RefreshToken.for_user(user)
            return Response({
                'user': UserSerializer(user).data,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


class ListUsers(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    # authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    # permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)
