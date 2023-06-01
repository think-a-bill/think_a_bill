from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views 

app_name = 'posts'
urlpatterns = [
    # post관련 url
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:post_pk>/', views.detail, name='detail'),
    # path('<int:post_pk>/update/', views.update, name='update'),
    path('<int:post_pk>/likes/', views.likes, name='likes'),
    path('<int:post_pk>/delete/', views.delete, name='delete'),


    # comment관련 url
    path('<int:post_pk>/comments/', views.comments_create, name='comments_create'),
    path('<int:post_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
    

    
    # 기타 url
    path('search/', views.search, name="search"),
    path('tags/<int:tag_pk>/', views.tagged, name='tagged'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
