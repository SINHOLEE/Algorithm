dy = [-1, 1, 0, 0]  # 상 하 좌 우
dx = [0, 0, -1, 1]

# 기둥 설치 일때,  [x, y, a, b]에서 a == 0, b == 1 일때
# 1) 바닥 위, 2) 다른 기둥의 위, 3) 보의 한쪽끝부분 위일 경우  세울 수 있고 아니면 설치 ㄴㄴ

# 보 설치일 때, [x, y, a, b]에서 a == 1, b == 1,
# 1) 한쪽 끝이 기둥 위, 혹은 양쪽 끝에 다른 보들이 있을때, 설치 아니면 설치 ㄴㄴ

# 기둘 삭제, a ==0, b == 0, #어렵네
# 1) 기준 기둥 상단에 하단 기둥이 없고( mat[y][x][1] ==0) and
# 2) 기둥 상단에 좌 우 보가 연결되어 있고
# 이부분이 어렵네
# 3) 왼쪽 보가 있을 경우 왼쪽보의 왼쪽상단이 기둥이 있고( mat[y][x][3] and mat[y][x-1][0]) and
# 4) 오른쪽 보가 있으면서 오른쪽 보의 오른쪽 상단이 기둥이 있으면 ( mat[y][x][3] and mat[y][x-1][0]

# 보 삭제 a == 1, b == 0,
# 보의 왼쪽 y, x 보의 오른쪽 y, x+1 모두 


def solution(n, build_frame):
    answer = [[]]

    mat = [[[0, 0, 0, 0] for _ in range(3)] for _ in range(3)]
    for a in mat:
        print(a)
    return answer


solution(5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]])
