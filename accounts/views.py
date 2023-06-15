from django.contrib import messages

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login, get_user_model, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.http import JsonResponse
from .forms import CustomUserCreationForm, CustomUserChangeForm , CustomAuthenticationForm
from allauth.socialaccount.models import SocialAccount
from .models import Question, User , PnuUser , Answer
from .forms import QuestionForm , AnswerForm
from django.urls import reverse 


# Create your views here.
def login(request):
    # if request.user.is_authenticated:
    #     return redirect('main')
    
    # if request.method == 'POST':
    #     form = CustomAuthenticationForm(request, request.POST)
    #     if form.is_valid():
    #         auth_login(request, form.get_user())
    #         return redirect('posts:index')
    # else:
    #     form = CustomAuthenticationForm()
    # context = {
    #     'form': form,
    # }
    # return render(request, 'accounts/login.html', context)
    pass

# User = get_user_model()

def signup(request):
    # if request.user.is_authenticated:
    #     return redirect('posts:index')
    
    # if request.method == 'POST':
    #     form = CustomUserCreationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('accounts:login')
    # else:
    #     form = CustomUserCreationForm()
    # context = {
    #     'form': form,
    # }
    # return render(request, 'accounts/signup.html', context)
    pass

def basic_signup(request):
    if request.user.is_authenticated:
        return redirect('posts:index')
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:basic_login')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)

@login_required
def account_edit(request):
  # instance = get_object_or_404(User,pk=request.user.pk)
  if request.method == 'POST':
    form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
    if form.is_valid():
       form.save()
       return redirect('accounts:detail', request.user)
  else:
    form = CustomUserChangeForm(instance=request.user)
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


# class profiledetailview(DetailView):
#   model = User
#   template_name = 'accounts/profile_detail.html'
#   context_object_name = 'details'


def profile_detail(request, username):
  # 어차피 해당 유저의 프로필을 보여줌.
  # profile_detail = User.objects.get(username=username)
  # context = {
  #   'profile_detail' : profile_detail,
  # }
  # return render(request,'accounts/profile_detail.html',context)    
  person = User.objects.get(username=username)
  context = {
         'person':person,
      }
  if request.method == 'GET':
      user = PnuUser.objects.create(name='익명')
      user.save()
      return render(request, 'accounts/profile_detail.html', context)
  elif request.method == 'POST':
      user = PnuUser()
      user.name = request.POST.get('username', '')
      if not user.name:
          user.name = '익명'
      user.save()
      return render(request, 'accounts/profile_detail.html', context)
  else:
    return render(request, 'accounts/profile_detail.html', context)

@login_required
def follow(request,username):
  person = User.objects.get(username=username)
  # 팔로우를 다른 유저가 하면 ~
  if person != request.user:
    # person(본인 아닌 다른유저)이 이미 팔로우가 되어 있으면
    if person.followers.filter(username=request.user.username).exists():
      # 역참조 코드 : followers
      person.followers.remove(request.user)
    else:
      person.followers.add(request.user)
      # 현재 있는 페이지로 리다이렉트
  return redirect('accounts:detail', username=person.username)

# @login_required
# def image_upload(request,username):
#   if request.method == 'POST':
#     user_model = User.objects.get(username=username)
#     image_data = request.FILES['image']
#     user_model.image = image_data
#     user_model.save()
#     messages.info(request, '이미지가 정상적으로 업로드 되었습니다.')
#     return redirect('accounts:detail' ,username=username)
#   else:
#     return HttpResponse('GET request')


@login_required
def toggle_follow(request):
  if request.method == 'POST':
    user_pk = request.POST.get('user_pk')
    person = User.objects.get(pk=user_pk)

    if person != request.user:
      if person.followers.filter(pk=request.user.pk).exists():
        person.followers.remove(request.user)
        is_following = False
      else:
        person.followers.add(request.user)
        is_following = True

      return JsonResponse({'is_following': is_following})

  return JsonResponse({'error': 'Invalid request'})

# def kakao_disconnect(request):
#     if request.user.is_authenticated:
#         # 사용자의 카카오 소셜 계정 연결 끊기
#         SocialAccount.objects.filter(user=request.user, provider='kakao').delete() 
#     # 계정 삭제 후 리다이렉트할 URL
#         redirect_url = 'posts:index'
#     return redirect('posts:index')

# def calculate_score(user):
#     user_score = 0  # 사용자의 점수를 초기화

#     # 사용자가 선택한 답안과 정답을 비교하여 점수 계산
#     for question in Question.objects.all():
#         user_answer = request.POST.get(f'question_{question.id}')  # 사용자가 선택한 답안
#         correct_answer = question.correct_answer  # 해당 문제의 정답

#         if user_answer == correct_answer:
#             user_score += question.score

#     user.score = user_score  # 계산된 점수를 사용자에 저장
#     user.save()

# def quiz(request):
#     # 문제 데이터 가져오기
#     questions = Question.objects.all()

#     if request.method == 'POST':
#         # 유저가 퀴즈를 제출한 경우
#         user = User.objects.get(name=request.user.username)
#         # 점수 계산
#         calculate_score(user)
#         # 등급 설정
#         set_grade(user)
#     context = {
#        'questions': questions,
#     }
#     return render(request, 'quiz.html', context)

# def set_grade(user):
#     if user.score >= 5:
#         user.grade = 'A'
#     elif user.score >= 4:
#         user.grade = 'B'
#     elif user.score >= 3:
#         user.grade = 'C'
#     else:
#         user.grade = 'D'
#     user.save()

# def home_quiz(request, pk):
#    if request.GET:
#       user = PnuUser()
#       user.name = request.GET.get('username', '')
#       if request.GET['username'] == "":
#          user.name = '익명'
#       user.save()
#       return redirect('quiz', pk=user.pk)
#    return render(request, "accounts/quiz.html")


def quiz_home(request): 
  if request.GET:
    user = PnuUser()
    user.name = request.GET['name']
    if request.GET['name'] == "":
      user.name = "익명"
    user.save()
    return redirect("accounts:quiz", user.pk)
  return render(request, 'accounts/quiz_home.html')

def quiz(request, pk):
  user = get_object_or_404(PnuUser, pk=pk)
  aans = get_object_or_404(Answer)

  num = 1
  if request.POST:
     num = int(request.POST['quiz_id']) + 1
     user.answer = user.answer + request.POST['answer']
     if request.POST['answer'] == aans.ans[num-2]:
        user.score += 1
        user.save()
     if num > 4:
      return redirect("accoutns:set_grade", pk)
  quiz = get_object_or_404(Question, id=num )
  return render(request, "accounts/quiz.html", {'quiz':quiz})

def quiz_make(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST, request.FILES)
        if form.is_valid():
            quiz = form.save(commit=False)
            quiz.save()
            return render(request, 'accounts/quiz_make.html', {'form': form})
    else:
        form = QuestionForm()
    return render(request, 'accounts/quiz_make.html', {'form': form})

def answer_make(request):
    if request.method == 'POST':
        form = AnswerForm(request.POST, request.FILES)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.user = request.user
            answer.save()
            return redirect(reverse('accounts:quiz', kwargs={'pk': answer.user.pk}))
    else:
        form = AnswerForm()
    return render(request, 'accounts/answer_make.html', {'form': form})

def set_grade(user):
    if user.score >= 5:
        user.grade = 'A'
    elif user.score >= 4:
        user.grade = 'B'
    elif user.score >= 3:
        user.grade = 'C'
    else:
        user.grade = 'D'
    user.save()
