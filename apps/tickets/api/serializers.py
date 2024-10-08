from rest_framework import serializers

from apps.catalogos.api.serializers import BasePrioridadSerializer, BaseEstatusSerializer
from apps.usuarios.api.serializers import GetUsuarioSerializer
from ..models import *

# Serializer para el catálogo de Ticket
# Serializer Base para Get y respuestas
class BaseTicketSerializer(serializers.ModelSerializer):
    fecha_creacion = serializers.DateTimeField(format='%d-%m-%Y %H:%M:%S', read_only=True)
    fecha_modificacion = serializers.DateTimeField(format='%d-%m-%Y %H:%M:%S', read_only=True)
    usuario = GetUsuarioSerializer(read_only=True)
    prioridad = BasePrioridadSerializer(read_only=True)
    estatus = BaseEstatusSerializer(read_only=True)

    class Meta:
        model = Ticket
        fields = '__all__'

# Serializer para recibir información de POST
class PostTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['titulo', 'descripcion']

    def create(self, validated_data):
        estatus = Estatus.objects.get(nombre='Nuevo')
        usuario = self.context['usuario']
        validated_data['estatus'] = estatus
        validated_data['usuario'] = usuario
        ticket = Ticket.objects.create(**validated_data)
        return ticket

    def validate_titulo(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("El título debe tener al menos 5 caracteres")
        return value
    
    def validate_descripcion(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("La descripción debe tener al menos 5 caracteres")
        return value
    
# Serializer para recibir información de PUT para actualizar la prioridad del ticket
class AsignarPrioridadTicket(serializers.ModelSerializer):
    prioridad = serializers.IntegerField()

    class Meta:
        model = Ticket
        fields = ['prioridad']

    def validate(self, data):
        if not Prioridad.objects.filter(pk=data['prioridad']).exists():
            raise serializers.ValidationError("La prioridad seleccionada no existe")
        return data
    
class MarcarSolucionadoTicket(serializers.ModelSerializer):
    
    class Meta:
        model = Ticket
        fields = []


# Serializer para recibir información de DELETE
class DeleteTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['id']

# Serializer para el catálogo de Comentario
# Serializer Base para Get y respuestas
class BaseComentarioSerializer(serializers.ModelSerializer):
    fecha_creacion = serializers.DateTimeField(format='%d-%m-%Y %H:%M:%S', read_only=True)
    fecha_modificacion = serializers.DateTimeField(format='%d-%m-%Y %H:%M:%S', read_only=True)
    usuario = GetUsuarioSerializer(read_only=True)

    class Meta:
        model = Comentario
        fields = '__all__'

# Serializer para recibir información de POST
class PostComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = ['ticket', 'comentario']

    def create(self, validated_data):
        usuario = self.context['usuario']
        validated_data['usuario'] = usuario
        comentario = Comentario.objects.create(**validated_data)
        return comentario
    
    def validate(self, data):
        if not Ticket.objects.filter(pk=data['ticket'].id).exists():
            raise serializers.ValidationError("El ticket seleccionado no existe")
        
        estado_solucionado = Estatus.objects.get(nombre='Solucionado')
        ticket = Ticket.objects.get(pk=data['ticket'].id)
        if ticket.estatus == estado_solucionado:
            raise serializers.ValidationError("El ticket ya se encuentra solucionado, por tanto no puedes agregar más comentarios")

    def validate_comentario(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("El comentario debe tener al menos 5 caracteres")
            
        return value
    
# Serializer para recibir información de PUT
class UpdateComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = ['comentario']

    def validate_comentario(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("El comentario debe tener al menos 5 caracteres")
            
        return value

# Serializer para recibir información de DELETE
class DeleteComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = ['id']