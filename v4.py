from random import random
M = 20
N = 5
a = []
# генерация матрицы 5 строк 20 столбцов и сумма строк
for i in range(N):
    b = []
    for j in range(M):
        b.append(int(random()*11))
        print("%3d" % b[j], end='')
    a.append(b)
    print('   |', sum(b), ' | ', sum(b)/M)

# просто разделение матрицы и суммы столбцов(чтобы было визуально понятно) 
for i in range(M):
    print(" --", end='')
print()

# подсчет суммы каждого столбца
for i in range(M):
    s = 0
    for j in range(N):
        s += a[j][i]
    print("%3d" % s, end='')
print()

# просто разделение суммы и среднего значения столбцов(чтобы было визуально понятно)
for i in range(M):
    print(" --", end='')
print()

# подсчет суммы каждого столбца
for i in range(M):
    s = 0
    for j in range(N):
        s += a[j][i]
    s = s/N
    print("%3d" % s, end='')
print()
