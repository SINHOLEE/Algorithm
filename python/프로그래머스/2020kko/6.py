import heapq
from itertools import permutations


def solution(board, r, c):
    card_set = set()
    for i in range(4):
        for j in range(4):
            if board[i][j]:
                card_set.add(board[i][j])
    card_list = list(card_set)
    answer = 9999999999999999
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    def ctrl_y_x(y, x, d, mat):

        while True:
            ny, nx = y+dy[d], x+dx[d]
            if not (0<= ny<4 and 0<= nx < 4):
                return y, x
            if mat[ny][nx]:
                return ny, nx
            y, x = ny, nx
        return ny, nx

    def find_min_dis(card_order, r, c):
        if card_order == (2,3,1):
            pass
        total_cnt = 0
        state = []
        dummy_board = [arr[:] for arr in board] # deepcopy
        for target_card in card_order:
            for _ in range(2):
                visited = [[0] * 4 for _ in range(4)]
                hq = []
                heapq.heappush(hq, (0, r, c))
                visited[r][c] = 1
                while hq:
                    cnt, y, x = heapq.heappop(hq)
                    if dummy_board[y][x] == target_card:
                        dummy_board[y][x] = 0
                        r, c = y, x
                        if len(state):  # 뒤집을 카드를 찾는 순서
                            state = []
                        else:  # 엔터를 누르기 위해 찾는 과정
                            state = [y, x, target_card]

                        total_cnt += cnt
                        break
                    for k in range(4):
                        for ctrl in range(2):
                            if ctrl:
                                ny, nx = ctrl_y_x(y, x, k, dummy_board)
                                if not (0<= ny<4 and 0<= nx < 4):
                                    continue
                                if visited[ny][nx]:
                                    continue
                                visited[ny][nx] = 1
                                heapq.heappush(hq, (cnt + 2, ny, nx))

                            else:
                                ny, nx = y+dy[k], x+dx[k]
                                if not (0<= ny<4 and 0<= nx < 4):
                                    continue
                                if visited[ny][nx]:
                                    continue
                                visited[ny][nx] = 1
                                heapq.heappush(hq, (cnt + 1, ny, nx))

        return total_cnt

    for card_order in permutations(card_list):
        answer = min(answer, find_min_dis(card_order, r, c))
    return answer


print(solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]], 1, 0))
# print(solution([[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]], 0, 1))
