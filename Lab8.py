(leftNumber, operation, rightNumber) = input().split()

leftNumber = float(leftNumber)
rightNumber = float(rightNumber)

if operation == '+':
    print(leftNumber + rightNumber)
elif operation == '-':
    print(leftNumber - rightNumber)
elif operation == '*':
    print(leftNumber * rightNumber)
elif operation == '/':
    try:
        print(leftNumber / rightNumber)
    except Exception:
        print("Ошибка: деление на ноль")
else:
    print("Неверная операция")
