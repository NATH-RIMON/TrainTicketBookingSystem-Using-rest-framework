from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (ListAPIView,RetrieveAPIView,CreateAPIView,UpdateAPIView
                                     ,DestroyAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView)

from tstation.models.models import TrainStation
from tstation.serializers.serializers import (TrainStationIdNameSerializers,
                        TrainStationCreateSerializers,TrainStationDeleteSerializers)
from tbcore.permissions.permission import IsSuperUser
from django.contrib.auth import get_user_model

User=get_user_model()

class TrainStationListAPIView(ListAPIView):
    permission_classes=(IsAuthenticated,IsSuperUser)
    queryset=TrainStation.objects.all()
    serializer_class=TrainStationIdNameSerializers
    lookup_field="id"


class TrainStationRetrieveAPIView(RetrieveAPIView):
    permission_classes=(IsAuthenticated,IsSuperUser)
    queryset=TrainStation.objects.all()
    lookup_field="pk"
    serializer_class=TrainStationIdNameSerializers

  
class TrainStationCreateAPIView(CreateAPIView):
    permission_classes=(IsAuthenticated,IsSuperUser)
    queryset=TrainStation.objects.all()
    lookup_field="pk"
    serializer_class=TrainStationCreateSerializers


class TrainStationUpdateAPIView(UpdateAPIView):
    permission_classes=(IsAuthenticated,IsSuperUser)
    queryset=TrainStation.objects.all()
    lookup_field="pk"
    serializer_class=TrainStationCreateSerializers

class TrainStationDestroyAPIView(DestroyAPIView):
    permission_classes=(IsAuthenticated,IsSuperUser)
    queryset=TrainStation.objects.all()
    lookup_field="pk"
    serializer_class=TrainStationDeleteSerializers
