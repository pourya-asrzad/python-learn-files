items =[
    ('Product1',10),
    ('Product2',9),
    ('Product3',12),
]

price =list(filter(lambda item:item[1]>=10,items))
print(price)