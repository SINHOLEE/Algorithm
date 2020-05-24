def solution(n):
    a = list(bin(n)[2:])[::-1]
    total = 0
    for i in range(len(a)):
        if a[i] == '1':
            total += 3 ** i
    print(total)

solution(10**10)