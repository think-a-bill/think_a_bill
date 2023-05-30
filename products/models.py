from django.db import models
from django.conf import settings
from accounts.models import User

# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    like_product = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_products')
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(blank=True, null=True, upload_to='images/product/%Y/%m/%d/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

