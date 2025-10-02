class products:
    
    def __init__(self):
        self.items:list[dict] = [{"name": "Sample Product", "details": "This is a sample product."}]

    def add_product(self, product: dict):
        self.items.append({"name": product["name"], "details": product["details"]})

    def list_products(self):
        return self.items

    def remove_product(self, product):
        self.items.remove(product)
    
    def clear_products(self):
        self.items = []
    
    def count_products(self):
        return len(self.items)
    
    def find_product(self, product):
        return product in self.items
    
    def get_product_details(self, product):
        if product in self.items:
            return {"name": product, "details": "Details about " + product}
        else:
            return None
        
    def update_product(self, old_product, new_product):
        if old_product in self.items:
            index = self.items.index(old_product)
            self.items[index] = new_product
            return True
        return False
    
    def sort_products(self):
        self.items.sort()
        
    def reverse_products(self):
        self.items.reverse()