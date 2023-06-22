def leftrotate(m):
    rotated_matrix = []
    n = len(m)

    for i in range(n):
        row = [m[j][i] for j in range(n-1, -1, -1)]
        rotated_matrix.append(row)

    return rotated_matrix

print(leftrotate([[1,2],[3,4]]))
print(leftrotate([[1,2,3],[4,5,6],[7,8,9]]))
print(leftrotate([[1,1,1],[2,2,2],[3,3,3]]))