T = int(input())
def change_hex_to_deca(string):
    result = 0
    exposure = -1

    for i in range(len(string) - 1, -1, -1):
        exposure += 1
        if string[i] == 'F':
            result += (16 ** exposure) * 15
        elif string[i] == 'E':
            result += (16 ** exposure) * 14
        elif string[i] == 'D':
            result += (16 ** exposure) * 13
        elif string[i] == 'C':
            result += (16 ** exposure) * 12
        elif string[i] == 'B':
            result += (16 ** exposure) * 11
        elif string[i] == 'A':
            result += (16 ** exposure) * 10
        else:
            result += (16 ** exposure) * int(string[i])
    return result



for tc in range(1,T+1):
    N, K = map(int, input().split())
    passwords = input()
    Q = N // 4

    passwords = passwords + passwords[: Q]
    # 하나의 숫자의 배수
    passible = []
    s = ''
    for q in range(N):
        s = ''
        for j in range(Q):
            s += passwords[q + j]
        passible.append(s)
    passible = list(set(passible))

    new_nums = []
    for p in range(len(passible)):
        new_nums.append(change_hex_to_deca(passible[p]))
    new_nums = sorted(new_nums)
    print('#%s %d' % (tc, new_nums[-K]))