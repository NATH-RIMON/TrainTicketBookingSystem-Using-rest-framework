from django.urls import path
from tstation.views.views import (TrainStationListAPIView,TrainStationRetrieveAPIView,TrainStationCreateAPIView,
            TrainStationUpdateAPIView,TrainStationDestroyAPIView,)



urlpatterns=[
    path("train-station/",TrainStationListAPIView.as_view(),name="station_list"),
    path("train-station-details/<int:pk>/",TrainStationRetrieveAPIView.as_view(),name="station_details"),
    path("train-station-create/",TrainStationCreateAPIView.as_view(),name="station_create"),
    path("train-station-update/<int:pk>/",TrainStationUpdateAPIView.as_view(),name="station_update"),
    path("station-delete/<int:pk>/",TrainStationDestroyAPIView.as_view(),name="station_delete"),
]