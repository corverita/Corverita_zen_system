from rest_framework import permissions
    
class EsCliente(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.perfil and request.user.perfil.rol.nombre == 'Cliente'
    
class EsProveedor(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.perfil and request.user.perfil.rol.nombre == 'Proveedor'
    
class EsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.perfil.rol.nombre == 'Admin'
    
class EsSoporte(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.perfil and request.user.perfil.rol.nombre == 'Soporte'
    
class EsSuperUsuario(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.is_superuser