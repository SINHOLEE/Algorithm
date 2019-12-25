from collections import deque
import sys

input = sys.stdin.readline
n, a, b = map(int, input().split())

x, y = min(a, b), max(a, b)


def bfs(x, y):
    cnt = 0
    dq_x = deque([x])
    dq_y = deque([y])
    stop = False
    while True:
        if len(dq_x) == 0 and len(dq_y) == 0:
            break
        visited = [0] * (2 + n)
        for i in range(len(dq_x)):
            ori = dq_x.popleft()
            leftori = ori - 2 ** cnt
            if 0 < leftori < n + 1:
                if not visited[leftori]:
                    dq_x.append(leftori)
                    visited[leftori] = 1

            rightori = ori + 2 ** cnt
            if 0 < rightori < n + 1:
                if not visited[rightori]:
                    dq_x.append(rightori)
                    visited[rightori] = 1

        for j in range(len(dq_y)):
            yookri = dq_y.popleft()
            leftyookri = yookri - 2 ** cnt
            if 0 < leftyookri < n + 1:
                if visited[leftyookri] == 0:
                    dq_y.append(leftyookri)
                    visited[leftyookri] = 2
                else:
                    if visited[leftyookri] == 1:
                        stop = True
                        break

            rightyookri = yookri + 2 ** cnt
            if 0 < rightyookri < n + 1:
                if visited[rightyookri] == 0:
                    dq_y.append(rightyookri)
                    visited[rightyookri] = 2
                else:
                    if visited[rightyookri] == 1:
                        stop = True
                        break
        cnt += 1
        if stop:
            break

    if stop:
        return cnt
    else:
        return -1


print(bfs(x, y))
