# 장고 프로젝트 외부에서 장고 프로젝트 기능에 접근할 예졍.
import asyncio
# 환경변수 정의
import os
import django
from channels.layers import get_channel_layer

os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'
django.setup()

# 비동기
async def main():
  channel_layer = get_channel_layer()

  message_dict = {'content' : 'world'}

  await channel_layer.send('hello', message_dict)
  response_dict = await channel_layer.receive('hello')
  is_equal = message_dict == response_dict
  print('송신/수신 데이터가 같습니까?', is_equal)

asyncio.run(main())