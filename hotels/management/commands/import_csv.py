from django.core.management.base import BaseCommand, CommandError
from hotels.models import Hotel, City
from decouple import config
from io import StringIO
import pandas as pd
import requests


class Command(BaseCommand):

    session = requests.Session()
    # set credentials in .env file
    session.auth = (config('CSV_USERNAME'), config('CSV_PASSWORD'))

    def handle(self, *args, **options):
        csv_city = self.session.get(
            'http://rachel.maykinmedia.nl/djangocase/city.csv')

        csv_hotel = self.session.get(
            'http://rachel.maykinmedia.nl/djangocase/hotel.csv')

        data_city = pd.read_csv(
            StringIO(csv_city.text), delimiter=';', engine='python', names=['acronym', 'name'])

        data_hotel = pd.read_csv(
            StringIO(csv_hotel.text), delimiter=';', engine='python', names=['city_acronym', 'city_code', 'name'])

        for index, row in data_city.iterrows():
            city, created = City.objects.get_or_create(
                name=row['name'],
                acronym=row['acronym'],
            )

        for index, row in data_hotel.iterrows():
            hotel, created = Hotel.objects.get_or_create(
                name=row['name'],
                city_code=row['city_code'],
                city_id=City.objects.get(acronym=row['city_acronym']).id
            )
