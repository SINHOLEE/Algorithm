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


def merge(left, right):
    new = []
    while True:
        if len(left) == 0 or len(right) == 0:
            break
        a = left[0]
        b = right[0]
        if compare(a, b) == 1:
            new.append(left.pop(0))
        else:
            new.append(right.pop(0))
    if len(left) == 0:
        new.extend(right)
    if len(right) == 0:
        new.extend(left)
    return new


def merge_sort(lis):
    if len(lis) < 2:
        return lis
    mid = len(lis) // 2
    left = merge_sort(lis[:mid])
    right = merge_sort(lis[mid:])
    return merge(left, right)


def solution(numbers):
    a = merge_sort(list(map(str, numbers)))
    for aa in a:
        if aa != '0':
            return ''.join(a)
    return '0'


print(solution([323, 32]))



