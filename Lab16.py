n = (int(input()))
res = []
tickets = input().split()

for i in range(0, n):
    if tickets[i].startswith('a') and tickets[i].endswith('55661'):
        res.append(tickets[i])

if len(res) == 0:
    print(-1)
else:
    print(' '.join(res))
