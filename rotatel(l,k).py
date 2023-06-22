def rotatelist(l, k):
    """Returns a new list that is l rotated k times."""
    if k <= 0:
        return l
    n = len(l)  # length of the list
    return [l[(i+k) % n] for i in range(n)]

print(rotatelist([1,2,3,4,5],1))
print(rotatelist([1,2,3,4,5],3))
print(rotatelist([1,2,3,4,5],12))