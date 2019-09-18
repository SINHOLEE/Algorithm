def combi(n, r):
    global count
    if r == 0:
        count += 1
        print(count)
        return
    elif n < r:
        return
    else:
        tr[r - 1] = arr[n - 1]
        combi(n-1, r-1)
        combi(n-1, r)

n = 24
r = 12

arr = list(range(1, 25))

tr = [0] * r
count = 0
combi(n, r)

print(count)