from django.test import TestCase
from restaurant.models import MenuItem


class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(
            title="IceCream",
            price=2,
            inventory=40
        )
        self.assertEqual(item.__str__(), "IceCream : 2")