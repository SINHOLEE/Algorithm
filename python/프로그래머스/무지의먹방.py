from collections import deque


def solution(food_times, k):
    food_len = len(food_times)
    food_sort = deque(sorted(enumerate(food_times), key=lambda x: x[1]))
    print(food_sort)
    temp_cnt = 0
    new_k = k
    while True:
        if not food_sort:
            return -1
        # 일단 낮은 숫자 순으로 정렬된 애들을 큐로 팝한다.
        idx, val = food_sort.popleft()

        if temp_cnt == val:
            food_len -= 1
            continue
        # 조건에 부합하면 멈추라??
        if new_k - (val - temp_cnt) * food_len < 0:
            food_sort.appendleft((idx, val))
            break

        new_k -= (val - temp_cnt) * food_len
        temp_cnt = val
        food_len -= 1
    food_sort = sorted(food_sort)
    return food_sort[new_k % food_len][0] + 1


print(solution([3,1,1,1,2,4,3],12), 6)
print(solution([3,1,2,1],5), 3)
print(solution([5,5,5],15), -1)
print(solution([4, 3, 5, 6, 2], 7), 3)
print(solution([4, 1, 1, 5], 4), 1)
print(solution([4, 1, 1, 5], 5), 4)
print(solution([4, 1, 1, 5], 6), 1)
print(solution([4, 1, 1, 5], 7), 4)
