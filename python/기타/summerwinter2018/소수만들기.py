def make_prime_num():
    arr = [True] * 3001
    for i in range(2, 3001):
        if arr[i]:
            for j in range(i*2, 3001, i):
                arr[j] = False

    return arr


def solution(nums):
    answer = 0
    prime_list = make_prime_num()
    len_nums = len(nums)
    for i in range(len_nums-2):
        for j in range(i+1, len_nums-1):
            for k in range(j+1, len_nums):
                if prime_list[nums[i] + nums[j] + nums[k]]:
                    answer += 1
    return answer

solution([1, 2, 3, 4])
solution([1, 2, 7, 6, 4])