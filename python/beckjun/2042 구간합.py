import math
import sys
input = sys.stdin.readline


def init(node, start, end):
    if start == end:
        tree[node] = arr[start]
        return tree[node]
    else:
        tree[node] = init(node*2, start, (start+end) // 2) + init(node * 2 + 1, (start+end) // 2 + 1, end)
        return tree[node]


def find_subsum(node, start, end, left, right):
    if left > end or right < start:
        return 0
    if left <= start <= right and left <= end <= right:
        return tree[node]
    mid = (start + end) // 2
    return find_subsum(node * 2, start, mid, left, right) + find_subsum(node * 2 + 1, mid+1, end, left, right)


#         트리인덱스, 바꿀인덱스, 범위s, 범위e, 바꿀 숫자
def update(node, target_idx, start, end, target_num):
    if start == end == target_idx:
        tree[node] = target_num
    else:
        mid = (start + end) // 2
        if start <= target_idx <= mid:
            tree[node] = update(node * 2, target_idx, start, mid, target_num) + tree[node * 2 + 1]
        elif mid+1 <= target_idx <= end:
            tree[node] = tree[node * 2] + update(node * 2 + 1, target_idx, mid+1, end, target_num)
    return tree[node]


n, m, k = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))

h = int(math.log(n, 2)) if math.log(n, 2) / int(math.log(n, 2)) == 1\
                        else int(math.log(n, 2)) + 1


tree = [0] * (2 ** (h+1))
init(1, 0, n-1)
for _ in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1:
        update(1, b-1, 0, n-1, c)
    else:
        print(find_subsum(1, 0, n-1, b-1, c-1))


