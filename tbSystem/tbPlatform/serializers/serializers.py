from rest_framework.serializers import ModelSerializer
from tbPlatform.models.models import Train
from rest_framework.validators import UniqueTogetherValidator
from django.contrib.auth import get_user_model

User=get_user_model()

class TrainIdNameSerializers(ModelSerializer):
    class Meta:
        model=Train
        fields="__all__"

class TrainCreateSerializers(ModelSerializer):

    class Meta:
        model=Train
        fields="__all__"
        validators = [
            UniqueTogetherValidator(
            queryset=Train.objects.all(),
            fields=['name','station_master','class_status','schedule','departure_time','plat_form',]
            )
        ]


class TrainDeleteSerializers(ModelSerializer):

    class Meta:
        model=Train
        fields=("name",)
    

