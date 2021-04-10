from django.shortcuts import render
from .models import Hotel, City
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .filters import HotelFilter

# Create your views here.

# This listview is making use of a filter based on django_filters package https://github.com/carltongibson/django-filter.
# Go to the filters.py file within this directory to modify the filter and/or add a new one.

# Iterating over the objects/queryset requires you to use object_list in the view, see https://docs.djangoproject.com/en/3.1/ref/class-based-views/generic-display/#listview
# Paginating requires you to use page_obj in the view, see https://docs.djangoproject.com/en/3.1/topics/pagination/#paginating-a-listview


def index(request):
    return render(request, 'hotels/index.html')


class HotelListView(LoginRequiredMixin, ListView):
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


class HotelDetailView(LoginRequiredMixin, DetailView):
    model = Hotel


class HotelCreateView(LoginRequiredMixin, CreateView):
    model = Hotel
    fields = ['name', 'city_code', 'city']

    def test_func(self):
        hotel = self.get_object()
        if self.request.user.is_staff:
            return True
        return False


class HotelUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Hotel
    fields = ['name', 'city_code', 'city']

    def test_func(self):
        hotel = self.get_object()
        if self.request.user.is_staff:
            return True
        return False


class HotelDeleteView(UserPassesTestMixin, DeleteView):
    model = Hotel
    success_url = '/dashboard'

    def test_func(self):
        hotel = self.get_object()
        if self.request.user.is_staff:
            return True
        return False
