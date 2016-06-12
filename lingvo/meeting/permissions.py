from utils.permissions import CustomActionPermissions


class MeetingPermission(CustomActionPermissions):

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        if view.action == 'destroy':
            return obj.creator == request.user
        return True

class AttendMeetingPermission(CustomActionPermissions):

    def has_permission(self, request, view):
        if super(AttendMeetingPermission, self).has_permission(request, view):
            if view.action == 'create':
                return str(request.data.get('user')) == str(request.user.id)
        return True

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        if view.action == 'destroy':
            return obj.user == request.user
        return True