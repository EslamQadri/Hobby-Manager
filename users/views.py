from rest_framework import generics, permissions
from django.contrib.auth.models import User
from rest_framework.response import Response
from users.serializers import UserSerializer
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken


class UserLogin(generics.CreateAPIView):
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        data = request.data
        username = data.get("username", None)
        password = data.get("password", None)

        if username is None or password is None:
            return Response(
                {"error": "Please provide both username and password."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user = User.objects.filter(username=username).first()

        if user is None or not user.check_password(password):
            return Response(
                {"error": "Invalid username or password."},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        refresh = RefreshToken.for_user(user)
        return Response(
            {"access_token": str(refresh.access_token), "refresh_token": str(refresh)},
            status=status.HTTP_200_OK,
        )


class UserSignup(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)


class UserLogout:
    pass
