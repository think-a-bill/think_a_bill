from django.conf import settings
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class User(AbstractUser):
    # nickname = models.CharField(max_length=20,unique=True)
    image = models.ImageField(blank=True, null=True, upload_to='profile/')
    birthday = models.DateField(blank=True, null=True,)
    follow = models.ManyToManyField('self',symmetrical=False,related_name='followers')
    score = models.IntegerField(default=0)
    grade = models.CharField(max_length=50, default='D')

class PnuUser(models.Model):
    name = models.CharField(max_length=20, default="익명")
    answer = models.CharField(default="", max_length=10,null=True,blank=True)
    score = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = [ 'score', 'name']

class Question(models.Model):
    question = models.CharField(max_length=200)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    image = models.ImageField(upload_to='quiz/', blank=True, null=True,)


    def __str__(self):
        return str(self.id)+'번 문제'
    
class Answer(models.Model):
    ans = models.CharField(default="", max_length=50, null=True, blank=True,)