class products:
    
    def __init__(self):
        self.items:list[dict] = [{"name": "Sample Product", "details": "This is a sample product."}]

    def add_product(self, product: dict[str, str]):
        self.items.append({"name": product["name"], "details": product["details"]})

    def list_products(self):
        return self.items