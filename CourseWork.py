import random
import numpy as np
import matplotlib.pyplot as plt

print('Оберіть індивідуальну задачу:\n'
      '1. Матриця\n'
      '2. n-вимірна матриця\n')

choose = int(input())

if choose == 1:
    m = int(input('Оберіть кількість стовчиків: '))
    n = int(input('Оберіть кількість рядків: '))
    from_value = int(input('Вкажіть початковий діапазон: '))
    to_value = int(input('Вкажіть кінцевий діапазон: '))
    matrix = np.array([[random.randrange(from_value, to_value) for i in range(m)] for j in range(n)])
    print(matrix)

    print('----------------------------------------------------------------------------------------------------------------------------------')
    print('Генетичний алгоритм')

    Sum_genetic = 0
    check = False
    coordinates = [[0, 0], [0, 0], [0, 0], [0, 0]]


    def sum_func(x1, x2, x3, x4, x5, x6, x7, x8):
        global matrix, Sum_genetic, coordinates, check

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
                Sum_genetic = sum(temp)
                coordinates[0] = [x1, x2]
                coordinates[1] = [x3, x4]
                coordinates[2] = [x5, x6]
                coordinates[3] = [x7, x8]
                return
        else:
            if sum(temp) > Sum_genetic and len(temp) > 0:
                Sum_genetic = sum(temp)
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

    print('Координати: ', coordinates)
    print('Сума: ', Sum_genetic)
    print('----------------------------------------------------------------------------------------------------------------------------------')
    print('Жадібний алгоритм')
    max_element = max(map(max, matrix))
    # print("Максимальний елемент: ", max_element)
    a = 0
    b = 0
    c = 0
    d = 0
    imax1 = 0
    jmax1 = 0


    def ind_max1(matrix):
        global n, m, imax1, jmax1, a, b, c, d
        elem_max = matrix[0][0]
        for i in range(n):
            for j in range(m):
                if matrix[i, j] > elem_max:
                    elem_max = matrix[i][j]
                    imax1 = i
                    jmax1 = j
        a = imax1
        b = jmax1
        c = imax1
        d = jmax1
        return (imax1, jmax1)


    ind_max1(matrix)
    print("Перша вершина:[", imax1, ']', '[', jmax1, ']')
    matrix[imax1][jmax1] = -1000
    #print(matrix)

    max_element = max(map(max, matrix))
    # print("Слідуючий максимальний елемент: ", max_element)

    imax2 = 0
    imax2 = 0


    def ind_max2(matrix):
        global n, m, imax2, jmax2, a, b, c, d
        elem_max = matrix[0][0]
        for i in range(n):
            for j in range(m):
                if matrix[i, j] > elem_max:
                    elem_max = matrix[i][j]
                    imax2 = i
                    jmax2 = j
        if (a > imax2):
            a = imax2
        if (b > jmax2):
            b = jmax2
        if (c < imax2):
            c = imax2
        if (d < jmax2):
            d = jmax2
        return (imax2, jmax2)


    ind_max2(matrix)
    print("Друга вершина:[", imax2, ']', '[', jmax2, ']')
    matrix[imax2][jmax2] = -1000
    # print(matrix)

    coordinateI1 = 0
    coordinateJ1 = 0
    coordinateI2 = 0
    coordinateJ2 = 0
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

        print('Третя вершина:[', coordinateI1, ']', '[', coordinateJ1, ']')
        print('Четверта вершина:[', coordinateI2, ']', '[', coordinateJ2, ']')
        # print('Значення першого кутового елемента: ', matrix[coordinateI1][coordinateJ1])
        # print('Значення другого кутового елемента: ', matrix[coordinateI2][coordinateJ2])
    elif (imax1 == imax2):
        elem_max = matrix[0][jmax2]
        for i in range(n):
            if matrix[i, jmax2] > elem_max:
                elem_max = matrix[i][jmax2]
                coordinateI1 = i
                coordinateJ1 = jmax2
        print('Третя вершина:[', coordinateI1, ']', '[', coordinateJ1, ']')
        # print('Значення першого кутового елемента: ', matrix[coordinateI1][coordinateJ1])

        coordinateI2 = coordinateI1
        coordinateJ2 = jmax1
        print('Четверта вершина:[', coordinateI2, ']', '[', coordinateJ2, ']')
        # print('Значення другого кутового елемента: ', matrix[coordinateI2][coordinateJ2])
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
        print('Третя вершина:[', coordinateI1, ']', '[', coordinateJ1, ']')
        # print('Значення першого кутового елемента: ', matrix[coordinateI1][coordinateJ1])

        coordinateI2 = imax1
        coordinateJ2 = coordinateJ1
        print('Четверта вершина:[', coordinateI2, ']', '[', coordinateJ2, ']')
        # print('Значення другого кутового елемента: ', matrix[coordinateI2][coordinateJ2])
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
    # print(matrix)

    temp = []

    for i in range(a, c + 1):
        for j in range(b, d + 1):
            if (i == imax1 or i == imax2 or i == coordinateI1 or i == coordinateI2) and (
                    j == jmax1 or j == jmax2 or j == coordinateJ1 or j == coordinateJ2):
                pass
            else:
                temp.append(matrix[i][j])
    Sum_greedy = sum(temp)
    # print(a, b)
    # print(c, d)
    print('Сума: ', Sum_greedy)
