from random import randint as rnd


def func(matr2):
    for i in matr2[1:-1]:
        matr1.append(i[1:-1])
    return matr1


m = int(input("Введите количество столбцов: "))
n = int(input("Введите количетсво строк: "))
matr2 = [[rnd(-5, 10) for j in range(m)] for i in range(n)]
matr1 = []
print("Исходная матрица matr2:", *matr2, sep="\n")
res = func(matr2)
print("\nКонечная матрица matr1:", *res, sep="\n")
