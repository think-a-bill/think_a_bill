from django.urls import path
from . import views

app_name = 'chats'
urlpatterns = [
    path('',views.index,name='index'),
    path('liveblog/',views.liveblog_index),
    path('liveblog/posts/<int:post_id>/',views.post_partial,name='post_partial'),
    path('<str:room_name>/chats/',views.room_chat,name='room_chat'),
    path('echo/', views.echo_page),
]
