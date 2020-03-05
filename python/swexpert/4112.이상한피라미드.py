from collections import deque


def make_pyramid():
    pyramid = dict()
    idx = 1
    cnt1 = 1
    while cnt1 < 10000:
        for _ in range(idx):
            pyramid[cnt1] = idx
            cnt1 += 1
        idx += 1
    return pyramid


my_pyramid = make_pyramid()
for t in range(1, int(input()) + 1):
    start, goal = map(int, input().split())

    visited = [False] * 10001
    visited[start] = True
    q = deque([(start, 0)])
    res = -1
    while q:
        node, cnt = q.popleft()
        if node == goal:
            res = cnt
            break

        depth = my_pyramid[node]

        for d in (-1, 1, -depth, -(depth - 1), depth, depth+1):
            new_node = node + d
            if not (0 < new_node < 10001):
                continue
            if visited[new_node]:
                continue
            if d == -1 or d == 1:
                if depth != my_pyramid[new_node]:
                    continue
            elif d == -depth or d == -(depth - 1):
                if depth - 1 != my_pyramid[new_node]:
                    continue
            else:
                if depth + 1 != my_pyramid[new_node]:
                    continue
            visited[new_node] = True
            q.append((new_node, cnt + 1))

    print('#%s %s' % (t, res))
