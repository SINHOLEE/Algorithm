# # 인동이형꺼
# def IsItDanjo(n):
#     a = n % 10
#     n = int(n / 10)
#     while n != 0:
#         if n % 10 > a:
#             return False
#         else:
#             a = n % 10
#             n = int(n / 10)
#     return True

# 내꺼
def IsItDanjo(N):
    while True:
        if N < 10:
            return True
        a = N % 10
        if a >= (N // 10) % 10:
            N = N // 10
        else:
            return False

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    nums = sorted(nums)
    reversed_nums = nums[::-1]
    # print(reversed_nums)
    max_danjo = 0
    max_j = len(reversed_nums)
    for i in range(len(reversed_nums) - 1):
        if max_j == i:break
        for j in range(i + 1, max_j):

            num = reversed_nums[i] * reversed_nums[j]
            if max_danjo < num:
                if IsItDanjo(num):
                    max_danjo = num
                    max_j = j
                    break
                else:
                    pass
            else:
                pass


    if max_danjo == 0:
        print('#%s -1' % tc)
    else:
        print('#%s %d' % (tc, max_danjo))