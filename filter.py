## Filter (Extracts each element in the sequence for which the function returns True)

if __name__ == '__main__':
    items = range(-10,10)
    print(list(filter(lambda x: x < 0, items)))