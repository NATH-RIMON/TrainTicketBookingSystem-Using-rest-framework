from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model
# from tbauth.models.models import StationMasterUser,PassengerUser


User=get_user_model()

class UserNameEmailSerializers(ModelSerializer):
    
    class Meta:
        model=User
        fields=("id","username","email")



