def remdup(l):
    """Removes duplicates in l, keeping only the last occurrence of each number."""
    seen = set()
    result = []
    for x in reversed(l):
        if x not in seen:
            result.append(x)
            seen.add(x)
    result.reverse()
    return result
print(remdup([3,1,3,5]))
print(remdup([7,3,-1,-5]))
print(remdup([3,5,7,5,3,7,10]))