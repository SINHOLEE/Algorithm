# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
from collections import deque

input_stream = sys.stdin.readlines()
n = int(input_stream.pop(0))
mat = [list(map(int, input_stream.pop(0).split())) for _ in range(n)]
max_res = 0
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def water_load():
    dic = {}
    copied_mat = [arr[:] for arr in mat]
    q = deque()
    dic[0] = set()
    dic[0].add((0, 0))
    q.append((0, 0, 0))

    while q:
        t, y, x = q.popleft()

        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            if not (0 <= ny < n and 0 <= nx < n):
                continue
            if copied_mat[ny][nx]:
                continue
            q.append((t + 1, ny, nx))
            copied_mat[ny][nx] = 1
            if dic.get(t + 1) is None:
                dic[t + 1] = set()
                dic[t + 1].add((ny, nx))
            else:
                dic[t + 1].add((ny, nx))
    return dic


water_load_dic = water_load()


def get_buildable():
    temp = []
    copied_mat = [arr[:] for arr in mat]
    q = deque()
    copied_mat[n - 1][n - 1] = 1
    q.append((0, n - 1, n - 1))

    while q:
        t, y, x = q.popleft()

        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            if not (0 <= ny < n and 0 <= nx < n):
                continue
            if copied_mat[ny][nx]:
                continue
            if (ny, nx) in water_load_dic.get(t + 1, {}):
                continue
            q.append((t + 1, ny, nx))
            copied_mat[ny][nx] = 1
            temp.append((ny, nx))
    return temp


buildable_list = get_buildable()


def fill(copied_mat):
    q = deque()
    copied_mat[0][0] = 2  # 물
    q.append((0, 0))
    while q:
        y, x = q.popleft()

        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            if not (0 <= ny < n and 0 <= nx < n):
                continue
            if copied_mat[ny][nx]:
                continue
            q.append((ny, nx))
            copied_mat[ny][nx] = 2
    return copied_mat



def count_zero(copied_mat):
    cnt = 0
    for i in range(n):
        for j in range(n):
            if not copied_mat[i][j]:
                cnt += 1
    return cnt


copied_mat = [arr[:] for arr in mat]
copied_mat = fill(copied_mat)
max_res = max(max_res, count_zero(copied_mat))

for y, x in buildable_list:
    copied_mat = [arr[:] for arr in mat]
    copied_mat[y][x] = 1
    copied_mat = fill(copied_mat)
    max_res = max(max_res, count_zero(copied_mat))

print(max_res)

