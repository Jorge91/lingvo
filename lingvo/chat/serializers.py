from django.contrib.auth.models import User
from rest_framework import serializers

from chat.models import Chat, Message


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class ChatSerializer(serializers.ModelSerializer):
    user_from = UserSerializer()
    user_to = UserSerializer()

    class Meta:
        model = Chat
        depth = 2


class MessageSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Message
        depth = 2


class ChatDetailSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Chat
        fields = ('label', 'user_from', 'user_to', 'messages')


