from django.urls import path
from tbticketService.views.views import (TrainJourneyListAPIView,TrainJourneyRetrieveAPIView,TrainJourneyCreateAPIView,
            TrainJourneyUpdateAPIView,TrainJourneyDestroyAPIView,)



urlpatterns=[
    path("train-journey/",TrainJourneyListAPIView.as_view(),name="journey_list"),
    path("train-journey-details/<int:pk>/",TrainJourneyRetrieveAPIView.as_view(),name="journey_details"),
    path("train-journey-create/",TrainJourneyCreateAPIView.as_view(),name="journey_create"),
    path("train-journey-update/<int:pk>/",TrainJourneyUpdateAPIView.as_view(),name="journey_update"),
    path("journey-delete/<int:pk>/",TrainJourneyDestroyAPIView.as_view(),name="journey_delete"),
]