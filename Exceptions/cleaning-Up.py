# try:
#    file = open("cleaning-Up.py")
#    age = int(input("Age: "))
#    xfactor =10/age
# except (ValueError,ZeroDivisionError):
#    print("You didn't enter a valid age.")
# else:
#    print("No exceptions were throw.")
# finally:
#    file.close()


###############
# with


try:
   with open("cleaning-Up.py") as file,open("onother.txt") as target:
      print("File opened.")
   age = int(input("Age: "))
   xfactor =10/age
except (ValueError,ZeroDivisionError):
   print("You didn't enter a valid age.")
else:
   print("No exceptions were throw.")
