import sys
from pprint import pprint
# sys.stdin = open("sample_input.txt", "r")
# sys.stdout = open('output_그래프경로.txt', 'w', encoding='utf-8')


# def DFS(v):
#     global result
#     if visited[v] == False:
#         visited[v] = True
#         if v == G:
#             result = 1
#     for i in range(1, len(mat[v])):
#         if (visited[i] == False) and mat[v][i]:
#             DFS(i)
#
#
# T = int(input())
#
# for tc in range(1, T+1):
#     V, E = input().split()
#     V, E = int(V), int(E)
#     nums = []
#     for e in range(E):
#         temp1, temp2 = input().split()
#         nums += [int(temp1), int(temp2)]
#     S, G = input().split()
#     S, G = int(S), int(G)
#
#     mat = [[0] * (V + 1) for _ in range(V + 1)]
#     for i in range(0, len(nums), 2):
#         mat[nums[i]][nums[i + 1]] = 1
#
#     visited = [False] * (V + 1)
#     result = 0
#
#
#     DFS(S)
#     print('#{} {}'.format(tc, result))

def DFS(start):
    visited[start] = True

    for i in range(1, V + 1):
        if mat[start][i] == 1 and visited[i] == False:
            if i == G:
                result = 1
                return
            else:
                DFS(i)



T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    nums = []
    for e in range(E):
        temp1, temp2 = list(map(int, input().split()))
        nums += [temp1, temp2]
    S, G = input().split()
    S, G = int(S), int(G)

    mat = [[0] * (V + 1) for _ in range(V + 1)]
    for i in range(0, len(nums), 2):
        mat[nums[i]][nums[i + 1]] = 1

    visited = [False] * (V + 1)
    result = 0 # 갈 수 있으면 1, 없으면 0
    DFS(S) # 재귀함수로 검색하자.

    print('#{} {}'.format(tc, result))

