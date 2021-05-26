import math

# Функция для подсчета стороны используя координаты
def sideLength(x1, y1, x2, y2):
    return math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))

# Функция для проверки треугольника
def checkTriangle(a, b, c):
    if a + b < c or b + c < a or c + a < b:
        return 0
    else:
        return 1


method = int(input("[1] - длины сторон треугольника; [2] - координаты вершин: "))
if method == 1:
    a = float(input())
    b = float(input())
    c = float(input())

    if checkTriangle(a, b, c) == 0:
        print("Треугольника не существует")
    else:
        p = (a + b + c) / 2
        s = math.sqrt(p * (p - a) * (p - b) * (p - c))
        print("S = ", s)

elif method == 2:
    x1, y1 = map(float, input().split())
    x2, y2 = map(float, input().split())
    x3, y3 = map(float, input().split())

    a = sideLength(x1, y1, x2, y2)
    b = sideLength(x2, y2, x3, y3)
    c = sideLength(x3, y3, x1, y1)

    if checkTriangle(a, b, c) == 0:
        print("Треугольника не существует")
    else:
        p = (a + b + c) / 2
        s = math.sqrt(p * (p - a) * (p - b) * (p - c))
        print("S = ", s)
else:
    print("Ошибочный ввод")
