from tests.core.mixin import BaseTestCase

from apps.tickets.models import Ticket

class TestTicket(BaseTestCase):
    
        def setUp(self):
            super().setUp()

            self.crear_tickets = self.create_permiso('Crear Tickets')
            self.ver_tickets = self.create_permiso('Ver Tickets')
            self.editar_tickets = self.create_permiso('Editar Tickets')
            self.eliminar_tickets = self.create_permiso('Eliminar Tickets')
            self.asignar_prioridad_tickets = self.create_permiso('Asignar Prioridad a Tickets')
            self.marcar_solucionado_tickets = self.create_permiso('Marcar Solucionado Tickets')

            self.prioridad_baja = self.create_prioridad('Baja', 'Prioridad baja')
            self.prioridad_media = self.create_prioridad('Media', 'Prioridad media')
            self.prioridad_alta = self.create_prioridad('Alta', 'Prioridad alta')

            self.estatus_activo = self.create_estatus('Activo', 'Estado Activo')
            self.estatus_en_proceso = self.create_estatus('En Proceso', 'Estado En Proceso')
            self.estatus_solucionado = self.create_estatus('Solucionado', 'Estado Solucionado')
            self.estatus_nuevo = self.create_estatus('Nuevo', 'Estado Nuevo')

            self.usuario.perfil.rol.permisos.add(self.crear_tickets)
            self.usuario.perfil.rol.permisos.add(self.ver_tickets)
            self.usuario.perfil.rol.permisos.add(self.editar_tickets)
            self.usuario.perfil.rol.permisos.add(self.eliminar_tickets)
            self.usuario.perfil.rol.permisos.add(self.asignar_prioridad_tickets)
            self.usuario.perfil.rol.permisos.add(self.marcar_solucionado_tickets)
    
            self.data = {
                "titulo": "Test Ticket",
                "descripcion": "Este es un ticket de prueba",
            }
    
        def test_crear_ticket(self):
            # Test ticket creation
            response = self.client.post('/api/v1/tickets/tickets/', self.data)
            assert response.status_code == 201
            assert response.data['titulo'] == self.data['titulo']
            assert response.data['descripcion'] == self.data['descripcion']
    
        def test_crear_ticket_campos_requeridos(self):
            # Test ticket creation with missing required fields
            self.data.pop('titulo')
            response = self.client.post('/api/v1/tickets/tickets/', self.data)
            assert response.status_code == 400
            assert response.data['titulo'] == ['Este campo es requerido.']

        def test_crear_ticket_sin_permiso(self):
            # Test ticket creation without permission
            self.usuario.perfil.rol.permisos.remove(self.crear_tickets)
            response = self.client.post('/api/v1/tickets/tickets/', self.data)
            assert response.status_code == 403
            assert response.data['detail'] == 'Usted no tiene permiso para realizar esta acción.'

        def test_ver_tickets(self):
            # Test ticket view
            self.data['estatus_id'] = self.estatus_nuevo.id
            self.data['usuario_id'] = self.usuario.id
            ticket = Ticket.objects.create(**self.data)
            response = self.client.get('/api/v1/tickets/tickets/')
            assert response.status_code == 200
            assert len(response.data['results']) == 1

        def test_ver_ticket(self):
            # Test ticket view
            self.data['estatus_id'] = self.estatus_nuevo.id
            ticket = Ticket.objects.create(**self.data)
            response = self.client.get(f'/api/v1/tickets/tickets/{ticket.id}/')
            assert response.status_code == 200
            assert response.data['titulo'] == self.data['titulo']
            assert response.data['descripcion'] == self.data['descripcion']

        def test_editar_ticket(self):
            # Test ticket edit
            self.data['estatus_id'] = self.estatus_nuevo.id
            self.data['usuario_id'] = self.usuario.id
            ticket = Ticket.objects.create(**self.data)
            data = {
                "titulo": "Test Ticket Editado",
                "descripcion": "Este es un ticket de prueba editado",
            }
            response = self.client.put(f'/api/v1/tickets/tickets/{ticket.id}/', data, content_type='application/json')
            assert response.status_code == 200
            assert response.data['titulo'] == data['titulo']
            assert response.data['descripcion'] == data['descripcion']

        def test_editar_ticket_sin_permiso(self):
            # Test ticket edit without permission
            self.data['estatus_id'] = self.estatus_nuevo.id
            ticket = Ticket.objects.create(**self.data)
            self.usuario.perfil.rol.permisos.remove(self.editar_tickets)
            data = {
                "titulo": "Test Ticket Editado",
                "descripcion": "Este es un ticket de prueba editado",
            }
            response = self.client.put(f'/api/v1/tickets/tickets/{ticket.id}/', data, content_type='application/json')
            assert response.status_code == 403
            assert response.data['detail'] == 'Usted no tiene permiso para realizar esta acción.'

        def test_eliminar_ticket(self):
            # Test ticket deletion
            self.data['estatus_id'] = self.estatus_nuevo.id
            self.data['usuario_id'] = self.usuario.id
            ticket = Ticket.objects.create(**self.data)
            response = self.client.delete(f'/api/v1/tickets/tickets/{ticket.id}/')
            assert response.status_code == 204

        def test_eliminar_ticket_sin_permiso(self):
            # Test ticket deletion without permission
            self.data['estatus_id'] = self.estatus_nuevo.id
            ticket = Ticket.objects.create(**self.data)
            self.usuario.perfil.rol.permisos.remove(self.eliminar_tickets)
            response = self.client.delete(f'/api/v1/tickets/tickets/{ticket.id}/')
            assert response.status_code == 403
            assert response.data['detail'] == 'Usted no tiene permiso para realizar esta acción.'

        def test_asignar_prioridad_ticket(self):
            # Test ticket priority assignment
            self.data['estatus_id'] = self.estatus_nuevo.id
            self.data['usuario_id'] = self.usuario.id
            ticket = Ticket.objects.create(**self.data)
            data = {
                "prioridad": self.prioridad_alta.id
            }
            response = self.client.put(f'/api/v1/tickets/tickets/{ticket.id}/asignar_prioridad/', data, content_type='application/json')
            assert response.status_code == 200
            assert response.data['prioridad']['nombre'] == self.prioridad_alta.nombre

        def test_asignar_prioridad_ticket_sin_permiso(self):
            # Test ticket priority assignment without permission
            self.data['estatus_id'] = self.estatus_nuevo.id
            ticket = Ticket.objects.create(**self.data)
            self.usuario.perfil.rol.permisos.remove(self.asignar_prioridad_tickets)
            data = {
                "prioridad": self.prioridad_alta.id
            }
            response = self.client.put(f'/api/v1/tickets/tickets/{ticket.id}/asignar_prioridad/', data, content_type='application/json')
            assert response.status_code == 403
            assert response.data['detail'] == 'Usted no tiene permiso para realizar esta acción.'

        def test_marcar_solucionado_ticket(self):
            # Test ticket resolution
            self.data['estatus_id'] = self.estatus_nuevo.id
            self.data['usuario_id'] = self.usuario.id
            ticket = Ticket.objects.create(**self.data)
            response = self.client.post(f'/api/v1/tickets/tickets/{ticket.id}/marcar_solucionado/')
            assert response.status_code == 200
            assert response.data['estatus']['nombre'] == self.estatus_solucionado.nombre

        def test_marcar_solucionado_ticket_sin_permiso(self):
            # Test ticket resolution without permission
            self.data['estatus_id'] = self.estatus_nuevo.id
            ticket = Ticket.objects.create(**self.data)
            self.usuario.perfil.rol.permisos.remove(self.marcar_solucionado_tickets)
            response = self.client.post(f'/api/v1/tickets/tickets/{ticket.id}/marcar_solucionado/')
            assert response.status_code == 403
            assert response.data['detail'] == 'Usted no tiene permiso para realizar esta acción.'