class Shop:
    def __init__(self, name):
        self.name = name
        self.cart = []

    def add_to_cart(self, item, price, quantity):
        product = {'item': item, 'price': price, 'quantity': quantity}
        self.cart.append(product)

    def remove_from_cart(self, item_name):
        for product in self.cart:
            if product['item'].lower() == item_name.lower():
                self.cart.remove(product)
                print(f"{item_name} removed from cart.")
                return
        print(f"{item_name} not found in cart.")

    def checkout(self, amount):
        total = 0
        for item in self.cart:
            total += item['price'] * item['quantity']
        print('Total price: ', total)
        if amount < total:
            print(f'Please provide {total - amount} more')
        else:
            extra = amount - total
            print(f'Here is your items and extra money {extra}')

nahid = Shop('Nahid')
nahid.add_to_cart('alu', 20, 6)
nahid.add_to_cart('dim', 12, 24)
nahid.add_to_cart('rice', 50, 5)

print("\nCart before removing:")
print(nahid.cart)

# Remove an item
nahid.remove_from_cart('dim')

print("\nCart after removing:")
print(nahid.cart)

# Checkout
nahid.checkout(800)
