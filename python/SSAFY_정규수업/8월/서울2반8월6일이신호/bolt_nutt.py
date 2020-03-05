import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w', encoding='utf-8')

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    nums = list(map(int,input().split()))
    nums_arr = []
    temp = []
    for num_j in range(1, len(nums) + 1):
        if num_j % 2 == 1:
            temp += [nums[num_j - 1]]
        else:
            temp += [nums[num_j - 1]]
            nums_arr += [temp]
            temp = []
    
    # print("nums_arr", nums_arr)
    dic = {}
    count = 0
    for num_i in range(len(nums)):
        if num_i == 0:
            count = 1
            dic[nums[num_i]] = count
        else:
            if nums[num_i] in dic.keys():
                dic[nums[num_i]] += 1
            else:
                count = 1
                dic[nums[num_i]] = count
    # print(nums)
    # print('dic', dic)

    temp = []
    for key, value in dic.items():
        if value == 1:
            temp += [key]
    # print('temp , 처음 혹은 끝', temp)

    for na in range(len(nums_arr)):
        if nums_arr[na][0] in temp:
            final = nums_arr[na]
    # print(final)

    i = 0
    while i < len(nums_arr):
        if final[-1] == nums_arr[i][0]:
            final += [nums_arr[i][0]]
            final += [nums_arr[i][1]]
            i = 0
            
        else:
            i += 1
    # print(final)
    result = ' '.join(map(str,final))

    print('#{} {}'.format(t, result))
