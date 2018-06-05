from rest_framework import permissions


class IsProfessional(permissions.BasePermission):
    """
    Custom permission to only allow pro to read object.
    """
    def has_permission(self, request, view):
        user = request.user
        if request.method in permissions.SAFE_METHODS:
            return hasattr(user, 'professional') or user.is_superuser
        return True
