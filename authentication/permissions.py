from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return hasattr(request.user, 'role') and request.user.role == 'admin'


class IsAuthor(BasePermission):
    def has_permission(self, request, view):
        return hasattr(request.user, 'role') and request.user.role == 'author'

    def has_object_permission(self, request, view, author_obj):
        return author_obj.id == request.user.id


class IsAdminOrIsAuthor(BasePermission):
    def has_permission(self, request, view):
        return hasattr(request.user, 'role') and request.user.role in ['author', 'admin']

    def has_object_permission(self, request, view, obj):
        return request.user.role == 'admin' or obj.author == request.user.id


class IsUser(BasePermission):
    def has_permission(self, request, view):
        return hasattr(request.user, 'role') and request.user.role == 'user'
