import sys
from pprint import pprint
sys.stdin = open("sample_input.txt", "r")
sys.stdout = open('output_그래프경로.txt', 'w', encoding='utf-8')


T = int(input())

for tc in range(1, T+1):
    V, E = input().split()
    V, E = int(V), int(E)
    nums = []
    for e in range(E):
        temp1, temp2 = input().split()
        nums += [int(temp1), int(temp2)]
    S, G = input().split()
    S, G = int(S), int(G)

    mat = [[0] * (V + 1) for _ in range(V + 1)]
    for i in range(0, len(nums), 2):
        mat[nums[i]][nums[i + 1]] = 1

    visited = [False] * (V + 1)
    result = 0

    def DFS(v):
        global result
        global G
        if visited[v] == False:
            visited[v] = True
            if v == G:
                result = 1
        for i in range(1, len(mat[v])):
            if (visited[i] == False) and mat[v][i]:
                DFS(i)

    DFS(S)
    print('#{} {}'.format(tc, result))
