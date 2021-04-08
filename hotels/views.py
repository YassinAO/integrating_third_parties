from django.shortcuts import render
from .models import Hotel, City

# Create your views here.


def index(request):
    hotels = Hotel.get_all_hotels()
    cities = City.get_all_cities()
    data = {}
    data['hotels'] = hotels
    data['cities'] = cities

    return render(request, 'hotels/index.html', data)
