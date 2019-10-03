'''
출근하는 브라운
매일 지하철을 타고 출근하는 브라운은 다른 사람과 최대한 멀리 떨어져 앉는 것을 좋아한다. 다른 사람들과 최대한 멀리 떨어져 앉을 때, 가장 가까운 사람과의 거리를 구하라.

입력 형식
첫 번째 행에는 자리의 개수 N이 들어온다 (2 <= N <= 20000)
두 번째 행에는 각 자리에 대한 정보가 공백(space)으로 구분되어 들어온다
자리에 대한 정보는 0과 1로만 이루어져 있으며 최소한 한 개의 0과 1이 있다
1은 그 자리에 사람이 앉아 있는 것을 뜻하고 0은 해당 자리가 비어있는 것을 뜻한다
출력 형식
계산된 값을 정수로 출력
거리는 가장 인접한 사람과 브라운의 위치 차이의 절대값이다
예를 들어 1 0 1 0 0 0 1의 경우, 브라운이 5번 위치에 앉는다면 가장 인접한 사람과의 거리의 최댓값은 2이다

'''

'''
9
0 0 0 0 0 1 0 0 0
'''
n = int(input())
arr = list(map(int, input().split()))

max_count = 0
for i in range(n):
    if arr[i] == 0:
        left = i
        right = i
        count = 0
        left_check = False
        right_check = False
        while True:
            if left - 1 < 0:
                left_check = True
                break
            if  arr[left - 1] == 1:
                count += 1
                break
            count += 1
            left -= 1

        count1 = 0
        while True:
            if right + 1 > n-1:
                right_check = True
                break
            if arr[right + 1] == 1:
                count += 1
                break
            count1 += 1
            right += 1

        if right_check or left_check:
            result = max(count,count1)
        else:
            result = min(count, count1)

        if max_count < result:
            max_count = result

print(max_count)