from collections import deque
import sys

input = lambda: sys.stdin.readline()
arr = []
for _ in range(3):
    arr.extend(input().split())
arr = "".join(arr)


def four_directions(s):
    i = s.index('0')
    if i % 3 != 0:
        yield s[:i - 1] + s[i] + s[i - 1] + s[i + 1:]
    if i % 3 != 2:
        yield s[:i] + s[i + 1] + s[i] + s[i + 2:]
    if i > 2:
        yield s[:i - 3] + s[i] + s[i - 2:i] + s[i - 3] + s[i + 1:]
    if i < 6:
        yield s[:i] + s[i + 3] + s[i + 1:i + 3] + s[i] + s[i + 4:]


target = '123456780'


def bfs(root):
    if root == target: return 0
    queue, visited = deque([(root, 0)]), set()
    while queue:
        arr, count = queue.popleft()
        if arr not in visited:
            visited.add(arr)
            for new in four_directions(arr):
                if new == target: return count + 1
                if new in visited: continue
                queue.append((new, count + 1))
    return -1


print(bfs(arr))