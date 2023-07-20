from django_filters import rest_framework as filters
from advertisements.models import Advertisement, AdvertisementStatusChoices


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    created_at = filters.DateFromToRangeFilter(field_name='created_at')
    creator = filters.NumberFilter(field_name='creator')
    status = filters.ChoiceFilter(choices=AdvertisementStatusChoices.choices, field_name='status')

    class Meta:
        model = Advertisement
        fields = ['creator', 'created_at', 'status']

