import math

number = int(input())

if number <= 3:
    print("Простое")
    exit()

if number % 2 == 0 or number % 3 == 0:
    print("Составное")
    exit()

for i in range(5, int(math.sqrt(number)+1), 6):
    if number % i == 0 or number % (i + 2) == 0:
        print("Составное")
        exit()

print("Простое")
