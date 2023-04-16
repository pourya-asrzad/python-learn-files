class Flyer:
    def fly(self):
        pass

class Swimmer:
    def swim(self):
        pass


class FlyingFish(Swimmer,Flyer):
    pass

manager =FlyingFish()
manager.fly()

