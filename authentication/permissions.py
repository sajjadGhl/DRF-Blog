from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return hasattr(request.user, 'role') and request.user.role == 'admin'


class IsAuthor(BasePermission):
    def has_permission(self, request, view):
        return hasattr(request.user, 'role') and request.user.role == 'author'


class IsUser(BasePermission):
    def has_permission(self, request, view):
        return hasattr(request.user, 'role') and request.user.role == 'user'


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return (hasattr(obj, 'author') and obj.author == request.user.id) or\
               (hasattr(obj, 'user_id') and obj.user_id == request.user.id)
