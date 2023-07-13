from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from hobby.models import Hobby, HobbyProgress
from hobby.serializers import HobbySerializer, HobbyProgressSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
import drf_yasg


from drf_yasg import openapi


class HobbyViwe(RetrieveUpdateDestroyAPIView):
    serializer_class = HobbySerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        return Hobby.objects.filter(user=self.request.user)

    def delete(self, request, *args, **kwargs):
        request.data["user"] = self.request.user.id
        return super().delete(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        request.data["user"] = self.request.user.id
        return super().update(request, *args, **kwargs)


class CreateHobby(ListCreateAPIView):
    serializer_class = HobbySerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        return Hobby.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        request.data["user"] = self.request.user.id
        return super().create(request, *args, **kwargs)


class HobbyProgressViwe(RetrieveUpdateDestroyAPIView):
    serializer_class = HobbyProgressSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        return HobbyProgress.objects.filter(hobby__user=self.request.user)

    def delete(self, request, *args, **kwargs):
        request.data["user"] = self.request.user.id
        return super().delete(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        request.data["user"] = self.request.user.id
        return super().update(request, *args, **kwargs)


class CreateHobbyProgress(ListCreateAPIView):
    serializer_class = HobbyProgressSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        return HobbyProgress.objects.filter(hobby__user=self.request.user)

    def create(self, request, *args, **kwargs):
        request.data["user"] = self.request.user.id
        return super().create(request, *args, **kwargs)
