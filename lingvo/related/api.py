from django.db.models import Q, Count
from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from language.models import User_speaks_language, User_practices_language
from profile.models import Profile
from profile.serializers import ProfileSerializer
from related.serializers import RelatedProfileSerializer
from utils.viewsets import MultipleSerializersViewSet


class RelatedViewSet(MultipleSerializersViewSet, ListModelMixin):
    queryset = Profile.objects.all()
    serializer_class = RelatedProfileSerializer
    permission_classes = (IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        user = request.user

        practice_languages = User_practices_language.objects.filter(user=user).values_list('language', flat=True)

        users_speak = User_speaks_language.objects.filter(language__in=practice_languages).values('user').annotate(
            dcount=Count('language')).values_list('user', flat=True).order_by('dcount')

        queryset = Profile.objects.filter(Q(user__in=users_speak))
        queryset = queryset.exclude(user=user)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
