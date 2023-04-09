class Animal:
    def __init__(self):
        self.age =1


    def eat(self):
        print('eat')


# Animal : Parent , Base 
# Mammal : Child , Base 

class Mammal(Animal):
    def walk(self):
        print("walk")


        


m =Mammal()
print(isinstance(m,Animal),"isinstance")
print(issubclass(Mammal,Animal),"issubclass")
print(issubclass(Animal,Mammal),"issubclass")

# m > Mammal > Animal > object 