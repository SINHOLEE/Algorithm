E, S, M = input().split()
E, S, M = int(E), int(S), int(M)
count = 0
a, b, c = 1, 1, 1

if E == 1 and S == 1 and M == 1:
    print('1')
else:
    while a != E or b != S or c != M:
        count += 1
        a = (count % 15) + 1
        b = (count % 28) + 1
        c = (count % 19) + 1

        print(count)
    print(count)
