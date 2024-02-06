from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.db.models.signals import post_save
from django.dispatch import receiver

from core.models import Message
from .serializers import MessageSerializer


@receiver(post_save, sender=Message)
def send_message_to_websocket_room(
    sender, instance: Message, created, **kwargs
):
    if created:
        channel_layer = get_channel_layer()
        room_name = f"message_{instance.receiver.pk}"
        message_data = MessageSerializer(instance).data

        async_to_sync(channel_layer.group_send)(  # type: ignore
            room_name,
            {
                "type": "chat_message",
                "message": message_data,
            },
        )
