# A Python decorator is a specific change to the Python syntax that allows us to more conveniently alter functions and methods (and possibly classes in a future version). 
# This supports more readable applications of the DecoratorPattern but also other uses as well."

# A decorator in Python is any callable object that is used to modify a function or a class.

# This is also called metaprogramming as a part of the program tries to modify another part of the program at compile time.

# def sinterklaas(func):
#     print ("Executing sinterklaas")
#     def inner(x):
#         print("Before calling function " + func.__name__)
#         if (x != "Stijn"):
#             func(x)
#         else:
#             print("Oh oh! Stijn is going to Spain this year")
#         print("After calling function " + func.__name__)
#     return inner

# @sinterklaas
def gift(x):
    print("Delivering a gift to " + x)

if __name__ == '__main__':
    gift("Stijn")
    
    # present = sinterklaas(gift)
    # present("Stijn")