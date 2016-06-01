from rest_framework import status
from rest_framework.mixins import UpdateModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from profile.models import Profile
from profile.permissions import ProfilePermission
from profile.serializers import ProfileSerializer
from utils.viewsets import MultipleSerializersViewSet


class ProfileViewSet(MultipleSerializersViewSet, UpdateModelMixin, RetrieveModelMixin):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated, ProfilePermission)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class UserInfo(APIView):
    queryset = Profile.objects.all()

    def get(self, request):
        if request.user.is_authenticated():
            serializer = ProfileSerializer(instance=Profile.objects.get(user=request.user))
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)