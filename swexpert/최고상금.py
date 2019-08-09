nums_list = [2,3,8,8,8]
def pick_2_subset(nums_list):
    dumy = [0, 0, 0, 0, 0]
    # 부분집합 두개인 애들의 인덱스를 뽑아라
    indexes = []  # 확인용
    dumies = []
    for i in range(1<<len(nums_list)):
        temp = []
        for j in range(len(nums_list)):
            if i & (1<<j):
                temp += [j]
        if len(temp) == 2:
            indexes += [temp]
            dumy = mk_new_list(nums_list, temp)
            dumies += [dumy]
    return dumies
def deep_depth_may(lists):

    my_max = 0
    for l in range(len(lists)):
        cnt = ''.join(map(str, lists[l]))
        cnt = int(cnt)
        if my_max < cnt:
            my_max = cnt
    return my_max
# n -> 교환하는 횟수, m -> 교환하는 횟수만큼 반복하는데 필요한 for 문의 원소
def my_sum(m, n):

    num = 0
    for i in range(m):
        num += n ** i
    return num

# 부분집합 인덱스끼리 교환하는 함수
def mk_new_list(num_list, temp):
    dumy = [0] * len(nums_list)
    for i in range(len(nums_list)):

        if i in temp:
            for j in range(len(temp)):
                if i == temp[j]:
                    pass
                else:
                    dumy[i] = nums_list[temp[j]]
        else:
            dumy[i] = nums_list[i]
    return dumy


cnt1 = pick_2_subset(nums_list)
print(cnt1)
print(deep_depth_may(cnt1))
# T = int(input())
#
# for tc in range(1, T+1):
#     nums, n = input().split()
#     nums_list = []
#     n = int(n)
#     for num in nums:
#         nums_list += [int(num)]
#
#     print(nums_list)

n = 2
lists = []
nums_list = [3, 2, 8, 8, 8]
lists += [nums_list]
# result [[2, 3, 8, 8, 8], [8, 2, 3, 8, 8], [3, 8, 2, 8, 8], [8, 2, 8, 3, 8], [3, 8, 8, 2, 8], [3, 2, 8, 8, 8], [8, 2, 8, 8, 3], [3, 8, 8, 8, 2], [3, 2, 8, 8, 8], [3, 2, 8, 8, 8]]
# all_list = []
# for index in indexes:
#     nums_list[index[0]], nums_list[index[1]] = nums_list[index[1]], nums_list[index[0]]


# cnt = pick_2_subset(lists[0])  # index 자리에
#
# for c in cnt:
#     lists += [c]
#
# print(lists)
#

# print(deep_depth_may(lists))
my_max = deep_depth_may(lists)
for m in range(n):
    temp = []
    if m == 0:
        cnt = []
        b = lists[0]
        cnt = pick_2_subset(b) # 0 == m
        for c in cnt:
            lists += [c]
        if my_max < deep_depth_may(cnt):
            my_max = deep_depth_may(cnt)
        del(cnt)
    else:
        nCn = len(lists)-1
        start = my_sum(m, nCn)
        for k in range(start, len(lists)):
            cnt = []
            a = lists[k]
            new = pick_2_subset(a)
            for c in cnt:
                temp += [c]
            if my_max < deep_depth_may(new):
                my_max = deep_depth_may(new)
            del(new)
    for tp in temp:
        lists += [tp]
print(my_max)