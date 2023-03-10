from django.test import TestCase,Client
from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer
from rest_framework.renderers import JSONRenderer
class MenuViewSet(TestCase):
    def setup(self):
        MenuItem.objects.create(title="Dish1",price=23,inventory=100)
        MenuItem.objects.create(title="Dish1",price=23,inventory=100)
        MenuItem.objects.create(title="Dish1",price=23,inventory=100)
    def test_getall(self):
        response = self.client.get("/api/menu-items/")
        items = MenuItem.objects.all()
        serializer = MenuItemSerializer(items, many=True)
        response_data = response.content.decode('utf-8')
        expected_data = JSONRenderer().render(serializer.data).decode('utf-8')
        self.assertEqual(response_data, expected_data)
