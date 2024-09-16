def get_matrix(n, m, value):
    matrix = []

    for i in range(n):
        row = []

        for j in range(m):
            row.append(value)
        matrix.append(row)

    return matrix

result1 = get_matrix(3, 4, 7)
result2 = get_matrix(2, 5, 1)
result3 = get_matrix(6, 2, 54)

print(result1)
print(result2)
print(result3)
