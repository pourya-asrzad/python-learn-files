def fizz_buzz(number):
    if number % 3 == 0 and number % 5 ==0:
        return"fizzBuzz"
    if number % 5==0:
        return"buzz"
    if number % 3 ==0:
        return"Fizz"
    
    return number
    

print(fizz_buzz(7))