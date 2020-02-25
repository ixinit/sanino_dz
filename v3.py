a = int(input("Введите A: "))
b = int(input("Введите B: "))

if (a < b):
    if (b > 0):
        for i in range(a, b+1):
            print(i)
    else:
        for i in range(a, b-1):
            print(i)

if (a > b):
    if (b > 0):
        for i in range(a,b+1,-1):
            print(i)
    else:
        for i in range(a,b-1,-1):
            print(i)
