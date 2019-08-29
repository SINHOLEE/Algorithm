import sys
from pprint import pprint
# sys.stdin = open("input.txt", "r")
# sys.stdout = open('output_신호.txt', 'w', encoding='utf-8')


# def DFS(v):
#
#     global odder
#     global visited
#
#     visited[v] = True
#
#     for j in range(len(mat_t[v])):
#
#         if mat_t[v][j] == 1 and visited[v] == False:
#             DFS(j)
#     odder += [v]
#
# for tc in range(1, 11):
#     V, E = input().split()
#     V, E = int(V), int(E)
#
#     nums = list(map(int, input().split()))
#     mat = [[0] * (V + 1) for _ in range(V + 1)]
#     for j in range(0, len(nums), 2):
#         mat[nums[j]][nums[j+1]] = 1
#     count = 0
#
#     visited = [False] * (V + 1)
#
#
#
#
#
#
#     final_nodes = []
#
#     for i in range(1, len(nums), 2):
#         if nums[i] not in [nums[a] for a in range(0, len(nums), 2)] :
#             final_nodes += [nums[i]]
#     # pprint(mat)
#     mat_t = [[0] * (V + 1) for _ in range(V + 1)]
#     for j in range(0, len(nums), 2):
#         mat_t[nums[j+1]][nums[j]] = 1
#
#     for node in final_nodes:
#         DFS(node)
#
#     print('#{} {}'.format(tc, ' '.join(map(str, odder))))
#
#

# def DFS(v):
#     if visited[v] == False:
#
#         for j in range(1, V+1):
#             if mat_t[v][j] == 1 and visited[v] == False:
#                 DFS(j)
#
#         visited[v] = True
#
#         print(v, end=' ')
#
# for tc in range(1, 11):
#     V, E = input().split()
#     V, E = int(V), int(E)
#
#     nums = list(map(int, input().split()))
#     mat = [[0] * (V + 1) for _ in range(V + 1)]
#     for j in range(0, len(nums), 2):
#         mat[nums[j]][nums[j + 1]] = 1
#     count = 0
#
#     visited = [False] * (V + 1)
#
#     mat_t = [[0] * (V + 1) for _ in range(V + 1)]
#     for j in range(0, len(nums), 2):
#         mat_t[nums[j + 1]][nums[j]] = 1
#
#     print('#{}'.format(tc), end=' ')
#
#     for num in range(1, V+1):
#         DFS(num)
#
#     print()


V, E = map(int, input().split())

temp = list(map(int, input().split()))
linked_list = [False]
temm = [[] for _ in range(V)]
linked_list += temm
started_list = [False]
temm1 = [[] for _ in range(V)]
started_list += temm1

for tp in range(0, len(temp) - 1, 2):
    linked_list[temp[tp]] += [temp[tp + 1]]
    started_list[temp[tp + 1]] += [temp[tp]]
print(started_list)

visited = []
mystack = []

print(started_list[5])


