import unittest
from src.shopping_cart import calculate_total_price

class TestCalculateTotalPrice(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(calculate_total_price([]), 0)

    def test_single_item(self):
        items = [{'name': 'Book A', 'price': 10}]
        self.assertEqual(calculate_total_price(items), 10)

    def test_multiple_items(self):
        items = [
            {'name': 'Book A', 'price': 10},
            {'name': 'Book B', 'price': 15},
            {'name': 'Book C', 'price': 20}
        ]
        self.assertEqual(calculate_total_price(items), 45)

    def test_negative_price(self):
        items = [{'name': 'Book D', 'price': -5}]
        self.assertEqual(calculate_total_price(items), -5)

if __name__ == '__main__':
    unittest.main()
