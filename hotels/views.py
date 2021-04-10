from django.shortcuts import render
from .models import Hotel, City
from django.views.generic import ListView
from .filters import HotelFilter

# Create your views here.

# This listview is making use of a filter based on django_filters package https://github.com/carltongibson/django-filter.
# Go to the filters.py file within this directory to modify the filter and/or add a new one.

# Iterating over the objects/queryset requires you to use object_list in the view, see https://docs.djangoproject.com/en/3.1/ref/class-based-views/generic-display/#listview
# Paginating requires you to use page_obj in the view, see https://docs.djangoproject.com/en/3.1/topics/pagination/#paginating-a-listview


def index(request):
    return render(request, 'hotels/index.html')


class HotelListView(ListView):
    paginate_by = 8
    model = Hotel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = HotelFilter(
            self.request.GET, queryset=self.get_queryset())
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return HotelFilter(self.request.GET, queryset=queryset).qs
