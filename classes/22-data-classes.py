from collections import namedtuple

Point =namedtuple("Point",["x","y"])
p1 =Point(x=1,y=2)
p2 =Point(x=1,y=2)
print(Point)
print(p1==p2)