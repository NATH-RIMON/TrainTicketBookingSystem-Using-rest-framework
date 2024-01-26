from django.db import models
from django.contrib.auth import get_user_model
from tbcore.models.models import BaseTimeStampedModel


User = get_user_model()


class Train(BaseTimeStampedModel):
    name= models.CharField(max_length=512, unique=True,blank=False)
    CLASS_CHOICES_OPTION = (
        ("First", "First Class"),
        ("Second", "Second Class"),
        ("Economy", "Economy Class"),
    )
    station_master=models.ManyToManyField(User,blank=True,related_name="station_master")
    class_status=models.CharField(max_length=20,choices=CLASS_CHOICES_OPTION,default="First")
    schedule = models.DateField()
    departure_time = models.TimeField(unique=True)
    plat_form = models.PositiveIntegerField()
    def __str__(self):
        return self.name

