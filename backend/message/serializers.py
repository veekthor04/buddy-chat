from rest_framework import serializers

from core.models import User, Message
from user.serializers import UserMiniSerializer


class MessageSerializer(serializers.ModelSerializer):
    """Serializer for messages"""

    sender = UserMiniSerializer(read_only=True)
    receiver = UserMiniSerializer(read_only=True)
    receiver_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source="receiver", write_only=True
    )

    class Meta:
        model = Message
        fields = "__all__"
        read_only_fields = ["sender", "read_at", "created_at"]
