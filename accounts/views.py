from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login, get_user_model
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomUserChangeForm, CustomAuthenticationForm, CustomPasswordChangeForm

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
        return redirect('main')
    
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
  return render(request, 'account_edit.html',context)