

t = int(input())

for i in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    bin_nums = map(lambda x: x%2, nums)
    if sum(bin_nums) % 2 == 0:
        print("YES")
    else:
        for i in range(1, n):
            if abs(nums[i-1] - nums[i]) == 1:
                print("YES")
                break
        else:
            print("NO")


