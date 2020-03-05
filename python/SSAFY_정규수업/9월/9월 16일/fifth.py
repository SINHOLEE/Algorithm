prices = [1, 2, 3, 2, 3,4,4,1,23,23]

def solution(prices):

    answer = []
    for i in range(len(prices)):
        current = prices[i]
        count = 0
        for j in range(i+1, len(prices)):
            if current <= prices[j]:
                count += 1
            else:
                count += 1

                break
        answer.append(count)


    return answer

print(solution(prices))

