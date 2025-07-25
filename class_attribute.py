class shop:
    cart = [] #cart is a class attribute
    def __init__(self,buyer):
        self.buyer = buyer
    
    def add_to_cart(self, item):
        self.cart.append(item)

nahid = shop('nahidur')
nahid.add_to_cart('phone')
nahid.add_to_cart('shoes')
print(nahid.cart)
rouf = shop('abdur rouf')
rouf.add_to_cart('laptop')
rouf.add_to_cart('car')
print(rouf.cart)