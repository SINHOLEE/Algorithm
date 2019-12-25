T = int(input())

for t in range(T):
    n = int(input())
    nums = [""] * n
    for i in range(n):
        num = input().replace(' ', '')
        nums[i] = num
    same = False
    for i in range(n - 1):
        for j in range(i + 1, n):
            for k in range(min(len(nums[i]), len(nums[j]))):

                if nums[i][k] == nums[j][k]:
                    continue
                else:

                    break
            else:
                same = True
                break
        if same:
            break
    if same:
        print('NO')
    else:
        print('YES')

