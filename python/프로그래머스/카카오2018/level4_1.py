def divisor(num):
    for i in range(2, int(num ** (1/2))+1):
        if num // i >= 10000000:
            continue
        if num % i == 0:
            return num // i
    return 1


def solution(begin, end):
    arr = [begin] * (end-begin+1)
    cnt = 0
    for num in range(begin, end+1):
        arr[cnt] = divisor(num)
        cnt += 1
    if begin == 1:
        arr[0] = 0
    return arr


solution(1, 10)
