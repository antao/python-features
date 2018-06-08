def memoize(f):
    def memf(*x):
        if x not in memf.cache: 
            memf.cache[x] = f(*x) 
        return memf.cache[x] 
    memf.cache = {} 
    return memf

def square(x): 
    return (x ** 2)

if __name__ == '__main__':
    square = memoize(square)
    print(square(2))