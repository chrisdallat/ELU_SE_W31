import unittest
from shopping_cart import calculate_total

class TestShoppingCart(unittest.TestCase):

    def test_calculate_with_empty_cart(self):
        cart = []
        result = calculate_total(cart)
        self.assertEqual(result, 0.0)  # Should show 0.0

    def test_calculate_with_one_item(self):
        cart = [{'name': 'Item A', 'price': 10.99}]
        result = calculate_total(cart)
        self.assertEqual(result, 10.99)  # should show price of single item

    def test_calculate_with_multiple_items(self):
        cart = [
            {'name': 'Item A', 'price': 10.99},
            {'name': 'Item B', 'price': 5.99},
            {'name': 'Item C', 'price': 8.49}
        ]
        result = calculate_total(cart)
        self.assertEqual(result, 25.47)  # Should show correct total for all items in cart

    def test_calculate_with_negatives(self):

        cart = [
            {'name': 'Item A', 'price': -5.0},
            {'name': 'Item B', 'price': -10.99},
        ]
        result = calculate_total(cart)
        self.assertEqual(result, -15.99)  # Should show a negative price which can be checked to display an error or something.

if __name__ == '__main__':
    unittest.main()
