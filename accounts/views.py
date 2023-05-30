from django.contrib import messages

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login, get_user_model, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import DetailView

from .forms import CustomUserCreationForm, CustomUserChangeForm

# Create your views here.
# def login(request):
#     if request.user.is_authenticated:
#         return redirect('main')
    
#     if request.method == 'POST':
#         form = CustomAuthenticationForm(request, request.POST)
#         if form.is_valid():
#             auth_login(request, form.get_user())
#             return redirect('posts:index')
#     else:
#         form = CustomAuthenticationForm()
#     context = {
#         'form': form,
#     }
#     return render(request, 'accounts/login.html', context)

User = get_user_model()

def signup(request):
    if request.user.is_authenticated:
        return redirect('posts:index')
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)

@login_required
def account_edit(request):
  instance = get_object_or_404(User,pk=request.user.pk)
  if request.method == 'POST':
    form = CustomUserChangeForm(request.POST,instance=instance)
    if form.is_valid():
       form.save()
       return redirect('posts:index')
  else:
    form = CustomUserChangeForm(instance=instance)
  context = {
    'form' : form
  }
  return render(request, 'accounts/account_edit.html',context)

class CustomPasswordChangeView(PasswordChangeView):
  success_url = reverse_lazy('posts:index')

def delete(request):
  request.user.delete()
  auth_logout(request)
  return redirect('posts:index')


class profiledetailview(DetailView):
  model = User
  template_name = 'accounts/profile_detail.html'
  context_object_name = 'details'

def profile_detail(request,username):
  # 어차피 해당 유저의 프로필을 보여줌.
  profile_detail = User.objects.get(username=username)
  context = {
    'profile_detail' : profile_detail,
  }
  return render(request,'accounts/profile_detail.html',context)

@login_required
def follow(request,username):
  person = User.objects.get(username=username)
  # 팔로우를 다른 유저가 하면 ~
  if person != request.user:
    # person(본인 아닌 다른유저)이 이미 팔로우가 되어 있으면
    if person.followers.filter(pk=request.user.pk).exists():
      # 역참조 코드 : followers
      person.followers.remove(request.user)
    else:
      person.followers.add(request.user)
      # 현재 있는 페이지로 리다이렉트
  return redirect('accounts:detail', person.username)

@login_required
def image_upload(request,username):
  if request.method == 'POST':
    user_model = User.objects.get(username=username)
    image_data = request.FILES['image']
    user_model.image = image_data
    user_model.save()
    messages.info(request, '이미지가 정상적으로 업로드 되었습니다.')
    return redirect('accounts:detail' ,username=username)
  else:
    return HttpResponse('GET request')