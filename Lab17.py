
dropCount = {}
roundThenDrop = {}

for i in range(37):
    dropCount[i] = 0
    roundThenDrop[i] = 0

highestNumber = roundNow = reds = blacks = 0

while (True):

    # Записывает какой раунд по счету и полученный номер
    roundNow += 1
    number = int(input())
    if number < 0:
        break

    # Увеличиваем значения количества появления номера и записываем раунд, в котором выпало
    dropCount[number] += 1
    roundThenDrop[number] = roundNow

    # Выводим номера, которые выпадали в порядке возрастания частоты выпадения
    highestDropNumber = max(dropCount.values())
    for i in range(37):
        if dropCount[i] == highestDropNumber:
            print(i, end=' ')
    print()

    # Вывод не выпавших номеров
    for i in range(37):
        if roundThenDrop[i] == 0 or roundNow - roundThenDrop[i] > 12:
            print(i, end=' ')
    print()

    #
    if number != 0:
        if number < 11 or (number > 18 and number < 29):
            if number % 2 == 0:
                blacks += 1
            else:
                reds += 1
        else:
            if number % 2 == 0:
                reds += 1
            else:
                blacks += 1

    print(reds, blacks, '\n')
