from django.db import models
from django.conf import settings
from taggit.managers import TaggableManager

# Create your models here.
def post_img_path(instance, filename):
    return f'images/posts/{instance.title}/{filename}'

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_posts')
    title = models.CharField(max_length=50)
    content = models.TextField()
    category = models.CharField(max_length=10)
    image = models.ImageField(blank=True, null=True, upload_to='images/post/%Y/%m/%d/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = TaggableManager(blank=True, related_name='post_tags')  
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_comments')
    created_at = models.DateTimeField(auto_now_add=True)

class Emote(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    emotion = models.CharField(max_length=10)

