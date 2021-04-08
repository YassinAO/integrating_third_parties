from django.urls import path
from hotels.views import HotelListView

urlpatterns = [
    path('', HotelListView.as_view(), name='hotels-index')
]
