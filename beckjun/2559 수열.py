N, K = input().split()
N, K = int(N), int(K)
temps = list(map(int, input().split()))
temp = 0
for k in range(K):
    temp += temps[k]
max_temp = temp
if temp >= max_temp:
    max_temp = temp
for n in range(N - K):
    temp = temp - temps[n] + temps[n+K]
    if temp >= max_temp:
        max_temp = temp


print(max_temp)

