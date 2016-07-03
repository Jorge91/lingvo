from django.db.models import Q
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from chat.models import Chat
from chat.serializers import ChatSerializer, ChatDetailSerializer
from utils.viewsets import MultipleSerializersViewSet


class ChatsViewSet(MultipleSerializersViewSet, ListModelMixin, RetrieveModelMixin):
    queryset = Chat.objects.all()
    list_serializer_class = ChatSerializer
    retrieve_serializer_class = ChatDetailSerializer
    permission_classes = (IsAuthenticated,)
    filter_fields = ('categoria', 'categoria__titulo',)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.filter(Q(user_from=request.user) | Q(user_to=request.user))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        user_id = self.kwargs[self.lookup_field]
        instance = self.get_queryset().filter(
            Q(user_from=request.user, user_to__id=user_id) | Q(user_to=request.user, user_from__id=user_id)).first()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
