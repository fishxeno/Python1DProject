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

# Product Class
class Product:
    def __init__(self, name: str="Default", details: str="Default Description", 
                 price: float=0, image: str="default.png", stock: int=0):
        self.name = name
        self.details = details
        self.price = price 
        self.priceAfterDiscount = self.price * .95
        self.image = image
        self.stock = stock
    
    def getPrice(self, isMember):
        return self.priceAfterDiscount if isMember else self.price

    def addStock(self, stock:int):
        self.stock += stock

    def removeStock(self, stock:int):
        self.stock = max(0, self.stock-stock)


