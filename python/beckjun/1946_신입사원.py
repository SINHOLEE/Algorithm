import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    k = int(input())
    arr = [0] * k
    for i in range(k):
        a, b = map(int, input().split())
        arr[a-1] = b-1
    res = 0
    target = arr[0]
    for i in range(k):
        if arr[i] <= target:
            target = arr[i]
            res += 1
    print(res)
