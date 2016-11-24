# A decorator in Python is any callable object that is used to modify a function or a class.
# This is also called metaprogramming as a part of the program tries to modify another part of the program at compile time.

# != Decorator Software Design Pattern
# "Decorator is a function that takes another function and extends the behavior of the latter function without explicitly modifying it."
# Further explanation: https://wiki.python.org/moin/PythonDecorators and https://www.python.org/dev/peps/pep-0318/

def sinterklaas(func):
    print ("Executing sinterklaas")
    def inner(x): # Inner is a closure, it captures the actual value of gift
        print("Before calling function " + func.__name__)
        if (x != "Stijn"):
            func(x)
        else:
            print("Oh oh! Stijn is going to Spain this year")
        print("After calling function " + func.__name__)
    return inner

# The @ indicates the application of the decorator sinterklaas (syntax sugar).
@sinterklaas 
def gift(x):
    print("Delivering a gift to " + x)

if __name__ == '__main__':
    gift("Eduardo!!") 
    
    # present = sinterklaas(gift)
    # present("Oriol")