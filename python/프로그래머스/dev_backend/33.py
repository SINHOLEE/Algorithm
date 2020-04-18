length = 0
answer = 9999
KK = 0


def check(numbers):
    global length, KK
    for i in range(length - 1):
        # 만약 더 크다면
        if abs(numbers[i] - numbers[i + 1]) > KK:
            return False
    return True


def swap(numbers, k, cnt):
    global answer, length
    if cnt >= answer:
        return
    if check(numbers):
        answer = min(answer, cnt)
    if k + 1 < length - 1:
        swap(numbers, k + 1, cnt)
    for i in range(k, length - 1):
        for j in range(i + 1, length):
            numbers[i], numbers[j] = numbers[j], numbers[i]
            swap(numbers, i + 1, cnt + 1)
            numbers[i], numbers[j] = numbers[j], numbers[i]


def solution(numbers, K):
    global length, answer, KK
    length = len(numbers)
    KK = K
    if not check(numbers):
        for i in range(length - 1):
            swap(numbers, i, 0)
    if answer == 9999:
        answer = -1

    return answer