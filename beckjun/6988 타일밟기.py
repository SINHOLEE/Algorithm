import copy

#구하고 싶은 값 -> x, y를 뽑아내

# 역으로 구해

def xy(N):
    x = 1
    y = 1
    result = 1
    while True:
        if result == N:
            break

        result += 1
        y += 1
        if result == N:
            break
        check = False
        count = 0
        for i in range(y - 1):
            x += 1
            y -= 1
            result += 1
            count += 1
            if result == N:
                check = True
                break
        if check:
            break
        else:
            for j in range(count):
                x -= 1
                y += 1

    return x, y

def soulve(xx, yy):
    x = 1
    y = 1
    result = 1
    while True:
        if xx == x and yy == y:
            break

        result += 1
        y += 1
        if xx == x and yy == y:
            break
        check = False
        count = 0
        for i in range(y - 1):
            x += 1
            y -= 1
            result += 1
            count += 1
            if xx == x and yy == y:
                check = True
                break
        if check:
            break
        else:
            for j in range(count):
                x -= 1
                y += 1

    return result


T = int(input())

for tc in range(1, T+1):
    x, y = map(int, input().split())

    print('#%s %d' % (tc, soulve(xy(x)[0] + xy(y)[0], xy(x)[1] + xy(y)[1])))
