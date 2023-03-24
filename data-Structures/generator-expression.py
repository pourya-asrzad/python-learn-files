from sys import getsizeof

values = (x*2 for x in range(10000))
print("gen",getsizeof(values))

values = [x*2 for x in range(10000)]
print("gen",getsizeof(values))
# for x in values:
#     print(x)