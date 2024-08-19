from rest_framework import permissions

class PuedeCrearProducto(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.perfil and request.user.perfil.rol.permisos.filter(nombre='Crear Producto').exists()
    
class PuedeVerProducto(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.perfil and request.user.perfil.rol.permisos.filter(nombre='Ver Producto').exists()
    
class PuedeEditarProducto(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user and request.user.is_authenticated and request.user.perfil and request.user.perfil.rol.permisos.filter(nombre='Editar Producto').exists()
    
class PuedeEliminarProducto(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user and request.user.is_authenticated and request.user.perfil and request.user.perfil.rol.permisos.filter(nombre='Eliminar Producto').exists()
    
class PuedeRestockProducto(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user and request.user.is_authenticated and request.user.perfil and request.user.perfil.rol.permisos.filter(nombre='Restock Producto').exists()
    
class PuedeVenderProducto(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user and request.user.is_authenticated and request.user.perfil and request.user.perfil.rol.permisos.filter(nombre='Vender Producto').exists()