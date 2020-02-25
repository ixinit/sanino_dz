from random import random

n = int(input("Введите n для генерации последовательности: "))
posled = []
s_ch = 0
s_otr = 0
s_ch_otr = 0

# генерация последовательности из n случайных числе в диапазоне (-10:10)
for i in range(n):
    posled.append(int(random()*20-10))

# вывод последовательности
print(posled)

# проверка условий и подсчет сумм
for i in range(0, len(posled)):
    if (posled[i] % 2 == 0):
        s_ch += posled[i]
    if (posled[i] < 0):
        s_otr += posled[i]
    if (posled[i] % 2 == 0 and posled[i] < 0):
        s_ch_otr += posled[i]
# вывод суммы четных, отрицательных, четных и отрицательных
print(s_ch, s_otr, s_ch_otr)
