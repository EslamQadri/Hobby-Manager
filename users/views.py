from rest_framework import generics, permissions

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from users.serializers import UserSerializer, UserLoginSerializer

"""
i know i implementing a poor auth
"""


class UserLogin(generics.CreateAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key})


class UserSignup(generics.CreateAPIView):
    serializer_class = UserSerializer


class UserLogout:
    pass
