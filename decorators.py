# "The "decorators" we talk about with concern to Python are not exactly the same thing as the DecoratorPattern described above. 
# A Python decorator is a specific change to the Python syntax that allows us to more conveniently alter functions and methods (and possibly classes in a future version). This supports more readable applications of the DecoratorPattern but also other uses as well. "

# This is also called metaprogramming as a part of the program tries to modify another part of the program at compile time.

# def sprinkles(func):
#     def inner():
#         print("Chain some sprinkles")
#         func()
#     return inner

def wrap(func):
    def inner():
        print("I will wrap the " +  func.__name__)
        func()
    return inner

# @wrap
def gift():
    print("I am the gift")

if __name__ == '__main__':
    gift()
    present = wrap(gift)
    present()
    
