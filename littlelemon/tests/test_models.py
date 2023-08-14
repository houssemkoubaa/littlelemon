from restaurant.models import Menu
from django.test import TestCase


class MenuTest (TestCase):
    def setUp(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(item, "IceCream : 80")

    def test_menu_representation(self):
        expected_representation = f"Menu: {self.menu.name}"
        self.assertEqual(str(self.menu), expected_representation)
