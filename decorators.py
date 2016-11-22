# "The "decorators" we talk about with concern to Python are not exactly the same thing as the DecoratorPattern described above. 
# A Python decorator is a specific change to the Python syntax that allows us to more conveniently alter functions and methods (and possibly classes in a future version). This supports more readable applications of the DecoratorPattern but also other uses as well. "

# This is also called metaprogramming as a part of the program tries to modify another part of the program at compile time.

# def chained_decorator(func):
#     def inner():
#         print("I chained decoreted object")
#         func()
#     return inner

def decorator(func):
    def inner():
        print("I am a decoreted object")
        func()
    return inner

# @decorator
def my_function():
    print("I am an object")

if __name__ == '__main__':
    my_function()
    other_function = decorator(my_function)
    other_function()
    
