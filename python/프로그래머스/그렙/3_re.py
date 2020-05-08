from collections import deque


def solution(customer, K):
    rooms = [0] * 1000001
    answer = []
    temp = 0
    wait_line = deque([])
    for custom in customer:
        if custom[1] == 1: # 1 예약 문자
            if temp < K:
                rooms[custom[0]] = 1
                temp += 1
            else:
                wait_line.append(custom[0])
                rooms[custom[0]] = 2
        else:  # 예약 취소
            if rooms[custom[0]] == 1:  # 예약을 했엇는데 예약을 취소하면
                rooms[custom[0]] = 0
                temp -= 1
                if len(wait_line):
                    rooms[wait_line.popleft()] = 1
                    temp += 1
            elif rooms[custom[0]] == 2:
                rooms[custom[0]] = 0
                wait_line.remove(custom[0])
    for idx in range(len(rooms)):
        if rooms[idx] == 1:
            answer.append(idx)
    print(answer)
    return answer


solution([[1,1],[2,1],[3,1],[2,0],[2,1]], 2)
