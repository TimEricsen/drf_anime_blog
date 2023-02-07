from rest_framework import permissions


# A function that checks if the user is the owner of the object.
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user


# A function that gives access to view only to unregistered users.
class IsNotAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return view


# А function that gives access to personal page only for owner user.
class IsUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.username == obj.username:
            return view
