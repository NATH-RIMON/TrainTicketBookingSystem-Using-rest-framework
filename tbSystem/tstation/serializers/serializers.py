from rest_framework.serializers import ModelSerializer
from tstation.models.models import TrainStation
from rest_framework.validators import UniqueTogetherValidator
from django.contrib.auth import get_user_model

User=get_user_model()

class TrainStationIdNameSerializers(ModelSerializer):
    class Meta:
        model=TrainStation
        fields="__all__"

class TrainStationCreateSerializers(ModelSerializer):

    class Meta:
        model=TrainStation
        fields="__all__"
        validators = [
            UniqueTogetherValidator(
            queryset=TrainStation.objects.all(),
            fields=['name', 'details', 'created_by',]
            )
        ]

class TrainStationDeleteSerializers(ModelSerializer):

    class Meta:
        model=TrainStation
        fields=("status",)
    

