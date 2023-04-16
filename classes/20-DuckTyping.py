from abc import ABC,abstractmethod


class TextBox():
    def draw(self):
        print("TextBox")



class DropDownList():
    def draw(self):
        print("DropDownList")

def draw(controls):
    for control in controls:
       control.draw()

ddl = DropDownList()
textBox = TextBox()
draw([ddl,textBox])