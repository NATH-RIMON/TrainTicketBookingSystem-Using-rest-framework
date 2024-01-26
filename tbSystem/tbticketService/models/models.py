from django.db import models
from django.contrib.auth import get_user_model
from tbcore.models.models import BaseTimeStampedModel
from tstation.models.models import TrainStation
from tbPlatform.models.models import Train


User = get_user_model()

class TrainJourney(BaseTimeStampedModel):
    passenger = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,related_name="passenger")
    start_station = models.ForeignKey(
        TrainStation, on_delete=models.CASCADE,blank=False, related_name='trains_starting_here')
    
    end_station = models.ForeignKey(
    TrainStation, on_delete=models.CASCADE, blank=False, related_name='trains_stop_here')
    train=models.ForeignKey(Train,on_delete=models.CASCADE,blank=False, related_name='Train_name')
    seat_number = models.PositiveIntegerField(blank=False,unique=True)
    


    class Meta:    
        constraints=[
            models.UniqueConstraint(fields=['train','start_station','end_station',],
                                  name='journey_start_from_end',),
        ]

    def __str__(self):
        return self.passenger.username