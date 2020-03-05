import sys
sys.stdin = open('input_mm.txt', 'r')
sys.stdout = open('result_mm.txt', 'w', encoding='utf-8')

T = int(input())  # 테스트 케이스

for t in range(1, T + 1):
    N = int(input())  # 첫줄 양의 개수
    nums = list(map(int, input().split()))  # N개의 ai의 양의 정수 리스트

    #  max , min 동시에 구하는 로직
    my_max = 0
    my_min = 0
    for i in range(len(nums)):

        if i == 0:
            my_min = nums[i]
            my_max = nums[i]
        else:
            if my_max < nums[i]:
                my_max = nums[i]
            else:
                pass

            if my_min > nums[i]:
                my_min = nums[i]
            else:
                pass

    result = my_max - my_min  # 요구하는 답
    print('#', end='')
    print(t, result)
