from rest_framework.serializers import ModelSerializer
from tbticketService.models.models import TrainJourney
from rest_framework.validators import UniqueTogetherValidator
from django.contrib.auth import get_user_model

User=get_user_model()

class TrainJourneyIdNameSerializers(ModelSerializer):
    class Meta:
        model=TrainJourney
        fields="__all__"


class TrainJourneyCreateSerializers(ModelSerializer):

    class Meta:
        model=TrainJourney
        fields="__all__"
        validators = [
            UniqueTogetherValidator(
            queryset=TrainJourney.objects.all(),
            fields=['passenger','start_station','end_station','train','seat_number',]
            )
        ]


class TrainJourneyDeleteSerializers(ModelSerializer):

    class Meta:
        model=TrainJourney
        fields=("passenger",)

