from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from rest_framework import serializers
from .models import Chat, Message


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = (
            'username',
            'email',
            'groups',
            'last_login',
            'first_name',
            'last_name',
        )


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = (
            'name',
        )


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = (
            'title',
            'creator',
            'invited',
            'is_closed',
        )


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = (
            'sender',
            'chat',
            'message',
            'status',
        )


