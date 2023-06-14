from channels.generic.websocket import WebsocketConsumer, JsonWebsocketConsumer
from asgiref.sync import async_to_sync

class LiveblogConsumer(JsonWebsocketConsumer):
  groups = ['liveblog']

  def liveblog_post_created(self, event_dict):
    self.send_json(event_dict)

  def liveblog_post_deleted(self, event_dict):
    self.send_json(event_dict)

  def liveblog_post_updated(self, event_dict):
    self.send_json(event_dict)

class EchoConsumer(JsonWebsocketConsumer):

  # 웹소켓 수신 메세지를 처리하기 위한 receive 메서드 재정의. receive 메서드는 새로운 text/bytes frame을 받을 때마다 호출.
  def receive_json(self, content, **kwargs):
    print('수신 : ', content)
    # 서버단 (장고)에서 JSON 형식을 읽기

    # 응답시에 객체로는 문자를 읽을 수 없으니 json.dumps API를 통해 문자열로 변환하여 전송
    self.send_json({
      'content' : content['content'],
      'user' : content['user'],
    })

class ChatConsumer(JsonWebsocketConsumer):
  SQUARE_GROUP_NAME = 'square'
  groups = [SQUARE_GROUP_NAME]

  def receive_json(self, content, **kwargs):
    _type = content['type']

    if _type == 'chats.message':
      message = content['message']
      async_to_sync(self.channel_layer.group_send)(
        'square' ,
      {
          'type' : 'chat.message',
          'message' : message,
      }
      )
    else:
      print(f'Invalid message type : ${_type}')

  def chat_message(self,message_dict):
    self.send_json({
      'type' : 'chat.message',
      'message' : message_dict['message'],
    })