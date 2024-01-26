from django.db import models
from django.contrib.auth import get_user_model
from tbcore.models.models import BaseTimeStampedModel


User = get_user_model()


class TrainStation(BaseTimeStampedModel):
    name = models.CharField(max_length=512, unique=True,blank=False)
    details= models.TextField(blank=True)
    created_by=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True,
                                      related_name="railway_authority")
    
    def __str__(self):
        return self.name
        

