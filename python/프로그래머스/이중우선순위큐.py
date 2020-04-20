import heapq
import math


def find_max_idx(hq, cur_idx, cnt):
    global max_idx, max_value
    if cur_idx > cnt:
        temp = cur_idx // 2 if cur_idx % 2 else cur_idx // 2 - 1
        if max_value < hq[temp]:
            max_idx = temp
            max_value = hq[temp]
        return
    find_max_idx(hq, cur_idx*2+1, cnt)
    find_max_idx(hq, cur_idx*2+2, cnt)


def solution(operations):
    global max_idx, max_value
    hq = []
    cnt = -1
    for op in operations:
        if op == 'D 1':
            max_value = -1 * math.inf
            if len(hq):
                find_max_idx(hq, 0, cnt)
                hq = hq[:max_idx] + hq[max_idx+1:]
                cnt -= 1
        elif op == 'D -1':
            if len(hq):
                heapq.heappop(hq)
                cnt -= 1
        else:
            temp = op.split()
            heapq.heappush(hq, int(temp[1]))  # 최소 힙
            cnt += 1
    answer = []
    if len(hq) == 0:
        answer.append(0)
        answer.append(0)
    elif len(hq) == 1:
        answer.append(hq[0])
        answer.append(hq[0])
    else:
        max_value = -1 * math.inf
        find_max_idx(hq, 0, cnt)
        answer.append(max_value)
        answer.append(hq[0])
    print(answer)
    return answer


max_idx = 0
max_value = 0
solution(['I 1', 'I 2', 'I 3', 'I 4', 'I 5', 'I 6', 'I 7', 'I 8', 'I 9', 'I 10', 'D 1', 'D -1', 'D 1', 'D -1'])
