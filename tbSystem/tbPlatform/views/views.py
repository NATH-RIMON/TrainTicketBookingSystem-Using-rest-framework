from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (ListAPIView,RetrieveAPIView,CreateAPIView,UpdateAPIView
                                     ,DestroyAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView)

from tbPlatform.models.models import Train
from tbPlatform.serializers.serializers import (TrainIdNameSerializers,
                        TrainCreateSerializers,TrainDeleteSerializers)
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from tbcore.permissions.permission import IsSuperUser,StationMasterUserAccess
from django.contrib.auth import get_user_model

User=get_user_model()


class TrainListAPIView(ListAPIView):
    permission_classes=(IsAuthenticated,StationMasterUserAccess)
    queryset=Train.objects.all()
    serializer_class=TrainIdNameSerializers
    lookup_field="id"


class TrainRetrieveAPIView(RetrieveAPIView):
    permission_classes=(IsAuthenticated,)
    queryset=Train.objects.all()
    lookup_field="pk"
    serializer_class=TrainIdNameSerializers

  
class TrainCreateAPIView(CreateAPIView):
    permission_classes=(IsAuthenticated,StationMasterUserAccess)
    queryset=Train.objects.all()
    lookup_field="pk"
    serializer_class=TrainCreateSerializers


class TrainUpdateAPIView(UpdateAPIView):
    permission_classes=(IsAuthenticated,)
    queryset=Train.objects.all()
    lookup_field="pk"
    serializer_class=TrainCreateSerializers

class TrainDestroyAPIView(DestroyAPIView):
    permission_classes=(IsAuthenticated,)
    queryset=Train.objects.all()
    lookup_field="pk"
    serializer_class=TrainDeleteSerializers
