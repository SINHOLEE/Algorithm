n, m = map(int, input().split())

arr = [0] * (n+1)
for _ in range(n-1):
    a, b = map(int, input().split())
    arr[a] += 1
    arr[b] += 1
cnt = 0
for i in range(2, n+1):
    if arr[i] == 1:
        cnt += 1
if cnt == 0:
    print(m)
else:
    print(m/cnt)
