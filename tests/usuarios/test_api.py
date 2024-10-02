from tests.core.mixin import BaseTestCase

class TestRegistroUsuario(BaseTestCase):

    def setUp(self):
        super().setUp()

        self.data = {
            "username": "test",
            "first_name": "Test",
            "last_name": "User",
            "email": "test@user.com",
            "password": "T3st1ng.",
            "password_confirmation": "T3st1ng."
        }

    def test_registro_usuario(self):
        # Test the user registration
        response = self.client.post('/api/v1/usuarios/registro/', self.data)
        assert response.status_code == 201
        assert response.data['username'] == self.data['username']
        assert response.data['email'] == self.data['email']

    def test_registro_usuario_contrasena_no_coincide(self):
        # Test user registration with password mismatch
        self.data['password_confirmation'] = 'T3st1ng1.'
        response = self.client.post('/api/v1/usuarios/registro/', self.data)
        assert response.status_code == 400
        assert response.data['password'] == ['Las contraseñas no coinciden.']

    def test_registro_usuario_email_existente(self):
        # Test user registration with existing email
        self.data['email'] = self.usuario.email
        response = self.client.post('/api/v1/usuarios/registro/', self.data)
        assert response.status_code == 400
        assert response.data['email'] == ['Este campo debe ser único.']

    def test_registro_usuario_username_existente(self):
        # Test user registration with existing username
        self.data['username'] = self.usuario.username
        response = self.client.post('/api/v1/usuarios/registro/', self.data)
        assert response.status_code == 400
        assert response.data['username'] == ['Ya existe un usuario con ese nombre.']

    def test_registro_usuario_campos_requeridos(self):
        # Test user registration with missing required fields
        self.data.pop('username')
        response = self.client.post('/api/v1/usuarios/registro/', self.data)
        assert response.status_code == 400
        assert response.data['username'] == ['Este campo es requerido.']

    def test_registro_usuario_contrasena_corta(self):
        # Test user registration with short password
        self.data['password'] = '123'
        self.data['password_confirmation'] = '123'
        response = self.client.post('/api/v1/usuarios/registro/', self.data)
        assert response.status_code == 400

    def test_registro_usuario_contrasena_numerica(self):
        # Test user registration with long password
        self.data['password'] = '123456789012345678901234567890123456'
        self.data['password_confirmation'] = '123456789012345678901234567890123456'
        response = self.client.post('/api/v1/usuarios/registro/', self.data)
        assert response.status_code == 400