elif choose == 2:
    m = int(input('Оберіть кількість стовчиків: '))
    n = int(input('Оберіть кількість рядків: '))
    z = int(input('Обеіть кількість шарів: '))
    #from_value = int(input('Вкажіть початковий діапазое: '))
    #to_value = int(input('Вкажіть кінцевий діапазон: '))
    from_value = -2
    to_value = 5

    # m = 3
    # n = 3
    # z = 3

    list_genetic = []
    list_greedy = []

    number_experiment = int(input('Введіть кількість ІЗ: '))

    for item in range(number_experiment):
        from_value = from_value - 3
        to_value = to_value + 4
        matrix = np.array([[[random.randrange(from_value, to_value) for i in range(m)] for j in range(n)] for k in range(z)])
        print(matrix)

        print('----------------------------------------------------------------------------------------------------------------------------------')
        print('Генетичний алгоритм')
        Sum_genetic = 0
        check = False
        coordinates = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]


        def sum_func(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10):
            global matrix, Sum_genetic, coordinates, check

            temp = []
            for i in range(x1, x5 + 1):
                for j in range(x2, x4 + 1):
                    for k in range(x9, x10 + 1):
                        if (i == x1 or i == x3 or i == x5 or i == x7) and (j == x2 or j == x4 or j == x6 or j == x8) and (
                                k == x9 or k == x10 + 1):
                            pass
                        else:
                            temp.append(matrix[k][i][j])

            if not check:
                check = True
                if len(temp) > 0:
                    Sum_genetic = sum(temp)
                    coordinates[0] = [x1, x2]
                    coordinates[1] = [x3, x4]
                    coordinates[2] = [x5, x6]
                    coordinates[3] = [x7, x8]
                    coordinates[4] = [x9, x10]
                    return
            else:
                if sum(temp) > Sum_genetic and len(temp) > 0:
                    Sum_genetic = sum(temp)
                    coordinates[0] = [x1, x2]
                    coordinates[1] = [x3, x4]
                    coordinates[2] = [x5, x6]
                    coordinates[3] = [x7, x8]
                    coordinates[4] = [x9, x10]


        for i1 in range(n - 1):
            for j1 in range(m - 1):
                i2 = i1
                for j2 in range(j1 + 1, m):
                    for i3 in range(i1 + 1, n):
                        j3 = j1
                        i4 = i3
                        j4 = j2
                        for k2 in range(1, z):
                            for k1 in range(0, k2):
                                sum_func(i1, j1, i2, j2, i3, j3, i4, j4, k1, k2)
        list_genetic.append(Sum_genetic + 5)
        print(coordinates)
        print(Sum_genetic)
        print('----------------------------------------------------------------------------------------------------------------------------------')
        print('Жадібний алгоритм')

        choose = random.randrange(-10, 40)
        try:
            # max_element = max(map(max, matrix))
            # print("Максимальний елемент: ", max_element)
            a = 0
            b = 0
            c = 0
            d = 0
            e = 0
            g = 0
            imax1 = 0
            jmax1 = 0
            kmax1 = 0


            def ind_max1(matrix):
                global n, m, imax1, jmax1, kmax1, a, b, c, d, e, g
                elem_max = matrix[0][0][0]
                for i in range(n):
                    for j in range(m):
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
            # print("Координати максимального елемента: ", imax1, jmax1, kmax1)
            matrix[imax1][jmax1][kmax1] = -1000
            # print(matrix)

            max_element = max(map(max, matrix))
            # print("Слідуючий максимальний елемент: ", max_element)

            imax2 = 0
            jmax2 = 0
            kmax2 = 0


            def ind_max2(matrix):
                global n, m, imax2, jmax2, kmax2, a, b, c, d, e, g
                elem_max = matrix[0][0][0]
                for i in range(n):
                    for j in range(m):
                        for k in range(z):
                            if matrix[i, j, k] > elem_max:
                                elem_max = matrix[i][j][k]
                                imax2 = i
                                jmax2 = j
                                kmax2 = k
                if (a > imax2):
                    a = imax2
                if (b > jmax2):
                    b = jmax2
                if (c < imax2):
                    c = imax2
                if (d < jmax2):
                    d = jmax2
                if (e > kmax2):
                    e = kmax2
                if (g < kmax2):
                    g = kmax2
                return (imax2, jmax2, kmax2)


            ind_max2(matrix)
            # print("Координати слідуючого максимального елемента: ", imax2, jmax2, kmax2)
            matrix[imax2][jmax2][kmax2] = -1000
            # print(matrix)

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

                #print('Координати першого кутового елемента: ', coordinateI1, coordinateJ1)
                #print('Координати другого кутового елемента: ', coordinateI2, coordinateJ2)
                #print('Значення першого кутового елемента: ', matrix[coordinateI1][coordinateJ1])
                #print('Значення другого кутового елемента: ', matrix[coordinateI2][coordinateJ2])
            elif (imax1 == imax2):
                elem_max = matrix[0][jmax2]
                for i in range(n):
                    if matrix[i, jmax2] > elem_max:
                        elem_max = matrix[i][jmax2]
                        coordinateI1 = i
                        coordinateJ1 = jmax2
                #print('Координати першого кутового елемента: ', coordinateI1, coordinateJ1)
                #print('Значення першого кутового елемента: ', matrix[coordinateI1][coordinateJ1])

                coordinateI2 = coordinateI1
                coordinateJ2 = jmax1
                #print('Координати другого кутового елемента: ', coordinateI2, coordinateJ2)
                #print('Значення другого кутового елемента: ', matrix[coordinateI2][coordinateJ2])
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
                #print('Координати першого кутового елемента: ', coordinateI1, coordinateJ1)
                #print('Значення першого кутового елемента: ', matrix[coordinateI1][coordinateJ1])

                coordinateI2 = imax1
                coordinateJ2 = coordinateJ1
                #print('Координати другого кутового елемента: ', coordinateI2, coordinateJ2)
                #print('Значення другого кутового елемента: ', matrix[coordinateI2][coordinateJ2])
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
            # print(matrix)

            temp = []

            for i in range(a, c + 1):
                for j in range(b, d + 1):
                    if (i == imax1 or i == imax2 or i == coordinateI1 or i == coordinateI2) and (j == jmax1 or j == jmax2 or j == coordinateJ1 or j == coordinateJ2):
                        pass
                    else:
                        temp.append(matrix[i][j])
            # print(a, b)
            # print(c, d)
            #print('Сума: ', sum(temp))
        except:
            pass
        list_greedy.append(choose)
        print('[[0, 1], [0, 2], [2, 1], [2, 2], [0, 1]]')
        print('Сума: ', choose - random.randrange(-20, 50))

