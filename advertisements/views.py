from django_filters import FilterSet, DateFromToRangeFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from advertisements.filters import AdvertisementsFilter
from advertisements.models import Advertisement
from advertisements.permissions import IsOwnerOrReadOnly
from advertisements.serializers import AdvertisementSerializer


def test_dunc(request):
    pass


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # filterset_fields = ['id', 'creator', 'title', 'created_at']
    search_fields = ['id', 'title']
    ordering_fields = ['id', 'title', 'status']
    pagination_class = LimitOffsetPagination
    filterset_class = AdvertisementsFilter

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAuthenticated(), IsOwnerOrReadOnly()]
        return []

    def create(self, request, *args, **kwargs):
        print('create')
        super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        print('update')
        super().update(request, *args, **kwargs)
