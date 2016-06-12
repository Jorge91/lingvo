import datetime
from django.contrib.gis.geos import fromstr
from django.contrib.gis.measure import D
from rest_framework import status
from rest_framework.mixins import RetrieveModelMixin, CreateModelMixin, ListModelMixin, DestroyModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from meeting.models import Meeting, User_attends_meeting
from meeting.permissions import MeetingPermission, AttendMeetingPermission
from meeting.serializers import MeetingSerializer, AttendMeetingSerializer, AttendMeetingListSerializer
from meeting.settings import DEFAULT_DISTANCE
from utils.viewsets import MultipleSerializersViewSet


class MeetingViewSet(MultipleSerializersViewSet, RetrieveModelMixin, CreateModelMixin, ListModelMixin,
                     DestroyModelMixin):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer
    permission_classes = (IsAuthenticated, MeetingPermission)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        meeting = Meeting.objects.create(title=serializer.validated_data.get('title'),
                                         position=serializer.validated_data.get('position'),
                                         time=serializer.validated_data.get('time'), creator=request.user)

        serializer = MeetingSerializer(meeting)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.filter(time__gte=datetime.datetime.now())

        distance = request.query_params.get('distance', DEFAULT_DISTANCE)
        lat = request.query_params.get('lat')
        lon = request.query_params.get('lon')

        if lat is not None and lon is not None:
            pnt = fromstr('POINT(' + str(lat) + ' ' + str(lon) + ')', srid=4326)
            queryset = queryset.filter(position__distance_lte=(pnt, D(m=distance)))
            queryset = queryset.distance(pnt)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class AttendMeetingViewSet(MultipleSerializersViewSet, CreateModelMixin, ListModelMixin, DestroyModelMixin):
    queryset = User_attends_meeting.objects.all()
    serializer_class = AttendMeetingSerializer
    list_serializer_class = AttendMeetingListSerializer
    permission_classes = (IsAuthenticated, AttendMeetingPermission)

    def list(self, request, *args, **kwargs):

        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.filter(user=request.user)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
