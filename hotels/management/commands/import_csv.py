from django.core.management.base import BaseCommand, CommandError
from hotels.models import Hotel, City
from decouple import config
from io import StringIO
import pandas as pd
import requests

# This command retrieves CSV files from the authenticated HTTP
# and the retrieved data ends up in the models to populate the database.
# within the .env file you can specify the auth user/pass and csv urls.
# New commands can be made within this directory by creating a new file, read more at:
# https://docs.djangoproject.com/en/3.1/howto/custom-management-commands/

# This command is ran by using:
# python manage.py import_csv

# Or by creating a Windows scheduled task, see tutorial:
# https://www.youtube.com/watch?v=2UbJfx-cHb4


class Command(BaseCommand):

    session = requests.Session()
    # set credentials in .env file
    session.auth = (config('CSV_USERNAME'), config('CSV_PASSWORD'))

    def handle(self, *args, **options):
        # set credentials in .env file
        csv_city = self.session.get(config('CSV_CITY'))

        csv_hotel = self.session.get(config('CSV_HOTEL'))

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
        return
