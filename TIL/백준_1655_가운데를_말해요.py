n = int(input())
lis = []
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

    return result[1:]

def devided_sort(li, num):
    if len(li) <= 1:
        return li
    mid = len(li) // 2



for i in range(n):
    num = int(input())

    new_lis = devided_sort(lis, num)
    mid = (i+1) // 2
    if (i+1) % 2:
        print(new_lis[mid])
    else:
        print(new_lis[mid-1])