from django.test import TestCase,Client
from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer
class MenuViewTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        MenuItem.objects.create("title=Dish1",price=15,inventory=100)
        MenuItem.objects.create("title=Dish2",price=20,inventory=100)
        MenuItem.objects.create("title=Dish3",price=13,inventory=100)
    def test_getall(self):
        response=self.client.get("api/menu-items/")
        items=MenuItem.objects.all()
        serializer=MenuItemSerializer(items,many=False)
        self.assertEqual(response.data,serializer.data)
