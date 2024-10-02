from django.test import TestCase, Client

from apps.usuarios.models import Usuario, Rol, Permiso
from apps.perfiles_usuario.models import PerfilUsuario
from apps.catalogos.models import Prioridad, Estatus

from .utils import *

class BaseTestCase(TestCase):
    usuario = None
    perfil_usuario = None

    def create_user(self, username, email, password, **kwargs):
        # Create a user for testing
        usuario = Usuario.objects.create_user(username = username, email = email, password = password, **kwargs)
        return usuario
    
    def create_role(self, nombre):
        # Create a role for testing
        rol = Rol.objects.create(nombre=nombre)
        return rol

    def create_profile(self, biografia, usuario, fecha_nacimiento, telefono):
        # Create a profile for testing
        perfil = PerfilUsuario.objects.create(
            biografia=biografia, usuario=usuario, fecha_nacimiento=fecha_nacimiento, telefono=telefono
        )
        return perfil
    
    def create_permiso(self, nombre,):
        # Create a permission for testing
        permiso = Permiso.objects.create(nombre=nombre)
        return permiso
    
    def create_prioridad(self, nombre, descripcion):
        # Create a priority for testing
        prioridad = Prioridad.objects.create(nombre=nombre, descripcion=descripcion)
        return prioridad
    
    def create_estatus(self, nombre, descripcion):
        # Create a status for testing
        estatus = Estatus.objects.create(nombre=nombre, descripcion=descripcion)
        return estatus
    
    def setUp(self):
        # Set up any necessary data or configurations for your test case
        self.usuario = self.create_user(
            **user_data
        )
        self.usuario.set_password('T3st1ng.')
        self.usuario.save()

        rol = self.create_role('Admin')

        self.perfil_usuario = self.create_profile('Hola, soy un usuario de prueba', self.usuario, '1999-01-01', '1234567890')
        self.perfil_usuario.rol = rol
        self.perfil_usuario.save()

        auth_token = get_auth_token(login_data)
        self.headers={
            "Authorization":"Bearer "+auth_token
        }

        self.client = Client(headers=self.headers)