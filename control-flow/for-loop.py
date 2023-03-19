for number in range(1,10,2):
    print("Atempt",number,number*".")


count =0
for num in range(1,10):
    if num % 2 == 0:
        count+=1
        print(num)
print(F"we have {count} even numbers")