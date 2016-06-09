from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.fields import ImageField

from language.models import User_speaks_language, User_practices_language
from language.serializers import UserSpeaksLanguageSerializer, UserPracticesLanguageSerializer
from profile.models import Profile
from related.settings import MAX_LANGUAGES_SHOWN


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username')

class RelatedProfileSerializer(serializers.ModelSerializer):
    speaks = serializers.SerializerMethodField('user_speaks')
    practices = serializers.SerializerMethodField('user_practices')
    user = UserSerializer()
    picture = ImageField(max_length=None, allow_empty_file=False, use_url=False)

    class Meta:
        model = Profile
        fields = ('description', 'genre', 'born_date', 'user', 'speaks', 'practices', 'picture')
        read_only = ('user', 'speaks', 'practices')
        depth = 1


    def user_speaks(self, obj):
        a = User_speaks_language.objects.filter(user=obj.user)[:MAX_LANGUAGES_SHOWN]
        return UserSpeaksLanguageSerializer(a, many=True).data

    def user_practices(self, obj):
        a = User_practices_language.objects.filter(user=obj.user)[:MAX_LANGUAGES_SHOWN]
        return UserPracticesLanguageSerializer(a, many=True).data