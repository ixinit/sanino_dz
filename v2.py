num = int(input("Введите число:"))
digit = 0

# abs() - возвращает модуль числа
num = abs(num)

while (num > 0):
    num = num // 10
    digit += 1

print(digit)
