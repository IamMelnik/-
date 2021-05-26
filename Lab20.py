class Drink:
    def __init__(self):
        self.price = 0.0
        self.capacity = 0.0
        self.name = ""


money = int(input())
drinkAmount = int(input())

best = Drink()
currentDrink = Drink()

for i in range(drinkAmount):
    infoRows = input().split()
    currentDrink.name = infoRows[0]
    currentDrink.price = int(infoRows[1])
    currentDrink.capacity = int(infoRows[2])

    # Определяем максимальное количество литров, если равно нулю, то пропускаем наш Drink
    liters = (money // currentDrink.price) * currentDrink.capacity
    if liters == 0:
        continue

    if i == 0:
        best.name = currentDrink.name
        best.price = currentDrink.price
        best.capacity = currentDrink.capacity
        continue

    # Проверка лучший ли напиток или нет
    bestLiters = (money // best.price) * best.capacity
    if liters > bestLiters:
        best.name = currentDrink.name
        best.price = currentDrink.price
        best.capacity = currentDrink.capacity

if best.price == 0:
    print(-1)
else:
    bottles = money // best.price
    print(best.name, bottles)
    print(bottles * best.capacity)
    print(money - best.price * bottles)
