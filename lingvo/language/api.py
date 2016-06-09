from rest_framework.mixins import ListModelMixin, CreateModelMixin, DestroyModelMixin
from rest_framework.permissions import IsAuthenticated

from language.models import Language, User_speaks_language, User_practices_language
from language.permissions import UserSpeaksLanguagesPermission, UserPracticesLanguagesPermission

from language.serializers import LanguageSerializer, UserSpeaksLanguageSerializer, \
    UserPracticesLanguageSerializer, CreateUserPracticesLanguageSerializer, CreateUserSpeaksLanguageSerializer
from utils.viewsets import MultipleSerializersViewSet


class LanguagesViewSet(MultipleSerializersViewSet, ListModelMixin):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = (IsAuthenticated,)


class UserSpeaksLanguageViewSet(MultipleSerializersViewSet, CreateModelMixin, DestroyModelMixin):
    queryset = User_speaks_language.objects.all()
    serializer_class = UserSpeaksLanguageSerializer
    create_serializer_class = CreateUserSpeaksLanguageSerializer
    permission_classes = (IsAuthenticated, UserSpeaksLanguagesPermission)


class UserPracticesLanguageViewSet(MultipleSerializersViewSet, CreateModelMixin, DestroyModelMixin):
    queryset = User_practices_language.objects.all()
    serializer_class = UserPracticesLanguageSerializer
    create_serializer_class = CreateUserPracticesLanguageSerializer
    permission_classes = (IsAuthenticated, UserPracticesLanguagesPermission)