try:
   age = int(input("Age: "))
except ValueError as ex:
   print(ex)
   print("You didn't enter a valid age.")
else:
   print("No exceptions were throw.")

print("Execution continues.")