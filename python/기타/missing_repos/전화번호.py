T = int(input())

for t in range(T):
    n = int(input())
    nums = [""] * n
    for i in range(n):
        num = input().replace(' ', '')
        nums[i] = num
    same = False
    nums.sort()
    for i in range(n - 1):
        for k in range(min(len(nums[i]), len(nums[i+1]))):

            if nums[i][k] == nums[i+1][k]:
                continue
            else:
                break
        else:
            same = True
            break
    if same:
        print('NO')
    else:
        print('YES')
