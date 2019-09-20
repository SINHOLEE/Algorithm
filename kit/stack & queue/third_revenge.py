
# 내가 푼 방식
from collections import deque
# bridge_length = 2
# weight = 10
# truck_weights = [7, 4, 5, 6]
def solution(bridge_length, weight, truck_weights):
    # bridge = [0] * bridge_length
    bridge = deque(0 for i  in range(bridge_length))
    truck_weights = deque(truck_weights[j] for j in range(len(truck_weights)))
    # print(bridge)
    count = 0
    last_counts = len(truck_weights)
    total_second = 0
    final_count = 0
    sum_bridge = 0
    while True:
        # for i in range(bridge_length):
        #     if bridge[i] == 0:
        #         count += 1
        if count == last_counts and total_second != 0 and final_count == bridge_length:
            break
        if len(truck_weights) == 0:
            bridge.popleft()
            bridge.append(0)
            total_second += 1
            final_count += 1
            continue

        truck = truck_weights.popleft()
        header = bridge.popleft()
        sum_bridge -= header

        if sum_bridge + truck <= weight:
            count += 1
            sum_bridge += truck
            bridge.append(truck)
        else:
            truck_weights.insert(0, truck)
            bridge.append(0)
        total_second += 1



    return total_second


# 나랑 비슷하지만 깔끔한 방식 + 값을 계속 쥐고 있는 방식
def solution(bridge_length, weight, truck_weights):
    q=[0]*bridge_length
    sec=0
    sum_q = 0
    while q:
        sec+=1
        first_truck = q.pop(0)
        sum_q -= first_truck
        if truck_weights:
            if sum_q + truck_weights[0]<=weight:
                truck = truck_weights.pop(0)
                q.append(truck)
                sum_q += truck
            else:
                q.append(0)
    return sec

solution(bridge_length, weight, truck_weights)