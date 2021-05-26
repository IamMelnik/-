import random

while True:
    secretNumber = int(random.random() * 101)
    isWin = False

    print("{Приветственное сообщение от игры}")
    for i in range(5):
        guess = int(input())
        if guess > secretNumber:
            print("Загаданное число меньше")
        elif guess < secretNumber:
            print("Загаданное число больше")
        else:
            print("Поздравляю! Вы угадали")
            isWin = True
            break

    if not isWin:
        print("Вы проиграли. Было загадано: ", secretNumber)

    if not 1 == int(input("Хотите начать сначала? (1 - ДА)\n")):
        break
