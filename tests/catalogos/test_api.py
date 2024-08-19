from tests.core.mixin import BaseTestCase

from apps.catalogos.models import Prioridad, Estatus, TipoMovimiento

# TestCase para probar la API de Prioridad

class PrioridadAPITestCase(BaseTestCase):

    def setUp(self):
        super().setUp()
        # El perfil de usuario que se crea desde la clase padre ya tiene un rol de Admin, como en esto son catálogos y no permisos específicos, basta con ser admin.

        self.data = {
            "nombre": "Alta",
            "descripcion": "Prioridad alta"
        }


    def test_create_prioridad(self):
        # Testear la creación de una prioridad
        response = self.client.post('/api/v1/catalogos/prioridad/', data=self.data)
        self.assertEqual(Prioridad.objects.count(), 1)

    def test_list_prioridades(self):
        # Testear la lista de prioridades
        Prioridad.objects.create(**self.data)
        self.client.get('/api/v1/catalogos/prioridad/')
        self.assertEqual(Prioridad.objects.count(), 1)

    def test_retrieve_prioridad(self):
        # Testear la recuperación de una prioridad
        prioridad = Prioridad.objects.create(**self.data)
        self.client.get(f'/api/v1/catalogos/prioridad/{prioridad.id}/')
        self.assertEqual(Prioridad.objects.count(), 1)

    def test_update_prioridad(self):
        # Testear la actualización de una prioridad
        prioridad = Prioridad.objects.create(**self.data)
        self.data = {
            "nombre": "Baja",
            "descripcion": "Prioridad baja"
        }
        response = self.client.put(f'/api/v1/catalogos/prioridad/{prioridad.id}/', data=self.data, content_type='application/json')
        self.assertEqual(Prioridad.objects.get(id=prioridad.id).nombre, "Baja")

    def test_delete_prioridad(self):
        # Testear la eliminación de una prioridad
        prioridad = Prioridad.objects.create(**self.data)
        response = self.client.delete(f'/api/v1/catalogos/prioridad/{prioridad.id}/')
        self.assertEqual(Prioridad.objects.count(), 0)

    def test_prioridad_not_found(self):
        # Testear que una prioridad no exista
        response = self.client.get('/api/v1/catalogos/prioridad/999/')
        self.assertEqual(response.status_code, 404)

    def test_prioridad_not_found_delete(self):
        # Testear que una prioridad no exista al eliminar
        response = self.client.delete('/api/v1/catalogos/prioridad/999/')
        self.assertEqual(response.status_code, 404)

    def test_prioridad_not_found_update(self):
        # Testear que una prioridad no exista al actualizar
        self.data = {
            "nombre": "Baja",
            "descripcion": "Prioridad baja"
        }
        response = self.client.put('/api/v1/catalogos/prioridad/999/', data=self.data, content_type='application/json')
        self.assertEqual(response.status_code, 404)
        
        
