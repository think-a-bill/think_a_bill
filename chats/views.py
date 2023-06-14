from django.shortcuts import render, get_object_or_404
from chats.models import Post

# Create your views here.

def index(request):
  return render(request, 'chats/index.html')

def echo_page(request):
  return render(request, 'chats/echo_page.html')

def liveblog_index(request):
  post_qs = Post.objects.all()
  context = {
    'post_list' : post_qs,
  }
  return render(request, 'chats/liveblog_index.html',context)

def post_partial(request,post_id):
  post - get_object_or_404(Post,pk=post_id)
  context ={
    'post' : post
  }
  return render(request, 'chats/partial/post.html',context)

def room_chat(request, room_name):
  context = {
    'room_name' : room_name,
  }
  return render(request, 'chats/room_chat.html', context)