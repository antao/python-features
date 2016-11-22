# Comprehensions apply an arbitrary expression over an iterable object 

# For loop example
squares = []
for x in range(10):
    squares.append(x ** 2)
print (squares)

# List comprehension example
a = [x ** 2 for x in range(10)]
print (a)

# You can iterate for any sequence
print([(a + b) for a in 'funda' for b in 'adnuf'])

# Or write the for loops (more verbose, imho)
words = []
for a in 'funda':
    for b in 'adnuf':
        words.append(a + b)
print (words)

# Did I mentioned conditionals ?
print([x for x in range(10) if (x % 2 == 0)])

# Dictionary comprehensions from > 2.7
b = { 'a': 1, 'b': 2, 'c': 3 }
print({value:key for key, value in b.items()})
