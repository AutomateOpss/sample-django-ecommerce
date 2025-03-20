from django.test import TestCase
from .models import Order

class OrderModelTest(TestCase):

    def setUp(self):
        self.order = Order.objects.create(
            customer_name='John Doe',
            product_id=1,
            quantity=2,
            status='Pending'
        )

    def test_order_creation(self):
        self.assertEqual(self.order.customer_name, 'John Doe')
        self.assertEqual(self.order.quantity, 2)
        self.assertEqual(self.order.status, 'Pending')

    def test_order_str(self):
        self.assertEqual(str(self.order), f'Order {self.order.id} - {self.order.customer_name}')