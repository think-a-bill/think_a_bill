from django import forms
from .models import Post
from taggit.forms import TagField

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'category', 'image', 'content',)
