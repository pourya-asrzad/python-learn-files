class Animal:
    def __init__(self):
        print('animal ')
        self.age =1


    def eat(self):
        print('eat')


# Animal : Parent , Base 
# Mammal : Child , Base 

class Mammal(Animal):
    def __init__(self):
        print('Mammul ')
        self.weight =2
        super().__init__()

    def walk(self):
        print("walk")


        

m =Mammal()
# m.eat()
print(m.age)
print(m.weight)