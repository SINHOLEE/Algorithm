brown = 8
red = 1

def solution(brown, red):

    for i in range(1, int(red ** 0.5) + 1):
        if red % i == 0:
            if (red // i) * 2 + i * 2 + 4 == brown:
                answer = [red // i +2, i+2]
                break

    return answer
print(solution(brown,red))