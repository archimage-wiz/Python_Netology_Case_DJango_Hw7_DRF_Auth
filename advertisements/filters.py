from django_filters import rest_framework as filters, DateFromToRangeFilter
from django_filters.rest_framework import FilterSet

from advertisements.models import Advertisement


class AdvertisementsFilter(FilterSet):
    created_at = DateFromToRangeFilter()

    class Meta:
        model = Advertisement
        fields = ['created_at', 'status', 'title', 'description']

