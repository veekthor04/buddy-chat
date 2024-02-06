import json
import logging

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


logger = logging.getLogger(__name__)


class MessageConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"message_{self.room_name}"
        user = self.scope["user"]

        # If the user is not authenticated or is anonymous, close the
        # connection
        if not user.is_authenticated or user.is_anonymous:
            self.close()
            return

        logger.info(f"Connected to {self.room_group_name}")
        async_to_sync(self.channel_layer.group_add)(  # type: ignore
            self.room_group_name, self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        logger.info(f"Disconnected from {self.room_group_name}")
        async_to_sync(self.channel_layer.group_discard)(  # type: ignore
            self.room_group_name, self.channel_name
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json.get("message")

        logger.info(f"Received message: {message}")
        async_to_sync(self.channel_layer.group_send)(  # type: ignore
            self.room_group_name, {"type": "chat_message", "message": message}
        )

    def chat_message(self, event):
        message = event.get("message")

        logger.info(f"Sending message: {message}")
        self.send(text_data=json.dumps({"message": message}))
