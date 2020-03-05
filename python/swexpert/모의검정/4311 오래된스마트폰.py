def only_nums(depth):

    global M, target, passible_nums, check, result, nums# max_depth
    if depth == M + 1:
        return
    if len(target) + 1 <= depth:
        return
    for chr_of_nums in passible_nums:
        if depth == 1 and chr_of_nums == '0':
            continue
        nums += chr_of_nums
        result += 1
        if int(nums) > int(target):
            result = 0
            nums = ''
            check = True
            break
        else:
            if nums == target:
                check = True
                break
            else:
                only_nums(depth + 1)
                if check:
                    return
                else:
                    result -= 1
                    nums = nums[:-1]
    if check:
        return


T = int(input())

cals = [0, '+', '-', '*', '/']
for tc in range(1, T+1):
    N, O, M = map(int, input().split())  # 터치 가능한 숫자의 개수, 터치 가능한 연산자 개수, 최대 터치 가능 횟수

    passible_nums = sorted(list(map(str, input().split())))
    passible_cals = list(map(str, input().split()))
    target = str(input())
    print('tl', len(target))
    print(passible_nums)
    # 1 순열로 가능성 판단하기
    nums = ''
    result = 0
    check = False
    only_nums(1)
    print(result)
    print(nums)

