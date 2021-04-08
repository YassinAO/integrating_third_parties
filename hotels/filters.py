import django_filters
from .models import Hotel


class HotelFilter(django_filters.FilterSet):

    class Meta:
        model = Hotel
        fields = ['city']
