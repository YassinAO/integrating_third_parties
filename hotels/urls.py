from django.urls import path
from hotels.views import HotelListView, index
from django.contrib.auth.decorators import login_required
from hotels import views

urlpatterns = [
    path('', index, name='hotels-index'),
    path('dashboard/', login_required(HotelListView.as_view(template_name='hotels/dashboard.html')),
         name='hotels-dashboard'),
]
