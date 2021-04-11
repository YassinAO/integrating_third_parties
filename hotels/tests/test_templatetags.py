from django.test import TestCase
from hotels.templatetags.url_extras import my_url
from hotels.models import Hotel

# This test case is meant to see if the querystrings are correct when filtering the hotels and pagination the results.


class TemplateTagsTestCase(TestCase):

    def test_page_filter_query_string(self):
        page = my_url(1, 'page')
        self.assertEqual(page, '?page=1')

    def test_city_filter_query_string(self):
        city = my_url(1, 'city')
        self.assertEqual(city, '?city=1')

    def test_multiple_queries_string(self):
        pass
