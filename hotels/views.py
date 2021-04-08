from django.shortcuts import render
from .models import Hotel, City
from django.views.generic import ListView
from .filters import HotelFilter

# Create your views here.


class HotelListView(ListView):
    paginate_by = 5
    model = Hotel
    template_name = 'hotels/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = HotelFilter(
            self.request.GET, queryset=self.get_queryset())
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return HotelFilter(self.request.GET, queryset=queryset).qs
