# Filter (Extracts each element in the sequence for which the function returns True)
# filter(aFunction, aSequence)

if __name__ == '__main__':
    negatives = []
    for x in range(-10,10):
        if x < 0:
            negatives.append(x)
    print(negatives)

    # Using a filter
    print(list(filter(lambda x: x < 0, range(-10,10))))
