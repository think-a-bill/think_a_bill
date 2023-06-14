from functools import cached_property
from channels.layers import get_channel_layer

class ChannelLayerGroupSendMixin:
  CHANNEL_LAYER_GROUP_NAME = None

  @cached_property
  def channel_layer(self):
    return get_channel_layer()

  def channel_layer_group_send(self, message_dict):
    async_to_sync(self.channel_layer.group_send)(
      self.CHANNEL_LAYER_GROUP_NAME,
      message_dict
    )