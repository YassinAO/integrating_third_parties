from django.urls import path
# from django.contrib.auth.decorators import login_required
from .views import HotelListView, HotelDetailView, HotelCreateView, HotelUpdateView, DeleteView
from hotels import views

urlpatterns = [
    path('', views.index, name='hotels-index'),
    path('dashboard/', views.HotelListView.as_view(template_name='hotels/dashboard.html'),
         name='hotels-dashboard'),
    path('dashboard/<int:pk>', views.HotelDetailView.as_view(template_name='hotels/hotel_detail.html'),
         name='hotels-detail'),
    path('dashboard/create', views.HotelCreateView.as_view(template_name='hotels/hotel_form.html'),
         name='hotels-create'),
    path('dashboard/<int:pk>/update/', views.HotelUpdateView.as_view(template_name='hotels/hotel_form.html'),
         name='hotels-update'),
    path('dashboard/<int:pk>/delete/', views.HotelDeleteView.as_view(template_name='hotels/hotel_confirm_delete.html'),
         name='hotels-delete'),
]
