point ={
    "x":1,
    "y":2,
    "x=a":10
}

point_with_dict =dict(x=1,y=2)

if "x=a" in point:
     print(point["x=a"])
    
print(point.get("a",0))

del point["x"]

for key,value in point.items():
     print(value)