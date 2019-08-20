import sys
from pprint import pprint
sys.stdin = open("input.txt", "r")
sys.stdout = open('output.txt', 'w', encoding='utf-8')


def DFS(v):

    global odder
    global visited

    visited[v] = True

    for j in range(len(mat_t[v])):

        if mat_t[v][j] == 1 and visited[v] == False:
            DFS(j)
    odder += [v]

for tc in range(1, 11):
    V, E = input().split()
    V, E = int(V), int(E)

    nums = list(map(int, input().split()))
    mat = [[0] * (V + 1) for _ in range(V + 1)]
    for j in range(0, len(nums), 2):
        mat[nums[j]][nums[j+1]] = 1
    count = 0

    visited = [False] * (V + 1)






    final_nodes = []

    for i in range(1, len(nums), 2):
        if nums[i] not in [nums[a] for a in range(0, len(nums), 2)] :
            final_nodes += [nums[i]]
    # pprint(mat)
    mat_t = [[0] * (V + 1) for _ in range(V + 1)]
    for j in range(0, len(nums), 2):
        mat_t[nums[j+1]][nums[j]] = 1

    for node in final_nodes:
        DFS(node)

    print('#{} {}'.format(tc, ' '.join(map(str, odder))))



