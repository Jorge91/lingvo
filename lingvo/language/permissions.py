from rest_framework.permissions import BasePermission

from language.models import User_practices_language, User_speaks_language


class UserPracticesLanguagesPermission(BasePermission):
    def has_permission(self, request, view):
        if super(UserPracticesLanguagesPermission, self).has_permission(request, view):
            if view.action == 'create':
                return request.data.get('user') == request.user.id
            if view.action == 'destroy':
                return request.user.id == User_practices_language.objects.get(pk=view.kwargs.get('pk')).user.id
        return False


class UserSpeaksLanguagesPermission(BasePermission):
    def has_permission(self, request, view):
        if super(UserSpeaksLanguagesPermission, self).has_permission(request, view):
            if view.action == 'create':
                return request.data.get('user') == request.user.id
            if view.action == 'destroy':
                return request.user.id == User_speaks_language.objects.get(pk=view.kwargs.get('pk')).user.id
        return False