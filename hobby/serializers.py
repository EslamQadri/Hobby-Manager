from rest_framework.serializers import ModelSerializer
from hobby.models import Hobby, HobbyProgress


class HobbySerializer(ModelSerializer):
    class Meta:
        model = Hobby
        exclude = ["user"]


class HobbyProgressSerializer(ModelSerializer):
    class Meta:
        model = HobbyProgress
        fields = "__all__"
