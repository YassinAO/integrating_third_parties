from hotels.models import Hotel, City
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

# This test case is meant to see if the redirect, loaded templates and status codes are correct
# for those who are authorized and for those who aren't.


class TestViews(TestCase):

    def setUp(self):
        self.user = get_user_model()
        self.client = Client()
        self.dashboard_url = reverse('hotels-dashboard')
        self.create_hotel_url = reverse('hotels-create')
        # self.update_hotel_url = reverse('hotels-update',  kwargs={'pk': 1})
        self.create_user = self.user.objects.create_user(
            email='test@gmail.com', username='test', password='test123', is_staff=False)
        self.create_superuser = self.user.objects.create_superuser(
            email='super@gmail.com', username='super', password='super123')

    def test_auth_redirect_dashboard(self):
        login = self.client.login(
            email='test@gmail.com', password='test123')

        response = self.client.get(self.dashboard_url, follow=True)

        if (self.create_user or self.create_superuser) and login:
            self.assertEquals(response.status_code, 200)
            self.assertTemplateUsed(response, 'hotels/dashboard.html')
        else:
            self.assertEquals(response.status_code, 200)
            self.assertTemplateUsed(response, 'users/login.html')

    def test_status_code_and_permission_for_create_view(self):
        login = self.client.login(
            email='super@gmail.com', password='super123')
        response = self.client.get(self.create_hotel_url, follow=True)

        if (self.create_superuser.is_staff or self.create_user.is_staff) and login:
            self.assertEquals(response.status_code, 200)
            self.assertTemplateUsed(response, 'hotels/hotel_form.html')
        else:
            self.assertEquals(response.status_code, 403)

    # def test_status_code_and_permission_and_city_for_update_view(self):
    #     login = self.client.login(
    #         email='super@gmail.com', password='super123')
    #     response = self.client.get(self.update_hotel_url, follow=True)
