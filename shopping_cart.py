"""
ELU WEEK 31 Linting assignment, Chris Dallat
"""
def CalculateTotal(cart):
    """
    Funtion to calculate the total price of items in cart
    """
    total = 0
    for item in cart:
        total += item['price']
    return total


def display_total(Total):
    """
    Funtion to print out the resulting total
    """
    print("Total price: " + Total)


CART = [
    {'name': 'Item A', 'price': 10.99},
    {'name': 'Item B', 'price': 5.99},
    {'name': 'Item C', 'price': '8.49'}
]

for item in CART:
    print(f"Item: {item['name']} - Price: ${item['price']}")

shopping_cart_total = CalculateTotal(CART)
display_total(shopping_cart_total)
