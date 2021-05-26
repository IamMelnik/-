def codes(symbols, string, result, last, index, repeatLeft):
    for k in symbols:
        if (symbols[k] - 1 > repeatLeft):
            continue
        result[index] = k
        symbols[k] += 1
        if last == index:
            print(''.join(result), end=' ')
        else:
            isRepeated = symbols[k] > 1
            codes(symbols, string, result, last, index + 1, repeatLeft - isRepeated)

        symbols[k] -= 1


n = int(input())
string = input()

symbols = {}
result = []

for a in range(n):
    result += ' '

for char in string:
    symbols[char] = 0

codes(symbols, string, result, n - 1, 0, n - len(string) - 1)
print()
