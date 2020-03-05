n = int(input())

arr = [*map(int, input().split())]
dp = [-1000000001 ] * n
ordered = [-1] * n

tail = 0
for i in range(n):
