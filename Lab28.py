def print_factors(factors: dict) -> None:
    isFirst = False
    for key, value in factors.items():
        if isFirst:
            print("*", end="")
        else:
            isFirst = True

        print(key, end="")

        if value > 1:
            print("^", value, sep='', end='')

    print()


def print_factorization(n: int) -> None:
    factors = {}

    while True:
        isNeedContinue = False
        for i in range(2, n + 1):
            if n == 0:
                break
            if n % i == 0:
                n //= i
                factors[i] = factors.get(i, 0) + 1
                isNeedContinue = True
                break

        if not isNeedContinue:
            break

    print_factors(factors)


print_factorization(int(input()))
