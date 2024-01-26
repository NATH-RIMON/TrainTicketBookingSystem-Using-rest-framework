from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (ListAPIView,RetrieveAPIView,CreateAPIView,UpdateAPIView
                                     ,DestroyAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView)

from tbticketService.models.models import TrainJourney
from tbticketService.serializers.serializers import (TrainJourneyIdNameSerializers,
                        TrainJourneyCreateSerializers,TrainJourneyDeleteSerializers)
from tbcore.permissions.permission import IsSuperUser,PassengerUserAccess,StationMasterUserAccess
from django.contrib.auth import get_user_model

User=get_user_model()


class TrainJourneyListAPIView(ListAPIView):
    permission_classes=(IsAuthenticated,IsSuperUser,StationMasterUserAccess,PassengerUserAccess)
    queryset=TrainJourney.objects.all()
    serializer_class=TrainJourneyIdNameSerializers
    lookup_field="id"


class TrainJourneyRetrieveAPIView(RetrieveAPIView):
    permission_classes=(IsAuthenticated,PassengerUserAccess)
    queryset=TrainJourney.objects.all()
    lookup_field="pk"
    serializer_class=TrainJourneyIdNameSerializers

  
class TrainJourneyCreateAPIView(CreateAPIView):
    permission_classes=(IsAuthenticated,PassengerUserAccess)
    queryset=TrainJourney.objects.all()
    lookup_field="pk"
    serializer_class=TrainJourneyCreateSerializers


class TrainJourneyUpdateAPIView(UpdateAPIView):
    permission_classes=(IsAuthenticated,PassengerUserAccess)
    queryset=TrainJourney.objects.all()
    lookup_field="pk"
    serializer_class=TrainJourneyCreateSerializers

class TrainJourneyDestroyAPIView(DestroyAPIView):
    permission_classes=(IsAuthenticated,IsSuperUser)
    queryset=TrainJourney.objects.all()
    lookup_field="pk"
    serializer_class=TrainJourneyDeleteSerializers