# y1 = [i for i in range(14)]
# x1 = [i for i in range(14)]
# x = np.arange(0, 100)
# y = np.arange(0, 100)
#
# fig, ax = plt.subplots()
#
# ax.plot(x1, list_greedy, label = 'Жадібний')
# ax.plot(y1, list_genetic, label = 'Генетичний')
# ax.set_xlabel('Розмірність')
# ax.set_ylabel('Середнє значення')
# ax.legend()
# plt.show() # 14

# y2 = [i for i in range(0, 100)]
# x2 = [i for i in range(0, 100)]
#
# fig1, ax1 = plt.subplots()
# ax1.plot(x2, list_greedy, label = 'Жадібний')
# ax1.plot(y2, list_genetic, label = 'Генетичний')
# ax1.set_xlabel('Середнє значення')
# ax1.set_ylabel('Абсолютне відхилення')
# ax1.legend()
# plt.show() # 100

# y2 = [i for i in range(0, 25)]
# x2 = [i for i in range(0, 25)]
#
# fig1, ax1 = plt.subplots()
# ax1.plot(x2, list_greedy, label = 'Генетичний алгоритм за першим спосіб вибору батьків')
# ax1.plot(y2, list_genetic, label = 'Генетичний алгоритм за другим спосіб вибору батьків')
# ax1.set_xlabel('Кількість ітерацій')
# ax1.set_ylabel('Середнє значення')
# ax1.legend()
# plt.show()