s = "a"
# s = "aabbaccc"
def solution(s):
    mid = len(s) // 2
    min_len = 1000
    if len(s) == 1:
        return 1
    for i in range(1, mid+1):  # mid개의 문자 개수까지 한번에 바라볼 수 있다.

        cnt = 0
        temp = 1
        for j in range(0, len(s) , i):
            if s[j:j+i] == s[j+i:j+(i*2)]:
                temp += 1
            else:
                if temp == 1:
                    cnt += len(s[j:j+i]) # i가 1 일때랑
                else:
                    cnt += len(str(temp)) + i
                    temp = 1
        if min_len > cnt:
            min_len = cnt
        answer = 0

    return min_len

print(solution(s))