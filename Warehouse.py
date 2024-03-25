import uuid


class Product:
    def __init__(self, product_name, price):
        self.product_id = self.get_id()
        self.product_name = product_name
        self.price = price

    def __repr__(self):
        return f"Product(product_name='{self.product_name}', price={self.price})"
    
    def __str__(self):
        return f'Product Name: {self.product_name} | Price: {self.price}'

    @staticmethod
    def get_id():
        return str(uuid.uuid4().fields[-1])[:6]
    

class Warehouse:
    def __init__(self):
        self.products = []
        
    def add_product(self, product_name, price):
        product_names = [product.product_name for product in self.products]
        if product_name not in product_names:
            self.products.append(Product(product_name, price))
        else:
            print(f'The product {product_name} already exists in warehouse.')
    
    def remove_product(self, product_name):
        for product in self.products:
            if product.product_name == product_name:
                self.products.remove(product)
                print(f'Product {product_name} has been removed from warehouse.')
                return
        print(f'The product {product_name} does not exist in warehouse.')
    
    def display_products(self):
        if not self.products:
            print('Warehouse is empty.')
        else:
            print('Products in warehouse:')
            for product in self.products:
                print(product)
            
    def sort_by_price(self, ascending = True):
        sorted_products = sorted(
            self.products, 
            key=lambda x: x.price, 
            reverse=not ascending)
        print('Sorted products by price:')
        for product in sorted_products:
            print(product)
            
    def sort_by_name(self, ascending = True):
        sorted_products = sorted(
            self.products, 
            key=lambda x: x.product_name, 
            reverse=not ascending)
        print('Sorted products by name:')
        for product in sorted_products:
            print(product)
            
        
    def search_product(self, query):
        found_products = [
            prod for prod in self.products 
            if query in prod.product_name
            ]
        if found_products:
            print('Product found:')
            for product in found_products:
                print(product)
        else:
            print('No matching products found.')
 
warehouse = Warehouse()
warehouse.add_product('Laptop', 3900.0)
warehouse.add_product('Mobile Phone', 1990.0)
warehouse.add_product('Camera', 2900.0)
warehouse.add_product('USB Cable', 24.9)
warehouse.add_product('Mouse', 49.0)


                
        
            
    
