import math
import sys
input = sys.stdin.readline


def find_max(l, r):
    target = -9999999999
    while True:
        if l > r:
            break
        if l % 2:
            target = max(target, tree[l])
            l += 1
        if r % 2 == 0:
            target = max(tree[r], target)
            r -= 1
        r //= 2
        l //= 2
    return target


def swap(idx):
    if idx == 1:
        return
    else:
        if idx % 2:
            tree[idx // 2] = max(tree[idx-1], tree[idx])
        else:
            tree[idx // 2] = max(tree[idx], tree[idx+1])
        swap(idx//2)


n, m, q = map(int, input().split())

arr = [*map(int, input().split())]
h = int(math.log(n, 2)) if math.log(n, 2) / int(math.log(n, 2)) == 1 else int(math.log(n, 2)) + 1

left = list(sorted(map(int, input().split())))
right = list(sorted(map(int, input().split())))

tree = [-9999999999] * 2 ** (h+1)
for i in range(n):
    node = 2 ** h + i
    temp = arr[i]
    while node != 0:
        tree[node] = max(tree[node], temp)
        node //= 2
for _ in range(q):
    a, b = map(int, input().split())
    tree[2 ** h + a - 1], tree[2 ** h + b - 1] = tree[2 ** h + b - 1], tree[2 ** h + a - 1]
    swap(2 ** h + a - 1)
    swap(2 ** h + b - 1)
    dic = {}
    res = 0
    for i in range(m):
        if left[i] <= right[i]:
            if dic.get((left[i], right[i])) is None:
                dic[(left[i], right[i])] = find_max(2**h + left[i]-1, 2 ** h + right[i]-1)
            res = max(res, dic[(left[i], right[i])])
        else:
            res = 10 ** 9
    print(res)
