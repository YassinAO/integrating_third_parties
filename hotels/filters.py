import django_filters
from .models import Hotel

# This filter specifies what we want to filter on in the model.

# You can modify this or add a new filter for a different model
# Make sure to import this new model.


class HotelFilter(django_filters.FilterSet):

    class Meta:
        model = Hotel
        fields = ['city']
