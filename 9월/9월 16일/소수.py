
def issotsu(n):
    return all([(n % j) for j in range(2, int(n ** 0.5) + 1)]) and n > 1



def perm(depth, r, memb, tep):
    global answer, visited, bucket
    if depth == r:
        if PrimeNums[int(tep)] and bucket[int(tep)] == False:
            bucket[int(tep)] = True
            answer += 1
        return
    for i in range(len(memb)):
        if visited[i] == False:
            visited[i] = True

            perm(depth+1, r, memb, tep + memb[i])
            visited[i] = False

def solution(numbers):
    global answer, visited, bucket
    answer = 0
    bucket = [False] * 10000000
    visited = [False]*len(numbers)
    for i in range(1, len(numbers)+1):
        temp = ''
        perm(0,i, numbers ,temp)

    return answer

numbers = '011'

print(solution(numbers))
