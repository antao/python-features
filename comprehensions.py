# Comprehensions apply an arbitrary expression over an iterable object. 
# Represents an elegant way of Python's for implementing a well-known mathematic notation: { x2 | x ∈ ℕ }

# Read: http://python-history.blogspot.nl/2010/06/from-list-comprehensions-to-generator.html

def exponencial():
    squares = []
    for x in range(10):
        squares.append(x ** 2) # exponencial basic operator
    print (squares)

if __name__ == '__main__':
    exponencial()
    
    # List comprehension example
    print([x ** 2 for x in range(10)])

    # You can iterate for any sequence
    print([(a + b) for a in 'funda' for b in 'adnuf'])

    # Or write the for loops (more verbose, imho)
    words = []
    for a in 'funda':
        for b in 'adnuf':
            words.append(a + b)
    print (words)

    # Did I mentioned conditionals?
    print([x for x in range(10) if (x % 2 == 0)])

    # Dictionary comprehensions from > 2.7
    dictionary = { 'a': 1, 'b': 2, 'c': 3 }
    print({value:key for key, value in dictionary.items()})
