import sys


def merge(lef, rig):
    result = [0]
    i = 0
    j = 0

    while True:
        if i == len(lef) or j == len(rig):
            break
        if lef[i] < rig[j]:
            result[-1:] = [result[-1], lef[i]]
            i += 1
        else:
            result[-1:] = [result[-1], rig[j]]
            j += 1

    while True:
        if i == len(lef):
            break
        result[-1:] = [result[-1], lef[i]]
        i += 1
    while True:
        if j == len(rig):
            break
        result[-1:] = [result[-1], rig[j]]
        j += 1

    # if i < len    (lef):
    #     result[-1:] = [result[-1]] + lef[i:]
    # if j < len(rig):
    #     result[-1:] = [result[-1]] + rig[j:]

    return result[1:]

def devided_sort(li):
    global count
    if len(li) <= 1:
        return li
    mid = len(li) // 2

    left = devided_sort(li[:mid])
    right = devided_sort(li[mid:])
    if left[-1] > right[-1]:
        count += 1

    return merge(left, right)

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    count = 0
    sorted_arr = devided_sort(arr)
    print('#%s %s' % (tc, sorted_arr))