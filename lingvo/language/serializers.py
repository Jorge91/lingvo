from django.contrib.auth.models import User
from rest_framework import serializers
from language.models import Language, User_speaks_language, User_practices_language

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id',)

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language

class UserSpeaksLanguageSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = User_speaks_language
        depth = 2

class CreateUserSpeaksLanguageSerializer(serializers.ModelSerializer):

    class Meta:
        model = User_speaks_language

class UserPracticesLanguageSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = User_practices_language
        depth = 2

class CreateUserPracticesLanguageSerializer(serializers.ModelSerializer):

    class Meta:
        model = User_practices_language