def binary_search(list,item):
    low=0
    higth=len(list) -1

    while low <= higth:
        mid =int((low+higth)/2) # mid = 2
        guess= list[mid]
        print(guess)
        if guess == item:
            return mid
        if guess > item:  
            higth = mid-1 
        else:# true
            low = mid +1 # low = 2+1 = 3

    return None


my_list =[1,3,5,7,9]

print(binary_search(my_list,10))