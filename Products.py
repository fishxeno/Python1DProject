# Product Class
class Product:
    def __init__(self, name: str = "Default", details: str = "Default Description",
                 price: float = 0, image: str = None, stock: int = 0):
        self.name = name
        self.details = details
        self.price = price
        self.priceAfterDiscount = self.price * .95
        self.image = image if not None else "./images/default.png"
        self.stock = stock

    def updateStock(self, stock: int):
        self.stock = max(0, self.stock+stock)
