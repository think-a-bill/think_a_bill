from django import forms
from .models import Post,Comment
from taggit.forms import TagField, TagWidget

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'category', 'content','image', 'tags')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)