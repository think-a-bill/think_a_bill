from django.conf import settings
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from django.db import models

# Create your models here.
class User(AbstractUser):
    # nickname = models.CharField(max_length=20,unique=True)
    image = models.ImageField(blank=True, null=True, upload_to='profile/')
    birthday = models.DateField(blank=False,)
    follow = models.ManyToManyField('self',symmetrical=False,related_name='followers')
