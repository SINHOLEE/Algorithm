heights = [1,5,3,6,7,6,5]

def solution(heights):


    answer = [0] * len(heights)

    for i in range(len(heights)-1, 0, -1):
        for j in range(i-1, -1, -1):
            if heights[j] > heights[i]:
                answer[i] = j+1
                break

            # print(i, j)


        # print(i)
    return answer

print(solution(heights))