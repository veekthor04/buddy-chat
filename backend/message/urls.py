from django.urls import path

from rest_framework.routers import SimpleRouter

from .views import MessageViewSet, MarkMessageAsReadView


router = SimpleRouter()
router.register(r"", MessageViewSet, basename="message")

urlpatterns = [
    path("<uuid:message_id>/read/", MarkMessageAsReadView.as_view(), name="message-mark-as-read"),
]

urlpatterns += router.urls