# Pruebas de la API de Estatus
class EstatusAPITestCase(BaseTestCase):

    def setUp(self):
        super().setUp()
        # El perfil de usuario que se crea desde la clase padre ya tiene un rol de Admin, como en esto son catálogos y no permisos específicos, basta con ser admin.

        self.data = {
            "nombre": "Activo",
            "descripcion": "Estatus activo"
        }


    def test_create_estatus(self):
        # Testear la creación de un estatus
        response = self.client.post('/api/v1/catalogos/estatus/', data=self.data)
        self.assertEqual(Estatus.objects.count(), 1)

    def test_list_estatus(self):
        # Testear la lista de estatus
        Estatus.objects.create(**self.data)
        self.client.get('/api/v1/catalogos/estatus/')
        self.assertEqual(Estatus.objects.count(), 1)

    def test_retrieve_estatus(self):
        # Testear la recuperación de un estatus
        estatus = Estatus.objects.create(**self.data)
        self.client.get(f'/api/v1/catalogos/estatus/{estatus.id}/')
        self.assertEqual(Estatus.objects.count(), 1)

    def test_update_estatus(self):
        # Testear la actualización de un estatus
        estatus = Estatus.objects.create(**self.data)
        self.data = {
            "nombre": "Inactivo",
            "descripcion": "Estatus inactivo"
        }
        response = self.client.put(f'/api/v1/catalogos/estatus/{estatus.id}/', data=self.data, content_type='application/json')
        self.assertEqual(Estatus.objects.get(id=estatus.id).nombre, "Inactivo")

    def test_delete_estatus(self):
        # Testear la eliminación de un estatus
        estatus = Estatus.objects.create(**self.data)
        response = self.client.delete(f'/api/v1/catalogos/estatus/{estatus.id}/')
        self.assertEqual(Estatus.objects.count(), 0)

    def test_estatus_not_found(self):
        # Testear que un estatus no exista
        response = self.client.get('/api/v1/catalogos/estatus/999/')
        self.assertEqual(response.status_code, 404)

    def test_estatus_not_found_delete(self):
        # Testear que un estatus no exista al eliminar
        response = self.client.delete('/api/v1/catalogos/estatus/999/')
        self.assertEqual(response.status_code, 404)

# Pruebas de la API de TipoMovimiento
class TipoMovimientoAPITestCase(BaseTestCase):

    def setUp(self):
        super().setUp()
        # El perfil de usuario que se crea desde la clase padre ya tiene un rol de Admin, como en esto son catálogos y no permisos específicos, basta con ser admin.

        self.data = {
            "nombre": "Entrada",
            "descripcion": "Tipo de movimiento de entrada"
        }


    def test_create_tipo_movimiento(self):
        # Testear la creación de un tipo de movimiento
        response = self.client.post('/api/v1/catalogos/tipo-movimiento/', data=self.data)
        self.assertEqual(TipoMovimiento.objects.count(), 1)

    def test_list_tipo_movimiento(self):
        # Testear la lista de tipos de movimiento
        TipoMovimiento.objects.create(**self.data)
        self.client.get('/api/v1/catalogos/tipo-movimiento/')
        self.assertEqual(TipoMovimiento.objects.count(), 1)

    def test_retrieve_tipo_movimiento(self):
        # Testear la recuperación de un tipo de movimiento
        tipo_movimiento = TipoMovimiento.objects.create(**self.data)
        self.client.get(f'/api/v1/catalogos/tipo-movimiento/{tipo_movimiento.id}/')
        self.assertEqual(TipoMovimiento.objects.count(), 1)

    def test_update_tipo_movimiento(self):
        # Testear la actualización de un tipo de movimiento
        tipo_movimiento = TipoMovimiento.objects.create(**self.data)
        self.data = {
            "nombre": "Salida",
            "descripcion": "Tipo de movimiento de salida"
        }
        response = self.client.put(f'/api/v1/catalogos/tipo-movimiento/{tipo_movimiento.id}/', data=self.data, content_type='application/json')
        self.assertEqual(TipoMovimiento.objects.get(id=tipo_movimiento.id).nombre, "Salida")

    def test_delete_tipo_movimiento(self):
        # Testear la eliminación de un tipo de movimiento
        tipo_movimiento = TipoMovimiento.objects.create(**self.data)
        response = self.client.delete(f'/api/v1/catalogos/tipo-movimiento/{tipo_movimiento.id}/')
        self.assertEqual(TipoMovimiento.objects.count(), 0)

    def test_tipo_movimiento_not_found(self):
        # Testear que un tipo de movimiento no exista
        response = self.client.get('/api/v1/catalogos/tipo-movimiento/999/')
        self.assertEqual(response.status_code, 404)

    def test_tipo_movimiento_not_found_delete(self):
        # Testear que un tipo de movimiento no exista al eliminar
        response = self.client.delete('/api/v1/catalogos/tipo-movimiento/999/')
        self.assertEqual(response.status_code, 404)