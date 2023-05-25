from django import forms
from .models import Post,Comment
from taggit.forms import TagField

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'category', 'image', 'content',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)