class Point:
    def __init__(self,x,y):#python3 magic methods
        self.x=x
        self.y=y

        
    def __str__(self):
        return f"({self.x},{self.y})"

    def draw(self):
        print(f"Point ({self.x},{self.y})")


point=Point(1,2)
# point.__str__
print(point)