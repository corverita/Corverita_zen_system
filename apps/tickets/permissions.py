from rest_framework import permissions

class PuedeCrearTickets(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.perfil and request.user.perfil.rol.permisos.filter(nombre='Crear Tickets').exists()
    
class PuedeVerTickets(permissions.BasePermission):
    def has_permission(self, request, view):
        print(request.user.perfil.rol.permisos)
        return request.user and request.user.perfil and request.user.perfil.rol.permisos.filter(nombre='Ver Tickets').exists()
    
class PuedeEditarTickets(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user and request.user.perfil and request.user.perfil.rol.permisos.filter(nombre='Editar Tickets').exists() and obj.usuario == request.user
    
class PuedeEliminarTickets(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user and request.user.perfil and request.user.perfil.rol.permisos.filter(nombre='Eliminar Tickets').exists() and (obj.usuario == request.user or request.user.perfil.nombre == 'Admin')
    
class PuedeAsignarPrioridad(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user and request.user.perfil and request.user.perfil.rol.permisos.filter(nombre='Asignar Prioridad a Tickets').exists()
    
class PuedeMarcarSolucionado(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user and request.user.perfil and request.user.perfil.rol.permisos.filter(nombre='Marcar Solucionado Tickets').exists()