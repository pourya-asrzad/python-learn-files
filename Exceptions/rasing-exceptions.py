# def calculate_xfactor(age):
#     if age <= 0:
#         raise ValueError("age can not be 0 or less.")
#     return 10/age

# try:
#     calculate_xfactor(-1)
# except ValueError as error:
#     print(error)


###################
# cost of rasing


from timeit import timeit


code1 ="""
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("age cannot be 0 or less.")
    return 10/age

try:
    calculate_xfactor(-1)
except ValueError as error:
    pass
"""

code2="""
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10/age

    
xfactor = calculate_xfactor(-1)
if xfactor == None:
    pass
"""

print('first code',timeit(code1,number=10000))
print('first code',timeit(code2,number=10000))