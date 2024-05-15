from Entity.products import Product
class Electronics(Product):

    def __init__(self, productId, productName, description, price, quantityInStock, brand, warrantyPeriod):
        super().__init__(productId, productName, description, price, quantityInStock, "Electronics")
        self.brand = brand
        self.warrantyPeriod = warrantyPeriod
    
    def getBrand(self):
        return self.brand
    
    def setBrand(self, brand):
        self.brand = brand
    
    def getWarrantyPeriod(self):
        return self.warrantyPeriod
    
    def setWarrantyPeriod(self, warrantyPeriod):
        self.warrantyPeriod = warrantyPeriod
    