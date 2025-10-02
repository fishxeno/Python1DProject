class products:
    def __init__(self):
        self.items = []
        
    def add_product(self, product: dict[str, str, int, str]):
        self.items.append({"name": product["name"], "details": product["details"], "price": product["price"], "image": product["image"]})

    def list_products(self):
        return self.items

class discounted_products(products):
    def __init__(self, discount: float):
        super().__init__()
        self.discount = discount

    def apply_discount(self):
        for item in self.items:
            item["details"] += f" (Discounted by {self.discount*100}%)"