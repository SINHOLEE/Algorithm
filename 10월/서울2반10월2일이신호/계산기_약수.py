def div(n, temp):
    for i in range(2, int(n ** 0.5) +1):
        if n % i == 0:
            temp.append(i)
            temp.append(n // i)
    return sorted(temp)

def check_able(n):

T = int(input())
for tc in range(1, T+1):
    nums = list(map(int, input().split()))
    target = int(input())
    len_nums = len(nums)
    my_nums = []
    for idx in range(len(nums)):
        if nums[idx]:
            my_nums.append(idx)
    print(target)
    print(my_nums)

    dp = {}
    for num in div(target, []):
        print(num)
