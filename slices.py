# list[start:end]

l = ['f', 'u', 'n', 'd', 'a']

# Take items from 1 to 4, upper bound non-inclusive
print(l[1:4]) 

# Take all items except the last
print(l[0:-1])

# Reverse the list
print(l[::-1])

# Copy all items of a list
b = l[:]
print(l)
print(b)

# Skip the last item 
print(l[:-1])

# "One way to remember how slices work is to think of the indices as pointing between characters, with the left edge of the first character numbered 0."

# +---+---+---+---+---+
# | f | u | n | d | a |
# +---+---+---+---+---+
# 0   1   2   3   4   5
#-5  -4  -3  -2  -1