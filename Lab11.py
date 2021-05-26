a = float(input())
n = int(input())
res = 1.0

for i in range(abs(n)):
    res *= a

if n < 0:
    result = 1 / res

print(res)
