from django.test import TestCase
# Replace 'your_app' with the actual name of your Django app
from restaurant.models import Menu
from rest_framework.test import APIClient
from rest_framework import status


class MenuViewTest(TestCase):
    def setUp(self):
        # Create sample Menu objects for testing
        self.menu1 = Menu.objects.create(Title="Menu 1")
        self.menu2 = Menu.objects.create(Title="Menu 2")
        self.menu3 = Menu.objects.create(Title="Menu 3")

        # Create an API client
        self.client = APIClient()

    def test_getall(self):
        # Get the list of Menu objects via the API
        # Adjust the URL to match your API endpoint
        response = self.client.get('/api/menu-items/')

        # Check if the request was successful
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Serialize the actual data and compare it to the response data
        expected_data = [
            {"id": self.menu1.id, "Title": "Menu 1"},
            {"id": self.menu2.id, "Title": "Menu 2"},
            {"id": self.menu3.id, "Title": "Menu 3"},
        ]
        self.assertEqual(response.data, expected_data)
