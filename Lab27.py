n = int(input().strip())
values = map(int, input().strip().split(" "))
top5min = []

for number in values:
    for i in range(6):

        # Выход из цикла при необходимости
        if i >= len(top5min) or i == 5:
            break

        # Если число больше, то оно вставляется на месте меньшего
        if number > top5min[i]:
            top5min.insert(i, number)
            break

    # Вставка в конце листа
    if i == 5 or i == len(top5min):
        top5min.append(number)

    # Убирается первое число
    if len(top5min) > 5:
        top5min.pop(0)

    # Выводим минимальные
    for symbol in top5min:
        print(symbol, end=" ")
    print()
