def splitsum(l):
    pos = 0  # sum of squares of positive numbers
    neg = 0  # sum of cubes of negative numbers

    for num in l:
        if num > 0:
            pos += num ** 2
        elif num < 0:
            neg += num ** 3

    return [pos, neg]

print(splitsum([1,3,-5]))
print(splitsum([2,4,6]))
print(splitsum([-19,-7,-6,0]))
print(splitsum([-1,2,3,-7]))