from django.urls import path, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views import CustomPasswordChangeView

app_name = 'accounts'
urlpatterns = [
    path('login/',LoginView.as_view(template_name='accounts/login_form.html'), name='login'),
    path('logout/',LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('edit/',views.account_edit, name='account_edit'),
    path('password-change/', CustomPasswordChangeView.as_view(template_name='accounts/password_change_form.html'), name='password_change'),
    path('delete/',views.delete,name='delete'),
    path('<username>/',views.profile_detail,name='detail'),
    # path('<username>/follow/',views.follow,name='follow'),
    path('toggle-follow/', views.toggle_follow, name='toggle_follow'),
    path('<username>/image/',views.image_upload,name='image_upload')
]