from django.shortcuts import render, get_object_or_404
from chats.models import Post

# Create your views here.

def index(request):
  return render(request, 'chats/index.html')

def room_chat(request, room_name):
  return render(request,'chats/room_chat.html',{
    'room_name' : room_name,
  })