from Entity.products import Product
class Clothing(Product):
    def __init__(self, productId, productName, description, price, quantityInStock, size, color):
        super().__init__(productId, productName, description, price, quantityInStock, "Clothing")
        self.size = size
        self.color = color
    
    def getSize(self):
        return self.size
    
    def setSize(self, size):
        self.size = size
    
    def getColor(self):
        return self.color
    
    def setColor(self, color):
        self.color = color
