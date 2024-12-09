from django.urls import path
from ..MyChatApp import consumers

websocket_urlpatterns = [
    path('ws/mainapp/<str:room_name>/', consumers.ChatConsumer.as_asgi()),
]