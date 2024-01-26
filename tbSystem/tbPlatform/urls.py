from django.urls import path
from tbPlatform.views.views import (TrainListAPIView,TrainRetrieveAPIView,TrainCreateAPIView,
            TrainUpdateAPIView,TrainDestroyAPIView,)


urlpatterns=[
    path("train/",TrainListAPIView.as_view(),name="train_list"),
    path("train-details/<int:pk>/",TrainRetrieveAPIView.as_view(),name="train_details"),
    path("train-create/",TrainCreateAPIView.as_view(),name="train_create"),
    path("train-update/<int:pk>/",TrainUpdateAPIView.as_view(),name="train_update"),
    path("train-delete/<int:pk>/",TrainDestroyAPIView.as_view(),name="train_delete"),
]
