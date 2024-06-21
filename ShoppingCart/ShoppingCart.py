"""
Zadanie 8: Klasa ShoppingCart i Product
Stwórz klasę Product, która przechowuje nazwę produktu i cenę.
Następnie stwórz klasę ShoppingCart, która przechowuje listę produktów i
ma metody do dodawania i usuwania produktów z koszyka oraz obliczania całkowitej wartości koszyka.
"""

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}"

class ShoppingCart:
    def __init__(self):
        self.product_list = []

    def add_product(self, product):
        self.product_list.append(product)
        return f'The {product} added to the list.'

    def remove_product(self, product):
        if product in self.product_list:
            self.product_list.remove(product)
            return f'The {product} has been removed.'
        else:
            return f'The {product} is not listed.'

    def total_cost(self):
        total = sum(product.price for product in self.product_list)
        return f'Total cost: {total}'

product1 = Product('Rice', 2.99)
product2 = Product('Cheese', 5.59)
sh = ShoppingCart()
print(sh.add_product(product1))
print(sh.add_product(product2))
print(sh.remove_product(product1))
print(sh.total_cost())
