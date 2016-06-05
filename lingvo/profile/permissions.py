from utils.permissions import CustomActionPermissions


class ProfilePermission(CustomActionPermissions):

    def has_object_permission(self, request, view, obj):
        if view.action == 'update' or view.action == 'partial_update':
            return obj.user == request.user
        return True

