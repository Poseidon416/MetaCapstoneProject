from django.test import TestCase
from ..restaurant.models import Menu
from ..restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        # Create test instances of the Menu model
        self.menu1 = Menu.objects.create(name='Menu 1', price=10)
        self.menu2 = Menu.objects.create(name='Menu 2', price=15)
        self.menu3 = Menu.objects.create(name='Menu 3', price=20)
        
    def test_getall(self):
        # Retrieve all Menu objects
        response = self.client.get('/restaurant/menu/')
        
        self.assertEqual(response.status_code, 200)
        
        # Serialize the Menu instances
        expected_data = MenuSerializer([self.menu1, self.menu2, self.menu3], many=True).data
        self.assertEqual(response.data, expected_data)