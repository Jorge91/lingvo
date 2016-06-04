from rest_framework import serializers
from language.models import Language, User_speaks_language, User_practices_language


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language

class UserSpeaksLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_speaks_language

class UserPracticesLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_practices_language