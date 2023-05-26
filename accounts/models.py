from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    nickname = models.CharField(max_length=20,unique=True)
    profile_photo = models.ImageField(blank=True, upload_to='profile')
    birthday = models.DateField(blank=False,)
    follow = models.ManyToManyField('self',symmetrical=False,related_name='followers')
