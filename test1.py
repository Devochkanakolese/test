import random

q = random.randint(0,10)
w = 0

while True:
    w += 1
    print("Попытка:", w)
    a = int(input("Введите число:"))
    if a > q:
        print("Меньше, чем ты написал")
    elif a < q:
        print("Больше, чем ты написал")
    else:
        print("Угадал Какой модлодец")
        break
