from django.urls import path, reverse_lazy , include
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views import CustomPasswordChangeView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
# from accounts.views import kakao_login, kakao_callback

app_name = 'accounts'
urlpatterns = [
    path('basic_login/',LoginView.as_view(template_name='accounts/login_form.html'), name='basic_login'),
    path('login/', views.login, name='login'),
    path('basic_logout/',LogoutView.as_view(), name='basic_logout'),
    path('logout/',LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('basic_signup/', views.basic_signup, name='basic_signup'),
    path('edit/',views.account_edit, name='account_edit'),
    path('password-change/', CustomPasswordChangeView.as_view(template_name='accounts/password_change_form.html'), name='password_change'),
    path('delete/',views.delete,name='delete'),
    path('<username>/',views.profile_detail,name='detail'),
    # path('<username>/follow/',views.follow,name='follow'),
    path('toggle-follow/', views.toggle_follow, name='toggle_follow'),
    # path('<username>/image/',views.image_upload,name='image_upload')
    path('quiz_home/', views.quiz_home, name='quiz_home'),
    path('quiz/<int:pk>/', views.quiz, name='quiz'),
    path('quiz_make/', views.quiz_make, name='quiz_make'),
    path('answer_make/', views.answer_make, name='answer_make'),
    path('set_grade/<int:pk>', views.set_grade,name='set_grade'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)