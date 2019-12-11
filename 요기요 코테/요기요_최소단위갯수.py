S = 'abba' * 200000

def solution(S):
    cnt = 1
    my_set = set()
    for char in S:
        if char not in my_set:
            my_set.add(char)
        else:
            my_set = set()
            my_set.add(char)
            cnt += 1

    return cnt

print(solution(S))