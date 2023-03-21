items =[
    ('Product1',10),
    ('Product2',9),
    ('Product3',12),
]


numbers =[]
# for item in items:
#       numbers.append(item[1])


# print(numbers)

x=list(map(lambda item:item[1],items))

print(x)    
# for item in x:
    

##############
#list comprehensions
prices =[item[1] for item in items]#for map
# print(prices)
filterprices=[item[1] for item in items if item[1] >= 10]
print(filterprices)