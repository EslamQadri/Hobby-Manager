from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from hobby.models import Hobby, HobbyProgress
from hobby.serializers import HobbySerializer, HobbyProgressSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class HobbyViwe(RetrieveUpdateDestroyAPIView):
    serializer_class = HobbySerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        return Hobby.objects.filter(user=self.request.user)


class CreateHobby(ListCreateAPIView):
    serializer_class = HobbySerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        return Hobby.objects.filter(user=self.request.user)


class HobbyProgressViwe(RetrieveUpdateDestroyAPIView):
    serializer_class = HobbyProgressSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        return HobbyProgress.objects.filter(hobby__user=self.request.user)


class CreateHobbyProgress(ListCreateAPIView):
    serializer_class = HobbyProgressSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        return HobbyProgress.objects.filter(hobby__user=self.request.user)
