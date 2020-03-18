import sys
import math

input = sys.stdin.readline
n, m, k = map(int, input().split())
arr = []

h = int(math.log(n, 2)) if math.log(n, 2) / int(math.log(n, 2)) == 1\
                        else int(math.log(n, 2)) + 1

tree = [0] * (2 ** (h+1))

for i in range(n):
    temp = int(input())
    arr.append(temp)
    node = 2 ** h + i
    # 트리 구성
    while node != 0:
        tree[node] += temp
        node //= 2

for _ in range(m+k):
    a, b, c = map(int, input().split())
    if a == 1:
        node = 2 ** h + b - 1
        original = tree[node]
        while node != 0:
            tree[node] += c - original
            node //= 2
    else:
        s, e, total = 2 ** h + b-1, 2 ** h + c-1, 0
        while True:
            if s > e:
                break
            if s % 2:  # start가 오른쪽 자식일때만, 그 원소를 더하고 자리는+1
                total += tree[s]
                s += 1
            if e % 2 == 0:  # end가 왼쪽 자식일때만, 그 원소를 더하고 자리는-1
                total += tree[e]
                e -= 1
            s //= 2
            e //= 2
        print(total)
