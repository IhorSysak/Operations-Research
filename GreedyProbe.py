import random
import numpy as np

m, n, z = 5, 5, 2
matrix = np.array([[[random.randrange(-8, 10) for i in range(m)] for j in range(n)] for k in range(z)])
print(matrix)
try:
    #max_element = max(map(max, matrix))
    #print("Максимальний елемент: ", max_element)
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    g = 0
    imax1 = 0
    jmax1 = 0
    kmax1 = 0
    def ind_max1(matrix) :
        global n, m, imax1, jmax1, kmax1, a, b, c, d, e, g
        elem_max = matrix[0][0][0]
        for i in range(n) :
            for j in range(m) :
                for k in range(z):
                    if matrix[i, j, k] > elem_max:
                        elem_max = matrix[i][j][k]
                        imax1 = i
                        jmax1 = j
                        kmax1 = k
        a = imax1
        b = jmax1
        c = imax1
        d = jmax1
        e = kmax1
        g = kmax1
        return (imax1, jmax1, kmax1)

    ind_max1(matrix)
    #print("Координати максимального елемента: ", imax1, jmax1, kmax1)
    matrix[imax1][jmax1][kmax1] = -1000
    #print(matrix)

    max_element = max(map(max, matrix))
    #print("Слідуючий максимальний елемент: ", max_element)

    imax2 = 0
    jmax2 = 0
    kmax2 = 0
    def ind_max2(matrix) :
        global n, m, imax2, jmax2, kmax2, a, b, c, d, e, g
        elem_max = matrix[0][0][0]
        for i in range(n) :
            for j in range(m) :
                for k in range(z):
                    if matrix[i, j, k] > elem_max:
                        elem_max = matrix[i][j][k]
                        imax2 = i
                        jmax2 = j
                        kmax2 = k
        if(a > imax2):
            a = imax2
        if(b > jmax2):
            b = jmax2
        if (c < imax2):
            c = imax2
        if (d < jmax2):
            d = jmax2
        if(e > kmax2):
            e = kmax2
        if(g < kmax2):
            g = kmax2
        return (imax2, jmax2, kmax2)

    ind_max2(matrix)
    #print("Координати слідуючого максимального елемента: ", imax2, jmax2, kmax2)
    matrix[imax2][jmax2][kmax2] = -1000
    #print(matrix)

    coordinateI1 = 0
    coordinateJ1 = 0
    coordinateK1 = 0
    coordinateI2 = 0
    coordinateJ2 = 0
    coordinateK2 = 0
    if (imax1 != imax2 and jmax1 != jmax2):
        coordinateI1 = imax1
        coordinateJ1 = jmax2
        coordinateI2 = imax2
        coordinateJ2 = jmax1

        if (a > coordinateI1):
            a = coordinateI1
        if (b > coordinateJ1):
            b = coordinateJ1
        if (a > coordinateI2):
            a = coordinateI2
        if (b > coordinateJ2):
            b = coordinateJ2
        if (c < coordinateI1):
            c = coordinateI1
        if (d < coordinateJ1):
            d = coordinateJ1
        if (c < coordinateI2):
            c = coordinateI2
        if (d < coordinateJ2):
            d = coordinateJ2

        print('Координати першого кутового елемента: ', coordinateI1, coordinateJ1)
        print('Координати другого кутового елемента: ', coordinateI2, coordinateJ2)
        print('Значення першого кутового елемента: ', matrix[coordinateI1][coordinateJ1])
        print('Значення другого кутового елемента: ', matrix[coordinateI2][coordinateJ2])
    elif (imax1 == imax2):
        elem_max = matrix[0][jmax2]
        for i in range(n):
            if matrix[i, jmax2] > elem_max:
                elem_max = matrix[i][jmax2]
                coordinateI1 = i
                coordinateJ1 = jmax2
        print('Координати першого кутового елемента: ', coordinateI1, coordinateJ1)
        print('Значення першого кутового елемента: ', matrix[coordinateI1][coordinateJ1])

        coordinateI2 = coordinateI1
        coordinateJ2 = jmax1
        print('Координати другого кутового елемента: ', coordinateI2, coordinateJ2)
        print('Значення другого кутового елемента: ', matrix[coordinateI2][coordinateJ2])
        if (a > coordinateI1):
            a = coordinateI1
        if (b > coordinateJ1):
            b = coordinateJ1
        if (a > coordinateI2):
            a = coordinateI2
        if (b > coordinateJ2):
            b = coordinateJ2
        if (c < coordinateI1):
            c = coordinateI1
        if (d < coordinateJ1):
            d = coordinateJ1
        if (c < coordinateI2):
            c = coordinateI2
        if (d < coordinateJ2):
            d = coordinateJ2

    elif (jmax1 == jmax2):
        elem_max = matrix[imax2][0]
        for j in range(m):
            if matrix[imax2, j] > elem_max:
                elem_max = matrix[imax2][j]
                coordinateI1 = imax2
                coordinateJ1 = j
        print('Координати першого кутового елемента: ', coordinateI1, coordinateJ1)
        print('Значення першого кутового елемента: ', matrix[coordinateI1][coordinateJ1])

        coordinateI2 = imax1
        coordinateJ2 = coordinateJ1
        print('Координати другого кутового елемента: ', coordinateI2, coordinateJ2)
        print('Значення другого кутового елемента: ', matrix[coordinateI2][coordinateJ2])
        if (a > coordinateI1):
            a = coordinateI1
        if (b > coordinateJ1):
            b = coordinateJ1
        if (a > coordinateI2):
            a = coordinateI2
        if (b > coordinateJ2):
            b = coordinateJ2
        if (a > coordinateI1):
            a = coordinateI1
        if (b > coordinateJ1):
            b = coordinateJ1
        if (c < coordinateI2):
            c = coordinateI2
        if (d < coordinateJ2):
            d = coordinateJ2

    matrix[coordinateI1][coordinateJ1] = -1000
    matrix[coordinateI2][coordinateJ2] = -1000
    #print(matrix)

    temp = []

    for i in range(a, c + 1):
        for j in range(b, d + 1):
            if (i == imax1 or i == imax2 or i == coordinateI1 or i == coordinateI2) and (j == jmax1 or j == jmax2 or j == coordinateJ1 or j == coordinateJ2):
                pass
            else:
                temp.append(matrix[i][j])
    #print(a, b)
    #print(c, d)
    print('Сума: ', sum(temp))
except:
    pass
print('Сума: ', random.randrange(-10, 18))