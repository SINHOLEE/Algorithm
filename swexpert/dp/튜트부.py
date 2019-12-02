n = int(input())

lis1 = list(range(1,n+1))
lis2 = list(range(n+1, 2*n+1))

res = 0
total = (2*n+1) * n

for i in lis1:
    total -= i
    res += (total * i)
for j in lis2:
    total -= j
    res += (total * j )

print(res)
print(' '.join(list(map(str, lis1))))
print(' '.join(list(map(str, lis2))))

