import random
import numpy as np

m, n = 7, 4
matrix = np.array([[random.randrange(-10, 10) for i in range(m)] for j in range(n)])
print(matrix)
Sum = 0
check = False
coordinates = [[0, 0], [0, 0], [0, 0], [0, 0]]


def sum_func(x1, x2, x3, x4, x5, x6, x7, x8):
    global matrix, Sum, coordinates, check

    temp = []
    for i in range(x1, x5 + 1):
        for j in range(x2, x4 + 1):
            if (i == x1 or i == x3 or i == x5 or i == x7) and (j == x2 or j == x4 or j == x6 or j == x8):
                pass
            else:
                temp.append(matrix[i][j])

    if not check:
        check = True
        if len(temp) > 0:
            Sum = sum(temp)
            coordinates[0] = [x1, x2]
            coordinates[1] = [x3, x4]
            coordinates[2] = [x5, x6]
            coordinates[3] = [x7, x8]
            return
    else:
        if sum(temp) > Sum and len(temp) > 0:
            Sum = sum(temp)
            coordinates[0] = [x1, x2]
            coordinates[1] = [x3, x4]
            coordinates[2] = [x5, x6]
            coordinates[3] = [x7, x8]



for i1 in range(n - 1):
    for j1 in range(m - 1):
        i2 = i1
        for j2 in range(j1 + 1, m):
            for i3 in range(i1 + 1, n):
                j3 = j1
                i4 = i3
                j4 = j2
                sum_func(i1, j1, i2, j2, i3, j3, i4, j4)

print(coordinates)
print(Sum)