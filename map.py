# Map applies a function call to each item instead of an arbitrary expression like in comprehensions
# map(aFunction, aSequence)

def square(x): 
    return (x ** 2)

def cube(x): 
    return (x ** 3)

if __name__ == '__main__':
    items = [1, 2, 3, 4, 5]

    # Using map 
    print(list(map(square, items)))

    # Lambda routines can also be passed in map as aFunction
    print(list(map((lambda x: x ** 2), items)))

    # Or even combined functions
    funcs = [square, cube]
    for r in items:
        print(list(map(lambda x: x(r), funcs)))
    
