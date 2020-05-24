t = int(input())

for i in range(t):
    n = int(input())
    athletes = list(map(int, input().split()))
    athletes.sort()
    res = 9999999999999999999
    for i in range(1, len(athletes)):
        res = min(res, abs(athletes[i-1] - athletes[i]))
    print(res)


