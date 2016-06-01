# -*- coding: utf-8 -*-
from rest_framework.viewsets import GenericViewSet


class MultipleSerializersViewSet(GenericViewSet):

    list_serializer_class = None
    create_serializer_class = None
    retrieve_serializer_class = None
    update_serializer_class = None
    partial_update_serializer_class = None
    destroy_serializer_class = None

    def get_serializer_class(self):
        if self.action == 'list' and self.list_serializer_class:
            return self.list_serializer_class
        elif self.action == 'create' and self.create_serializer_class:
            return self.create_serializer_class
        elif self.action == 'retrieve' and self.retrieve_serializer_class:
            return self.retrieve_serializer_class
        elif self.action == 'update' and self.update_serializer_class:
            return self.update_serializer_class
        elif self.action == 'partial_update' and self.partial_update_serializer_class:
            return self.partial_update_serializer_class
        elif self.action == 'destroy' and self.destroy_serializer_class:
            return self.destroy_serializer_class
        else:
            return self.serializer_class