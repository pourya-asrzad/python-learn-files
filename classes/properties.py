class Product:
    def __init__(self,price):
        self.price = price
    
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self,value):
        if value < 0 :
            raise ValueError("price must be bigger than 0")
            
        self.__price = value
    

        
    


product =Product(10)
product.price =-10
print(product.price)