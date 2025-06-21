import unittest
from src.shopping_cart import ShoppingCart, process_payment

class TestCartPaymentIntegration(unittest.TestCase):
    def test_successful_payment_clears_cart(self):
        cart = ShoppingCart()
        cart.add_item({'name': 'Book A', 'price': 10})
        total = sum(item['price'] for item in cart.items)
        result = process_payment(cart, total)
        self.assertTrue(result)
        self.assertEqual(len(cart.items), 0)

    def test_failed_payment_does_not_clear_cart(self):
        cart = ShoppingCart()
        cart.add_item({'name': 'Book B', 'price': -5})
        total = sum(item['price'] for item in cart.items)
        result = process_payment(cart, total)
        self.assertFalse(result)
        self.assertEqual(len(cart.items), 1)

if __name__ == '__main__':
    unittest.main()
