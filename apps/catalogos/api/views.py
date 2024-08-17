from apps.core.api.views import GenericCatalogBaseViewSet

from ..models import *
from .serializers import *

# ViewSet para el modelo de Estatus
class EstatusViewSet(GenericCatalogBaseViewSet):
    queryset = Estatus.objects.all()
    serializer_get = BaseEstatusSerializer

    def get_serializer_class(self):
        if self.action in ['create', 'update']:
            return PostEstatusSerializer
        if self.action in ['list', 'retrieve']:
            return BaseEstatusSerializer
        if self.action == 'destroy':
            return DeleteEstatusSerializer
        return self.serializer_get

# ViewSet para el modelo de Prioridad
class PrioridadViewSet(GenericCatalogBaseViewSet):
    queryset = Prioridad.objects.all()
    serializer_get = BasePrioridadSerializer

    def get_serializer_class(self):
        if self.action in ['create', 'update']:
            return PostPrioridadSerializer
        if self.action in ['list', 'retrieve']:
            return BasePrioridadSerializer
        if self.action == 'destroy':
            return DeletePrioridadSerializer
        return self.serializer_get
    
# ViewSet para el modelo de TipoMovimiento
class TipoMovimientoViewSet(GenericCatalogBaseViewSet):
    queryset = TipoMovimiento.objects.all()
    serializer_get = BaseTipoMovimientoSerializer

    def get_serializer_class(self):
        if self.action in ['create', 'update']:
            return PostTipoMovimientoSerializer
        if self.action in ['list', 'retrieve']:
            return BaseTipoMovimientoSerializer
        if self.action == 'destroy':
            return DeleteTipoMovimientoSerializer
        return self.serializer_get