import sys

sys.stdin = open('input_cal.txt', 'r', encoding='utf-8')

sys.stdout = open('output_cal.txt', 'w', encoding='utf-8')

T = int(input())

def all_perm(depth, i, lis):
    global c
    c+=1

    # if depth >= 1 and n > target:
    #     return
    if depth == i:

        string = ''.join(lis)
        n = int(string)
        bucket.add((i, n ))
        return
    for j in range(len_nums):

        all_perm(depth+1, i, lis + [str(my_nums[j])])

def backtrack(depth, count_nums, result):
    global min_depth, len_nums, check, c
    c += 1
    if target == result:
        if min_depth > depth + count_nums:
            min_depth = depth + count_nums
        check = True
        return
    if min_depth < depth + count_nums:
        return
    if target < result:
        return

    if dp[result] == -1:
        dp[result] = count_nums + depth - 1 # '='을 뺀 개수

    else:
        if dp[result] < count_nums + depth - 1:
            return
        else:
            dp[result] = count_nums + depth - 1

    for i, digit in bucket:

        if digit <= 1:
            continue
        if target % digit == 0:
            backtrack(depth+1, count_nums + i, result * digit)
    


for tc in range(1, T+1):
    nums = list(map(int, input().split()))
    target = int(input())
    len_nums = len(nums)
    my_nums = []
    for idx in range(len(nums)):
        if nums[idx]:
            my_nums.append(idx)
    len_nums = len(my_nums)
    target_len = len(str(target))
    c = 0
    bucket = set()
    for i in range(1, target_len+1):
        all_perm(0, i, [])

    bucket = sorted(list(bucket), reverse=True)
    dp = [-1] * (target + 1)

    check = False
    min_depth = 99999999


    if target == 1:
        print('#%s 2' % tc)
    else:
        backtrack(0, 0, 1)
        if check:
            print('#%s %s' % (tc, min_depth))
        else:
            print('#%s -1' % tc)
