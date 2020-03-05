'''
느낀점 
규칙만 찾으면 쉽게 풀 수 있는 문제.
함수 안의 함수가 아직까진 헷갈리니 조심해서 접근해야 함
'''

from pprint import pprint
    # 우 하 좌 상
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
n,m,k = map(int, input().split())

mat_orgin = [list(map(int, input().split())) for _ in range(n)]

def rotate(r, c, s, mat1):
    top = mat1[r-s][c-s]
    i = r-s
    j = c-s
    for k in range(4):
        for _ in range(s * 2):
            next = mat1[i+di[k]][j+dj[k]]
            mat1[i+di[k]][j+dj[k]] = top
            top = next
            i += di[k]
            j += dj[k]
    return mat1

def perm(max_depth, depth, temp):
    global A, mat_orgin
    if max_depth==depth:
        mat = [row[:] for row in mat_orgin]
        for t in temp:  # 0, 1 and 1, 0
            r, c, s = ro_list[t]
            for ro in range(1, s + 1):  # s만큼 큰 사각형으로 돌거니까,
                mat = rotate(r, c, ro, mat)
        A = min(A, min([sum(mat[kkk]) for kkk in range(n)]))

        return
    for i in range(max_depth):
        if visited[i] == False:
            visited[i] = True
            perm(max_depth, depth+1, temp+ [i])
            visited[i] = False

ro_list = []
for kk in range(k):
    r, c, s = map(int, input().split())
    r = r-1
    c = c-1
    ro_list.append([r, c, s])
A = 100000000000900
visited = [False] * k
perm(k, 0, [])

print(A)

