def solution(number, k):
    length = len(number)
    number = list( number)
    rnd = length - k
    visited = [0] * length
    answer = ""
    maz_cnt = 0
    max_idx = 0
    for i in range(rnd):
        temp = "0"
        for j in range(max_idx, k+i+1):
            if visited[j] == 0 and ord(temp) < ord(number[j]):
                temp = number[j]
                max_idx = j
                if temp == "9":
                    break
        visited[max_idx] = 1
        answer += temp

    return answer


solution("1231234",	3)

