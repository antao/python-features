# Filter (Extracts each element in the sequence for which the function returns True)
# filter(aFunction, aSequence)

if __name__ == '__main__':
    items = range(-10,10)

    negatives = []
    for x in items:
        if x < 0:
            negatives.append(x)
    print(negatives)

    # print(list(filter(lambda x: x < 0, items)))
