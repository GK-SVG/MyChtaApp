# Create your views here.
from django.shortcuts import render
from .models import ChatRoom, Message

def room(request, room_name):
    user = request.user
    room, created = ChatRoom.objects.get_or_create(name=room_name, created_by=user)
    messages = Message.objects.filter(room=room)
    return render(request, 'room.html', {
        'room_name': room_name,
        'messages': messages
    })