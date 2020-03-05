import sys
sys.stdin = open('input_dump.txt', 'r')
sys.stdout = open('output_dump.txt', 'w', encoding='utf-8')

def maxmin(nums):
    min_num = 0
    min_idx = 0
    max_num = 0
    max_idx = 0
    for i in range(0, len(nums)):
        if i == 0:
            min_num = nums[i]
            min_idx = i
            max_num = nums[i]
            min_idx = i
        else:
            if max_num < nums[i]:
                max_num = nums[i]
                max_idx = i
            else:
                pass
            if min_num > nums[i]:
                min_num = nums[i]
                min_idx = i
            else:
                pass
    return [max_idx, max_num, min_idx, min_num]  #maxmin[0] = maxindex, [1] = max


for t in range(1, 11):
    n = int(input())
    nums = list(map(int, input().split()))
    dump = 0
    while dump < n:
        max_idx = maxmin(nums)[0]
        min_idx = maxmin(nums)[2]
        nums[max_idx] -= 1
        nums[min_idx] += 1
        dump += 1
    print('#{} {}'.format(t, maxmin(nums)[1] - maxmin(nums)[3]))
        # max_idx = nums.index(max(nums))
        # min_idx = nums.index(min(nums))
        # nums[max_idx] -= 1
        # nums[min_idx] += 1
        #dump += 1
    # print(max(nums) - min(nums))
    # 메소드 사용

#
#
