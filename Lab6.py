import math

print("Введите коэффициенты")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
discr = b * b - 4 * a * c
print("Дискриминант D =", discr)
if discr > 0:
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
elif discr == 0:
    x = -b / (2 * a)
    print("x =", x)
else:
    print("Корней нет")
