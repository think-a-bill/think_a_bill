from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AuthenticationForm,  PasswordChangeForm
from django.contrib.auth import get_user_model
import datetime

# 회원가입
class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '아이디를 입력하세요',
                'style' : 'width: 400px;'
            }
        ),
    )
    email = forms.EmailField(
        label=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '이메일을 입력하세요',
            }
        ),
    )
    last_name = forms.CharField(
        label=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '이름을 입력하세요',
            }
        ),
    )

    birthday = forms.DateField(
        initial=datetime.date(2000, 1, 1),
        label=False,
        widget=forms.DateInput(
            attrs={
                'type':'date',
                'class': 'form-control',
            }
        ),
    )
    password1 = forms.CharField(
        label=False,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '비밀번호를 입력하세요',
            }
        ),
    )
    password2 = forms.CharField(
        label=False,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '비밀번호를 다시 입력하세요',
            }
        ),
    )

    
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'nickname', 'email','last_name', 'password1', 'password2', 'birthday')

# 유저 계정 수정
class CustomUserChangeForm(UserCreationForm):
  class Meta(UserChangeForm.Meta):
    model = get_user_model()
    fields = ('username', 'nickname', 'email','last_name', 'password1', 'password2', 'birthday')

# 비밀번호 변경