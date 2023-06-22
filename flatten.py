def listtype(l):
  return(type(l) == type([]))

def flatten(l):
    result = []
    for item in l:
        if listtype(item):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result
print(flatten([1,2,[3],[4,[5,6]]]))
print(flatten([1,2,3,(4,5,6)]))