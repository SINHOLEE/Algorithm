import functools


def compare(a, b):
    le = min(len(a), len(b))
    for idx in range(le):
        if a[idx] == b[idx]:
            continue
        elif a[idx] > b[idx]:
            return 1  # a가 더 크다
        else:
            return -1
    if len(a) == len(b):
        return 1
    elif len(a) > len(b):
        return compare(a[le:], b)
    else:
        return compare(a, b[le:])


def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=functools.cmp_to_key(compare), reverse=True)
    return str(int(''.join(numbers)))


print(solution([323, 32]))



