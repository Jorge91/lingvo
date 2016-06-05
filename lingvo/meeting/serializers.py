from django.utils import timezone
from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from meeting.models import Meeting, User_attends_meeting


class AttendMeetingSerializer(serializers.ModelSerializer):

    class Meta:
        model = User_attends_meeting
        fields = ('user', 'meeting', 'id')
        read_only = ('user', 'id')


class MeetingSerializer(GeoFeatureModelSerializer):
    attendances = serializers.SerializerMethodField('meeting_attendances')

    class Meta:
        model = Meeting
        fields = ('title', 'position', 'time', 'creator', 'id', 'attendances')
        read_only = ('creator', 'attendances')
        geo_field = 'position'

    def validate_time(self, value):
        if value <= timezone.now():
            raise serializers.ValidationError(u"You cannot create events in the past!")
        return value

    def meeting_attendances(self, obj):
        a = User_attends_meeting.objects.filter(meeting=obj)
        return AttendMeetingSerializer(a, many=True).data
