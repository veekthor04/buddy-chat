from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema, OpenApiExample
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import Message
from .serializers import MessageSerializer


@extend_schema(tags=["Messages"])
class MessageViewSet(viewsets.ModelViewSet):
    """
    A viewset for managing messages.
    """

    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "post", "delete", "head", "options", "trace"]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["receiver", "sender"]

    def get_queryset(self):
        """Return messages for the authenticated user"""
        return self.queryset.filter(
            Q(sender=self.request.user) | Q(receiver=self.request.user)
        ).select_related("sender", "receiver")

    def perform_create(self, serializer):
        """Create a new message"""
        serializer.save(sender=self.request.user)


class MarkMessageAsReadView(APIView):
    """Marks a message as read by the receiver"""

    permission_classes = (IsAuthenticated,)
    serializer_class = MessageSerializer

    @extend_schema(
        responses={
            200: {"description": "Message marked as read"},
            404: {"description": "Message not found"},
        },
        examples=[
            OpenApiExample(
                "Mark message as read",
                value={"detail": "Message marked as read"},
                status_codes=[200],
            ),
            OpenApiExample(
                "Message not found",
                value={"detail": "Message not found"},
                status_codes=[404],
            ),
        ],
        tags=["Messages"],
    )
    def patch(self, request, message_id):
        try:
            message = Message.objects.get(id=message_id, receiver=request.user)
        except Message.DoesNotExist:
            return Response(
                status=status.HTTP_404_NOT_FOUND,
                data={"detail": "Message not found"},
            )

        message.mark_as_read()
        return Response(
            status=status.HTTP_200_OK,
            data={"detail": "Message marked as read"},
        )
