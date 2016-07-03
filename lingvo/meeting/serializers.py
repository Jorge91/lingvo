from django.contrib.auth.models import User
from django.contrib.gis.db.models.sql import DistanceField
from django.utils import timezone
from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from meeting.models import Meeting, User_attends_meeting

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username')


class AttendMeetingSerializer(serializers.ModelSerializer):

    class Meta:
        model = User_attends_meeting
        fields = ('user', 'meeting', 'id')



class AttendMeetingListSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = User_attends_meeting
        fields = ('user', 'meeting', 'id')
        depth = 1



class MeetingSerializer(GeoFeatureModelSerializer):
    attendances = serializers.SerializerMethodField('meeting_attendances')
    distance = serializers.SerializerMethodField()
    user = UserSerializer()

    class Meta:
        model = Meeting
        fields = ('title', 'position', 'time', 'creator', 'id', 'attendances', 'distance')
        read_only = ('creator', 'attendances')
        geo_field = 'position'

    def validate_time(self, value):
        if value <= timezone.now():
            raise serializers.ValidationError(u"You cannot create events in the past!")
        return value

    def meeting_attendances(self, obj):
        a = User_attends_meeting.objects.filter(meeting=obj)
        return AttendMeetingSerializer(a, many=True).data

    def get_distance(self, obj):
        distance = getattr(obj, "distance", None)
        if distance is not None:
            return distance.standard
        else:
            return ""

