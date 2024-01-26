from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from tbcore.models.models import *

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class UserProfile(BaseTimeStampedModel):
    ROLE_OPTIONS=(
        ('Admin','Admin'),
        ('StationMaster','StationMaster'),
        ('Passenger','Passenger'),
    )
    email = models.EmailField(unique=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    role=models.CharField(max_length=20,choices=ROLE_OPTIONS,default='Admin')
    
    def __str__(self):
        return f"{self.user.email}"
    

