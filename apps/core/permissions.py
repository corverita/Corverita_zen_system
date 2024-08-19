from rest_framework import permissions

class EsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user and obj.usuario == request.user