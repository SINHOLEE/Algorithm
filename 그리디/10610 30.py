n = sorted(list(map(str, input())), reverse=True)

if sum(map(lambda x:ord(x)-48, n)) % 3 == 0 and int(''.join(map(lambda x:ord(x)-48, n))) % 10 == 0:
    print(int(''.join(map(lambda x:ord(x)-48, n))))
else:
    print(-1)