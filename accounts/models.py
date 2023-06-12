from django.conf import settings
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from django.db import models

# Create your models here.
class User(AbstractUser):
    # nickname = models.CharField(max_length=20,unique=True)
    image = models.ImageField(blank=True, null=True, upload_to='profile/')
    birthday = models.DateField(blank=True, null=True,)
    follow = models.ManyToManyField('self',symmetrical=False,related_name='followers')
    score = models.IntegerField(default=0)
    grade = models.CharField(max_length=50, default='D')

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    score = models.IntegerField(default=None)


