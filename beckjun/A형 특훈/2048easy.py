'''
mat를 함수에 넣어 관리할때는, 초기화하는것에 집중해야한다.
배울점, queue를 사용해서 000을 한번에 지우고,
그다음 merge 로직을 이용해서 합친다.
'''

from pprint import pprint
n = int(input())
mat = [list(map(int, input().split())) for _ in range(n)]
def left_or_up(arr):
    visited = [False] * n
    
    for i in range(1, n):
        while True:
            if i < 1:
                break
            if arr[i-1] == 0:
                arr[i-1] , arr[i] = arr[i], arr[i-1]
                visited[i-1], visited[i] = visited[i], visited[i-1]
                i -= 1
                continue
            elif arr[i-1] == arr[i]:
                if visited[i-1] == False and visited[i] == False:
                    arr[i-1] = arr[i-1] * 2
                    arr[i] = 0
                    visited[i-1] = True
                break

            elif arr[i-1] != arr[i]:
                i -= 1
                break
    return arr

def move(new_mat, direction, round):
    global max_block
    if direction == 0:  # 오른쪽
        for i in range(n):
            arr = new_mat[i][:][::-1]
            arr = left_or_up(arr)
            for j in range(n-1, -1, -1):
                new_mat[i][j] = arr[n-j-1]
                if max_block < arr[n-j-1]:
                    max_block = arr[n-j-1]
    elif direction == 1: # 위
        for i in range(n):
            arr = [new_mat[z][i] for z in range(n)]
            arr = left_or_up(arr)
            for j in range(n):
                new_mat[j][i] = arr[j]
                if max_block < arr[j]:
                    max_block = arr[j]
    elif direction == 2: # 아래
        for i in range(n):
            arr = [new_mat[j][i] for j in range(n)][::-1]
            arr = left_or_up(arr)
            for j in range(n - 1, -1, -1):
                new_mat[j][i] = arr[n - j - 1]
                if max_block < arr[n - j - 1]:
                    max_block = arr[n - j - 1]
    else: # 왼
        for i in range(n):
            arr = new_mat[i][:]
            arr = left_or_up(arr)
            for j in range(n):
                new_mat[i][j] = arr[j]
                if max_block < arr[j]:
                    max_block = arr[j]
    if round == 5:
        return
    for k in range(4):
        move([arr[:] for arr in new_mat], k, round+1)

max_block = 0
for i in range(4):
    move([arr[:] for arr in mat], i, 1)

print(max_block)
