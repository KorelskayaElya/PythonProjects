from rest_framework import permissions, viewsets
from rest_framework.viewsets import ModelViewSet
from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement
from advertisements.serializers import AdvertisementSerializer
from rest_framework.exceptions import PermissionDenied


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filterset_class = AdvertisementFilter

    def get_permissions(self):
        """Получение прав для действий."""

        if self.action in ["create", "update", "partial_update"]:
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = []

        return [permission() for permission in permission_classes]

    def perform_destroy(self, instance):
        """Удаление объявления."""

        if instance.creator != self.request.user:
            raise PermissionDenied("You are not allowed to delete this advertisement.")

        instance.delete()
