print("Первый способ с доп. переменной")
print("Введите первое число - a")
a = int(input())
print("Введите второе число - b")
b = int(input())
c = a
a = b
b = c
print("Результат (а и b):", a, b)

print("Второй способ без доп. переменной")
print("Введите первое число - a")
a = int(input())
print("Введите второе число - b")
b = int(input())
a, b = b, a
print("Результат (а и b):", a, b)
