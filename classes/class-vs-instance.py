# class Point:
#     default_color="red"

#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
    
#     def draw(self):
#         print(f"Point ({self.x},{self.y})")


# Point.default_color="Yellow"
# point=Point(1,2)
# point.draw()
# print(point.default_color)

# another=Point(3,4)
# another.draw()


#methods

class Point:

    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    @classmethod
    def zero(cls):
        return cls(0,0)

            
    def draw(self):
        print(f"Point ({self.x},{self.y})")



point=Point.zero()
point.draw()