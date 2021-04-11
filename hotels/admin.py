from django.contrib import admin
from .models import Hotel, City

# Register your models here.


class HotelModelAdmin(admin.ModelAdmin):
    search_fields = ('name', 'city_code',)
    list_filter = ('city',)
    ordering = ('city_code',)
    list_display = ('name', 'city_code', 'city',
                    'updated', 'created',)
    fieldsets = (
        ('Hotel Information', {'fields': ('name',)}),
        ('City Information', {'fields': ('city', 'city_code')}),
    )


class CityModelAdmin(admin.ModelAdmin):
    search_fields = ('name', 'acronym',)
    list_filter = ('name',)
    ordering = ('acronym',)
    list_display = ('name', 'acronym', 'updated', 'created',)
    fieldsets = (
        ('City Informatation', {'fields': ('name', 'acronym')}),
    )


admin.site.register(Hotel, HotelModelAdmin)
admin.site.register(City, CityModelAdmin)
