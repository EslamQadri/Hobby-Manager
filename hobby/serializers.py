from rest_framework.serializers import ModelSerializer, MultipleChoiceField
from hobby.models import Hobby, HobbyProgress, DAY_CHOICES


class HobbySerializer(ModelSerializer):
    days_of_hobby = MultipleChoiceField(choices=DAY_CHOICES)

    class Meta:
        model = Hobby
        fields = "__all__"


class HobbyProgressSerializer(ModelSerializer):
    class Meta:
        model = HobbyProgress
        fields = "__all__"
