from catalog.models import product
from django.conf import settings


class Cart():


    def __init__(self, request, obj = {}):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = obj
        self.cart = cart

    def add(self, product):

        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {
                'weight': 100,
                'price': product.price
                }
        else:
            self.cart[product_id]['weight'] += 100

        print(self.cart)
        self.save()


    def get_total_price(self):
        return sum(item['weight'] * item['price'] for item in self.cart.values())


    def __len__(self):
         return len(self.cart)

    def lenght(self):
        return len(self.cart)

    def remove(self, product):

        product_id = product.id

        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
    
    def __iter__(self):
        product_ids = self.cart.keys()

        products = product.objects.filter(id__in = product_ids)

        for Product in products:
            self.cart[Product.id]['product'] = Product
        for Product in self.cart.values():
            yield Product    



    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True




    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def auth_save(self):
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            return {}
        else:
            return self.cart
