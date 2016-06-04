from rest_framework import serializers

from profile.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    #user = serializers.SerializerMethodField('include_user')
    # faltan los idiomas

    class Meta:
        model = Profile
        fields = ('description', 'genre', 'born_date', 'user')
        read_only = ('user',)

    #def include_user(self, obj):
    #    return obj.user_id
