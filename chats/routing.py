from django.urls import path

from . import consumers
from .consumers import EchoConsumer, LiveblogConsumer

websocket_urlpatterns =[
  path('ws/liveblog/', LiveblogConsumer.as_asgi()),
  path('ws/echo/', EchoConsumer.as_asgi()),
  path('ws/chats/<str:room_name>/chats', consumers.ChatConsumer.as_asgi())
]