from django.db import models
from django.urls import reverse
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

    def get_absolute_url(self):
        return reverse('hotels-detail', kwargs={'pk': self.pk})
