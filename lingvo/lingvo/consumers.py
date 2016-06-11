# In consumers.py
import json

from channels import Group
from channels.auth import channel_session_user_from_http, channel_session_user
from channels.sessions import channel_session

# agrega persistencia de sesiones a los canales (para que pertenezcan a salas)
from django.contrib.auth.models import User
from django.db.models import Q

from chat.models import Chat, Message


@channel_session_user_from_http
def ws_connect(message):
    prefix, other_user = message['path'].decode('ascii').strip('/').split('/')

    chat = Chat.objects.filter(Q(user_from=other_user, user_to=message.user) | Q(user_to=other_user, user_from=message.user))
    if chat.count() > 0:
        chat = chat[0]
    else:
        label = str(message.user.id) + "-" + str(other_user)
        chat = Chat.objects.create(user_to=User.objects.get(id=other_user), user_from=message.user, label=label)

    Group(
        'chat-' + chat.label,
        channel_layer=message.channel_layer
    ).add(message.reply_channel)

    # agregamos la sala a la que pertenece a manera de sesion
    message.channel_session['room'] = chat.label


@channel_session_user
def ws_receive(message):
    label = message.channel_session['room']
    chat = Chat.objects.get(label=label)

    data = json.loads(message['text'])

    if data:
        m = Message.objects.create(chat=chat, message=data['message'])

        Group(
            'chat-' + label,
            channel_layer=message.channel_layer
        ).send({"text": str(message.user.id) + ": " + data['message']})


@channel_session_user
def ws_disconnect(message):
    label = message.channel_session['room']
    room = Chat.objects.get(label=label)
    Group(
        'chat-' + label,
        channel_layer=message.channel_layer
    ).discard(message.reply_channel)
