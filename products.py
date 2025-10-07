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

# products class
class products:
    def __init__(self):
        self.items = [Product]
        
    def add_product(self, product: Product):
        self.items.append(product.__dict__)

    def list_products(self):
        return self.items