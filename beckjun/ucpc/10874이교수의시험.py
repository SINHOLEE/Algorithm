N = int(input())
for n in range(1, N+1):
    temp = list(map(int, input().split()))

    for j in range(1, len(temp)+1):
        if ((j-1) % 5) +1 != temp[j-1]:
            break
    else:
        print(n)