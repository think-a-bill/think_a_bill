from django import forms
from .models import Post,Comment
from taggit.forms import TagField, TagWidget

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'category', 'content','image', 'tags')


class CommentForm(forms.ModelForm):
    tags = forms.CharField(
    label='태그',
    widget=TagWidget(
        attrs={
            'class': 'form-control',
            'placeholder': '태그는 콤마(,)로 구분하여 작성해주세요' 
            }
        )
    )
    class Meta:
        model = Comment
        fields = ('content',)