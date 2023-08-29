"""
ELU WEEK 31 Linting assignment, Chris Dallat
"""
def calculate_total(cart):
    """
    Funtion to calculate the total price of items in cart
    """
    total = 0
    for item in cart:
        total += item['price']
    return total


def display_total(total):
    """
    Funtion to print out the resulting total
    """
    print("Total price: " + total)


CART = [
    {'name': 'Item A', 'price': 10.99},
    {'name': 'Item B', 'price': 5.99},
    {'name': 'Item C', 'price': '8.49'}
]

for item_in_cart in CART:
    print(f"Item: {item_in_cart['name']} - Price: ${item_in_cart['price']}")

shopping_cart_total = calculate_total(CART)
display_total(shopping_cart_total)
