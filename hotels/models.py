from django.db import models

# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=200)
    acronym = models.CharField(max_length=50)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

    def __str__(self):
        return self.name

    @staticmethod
    def get_all_cities():
        return City.objects.all()


class Hotel(models.Model):
    name = models.CharField(max_length=200)
    city_code = models.CharField(max_length=50)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Hotel'
        verbose_name_plural = 'Hotels'

    def __str__(self):
        return self.name

    @staticmethod
    def get_all_hotels():
        return Hotel.objects.all()

    @staticmethod
    def get_hotel_by_city_id(city_id):
        if city_id:
            return Hotel.objects.filter(city=city_id)
        else:
            return Hotel.get_all_hotels()
