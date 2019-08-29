N = int(input())


max_idx = 0
max_arr = []
for num in range(N, 0, -1):
    arr = [0, N, num]

    i = 0
    while arr[i] >= 0:
        i += 1

        if i > 2:
            arr += [0]
            arr[i] = arr[i - 2] - arr[i - 1]
    if max_idx < i:
        max_idx = i
        max_arr = arr



print(max_idx - 1)
print(' '.join(map(str, max_arr[1:-1])))


