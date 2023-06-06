from rest_framework.permissions import BasePermission


class RolePermission(BasePermission):

    def has_permission(self, request, view):
        try:
            if request.user.role.slug in view.accessible_roles:
                return True
            else:
                return False
        except AttributeError:
            return True


