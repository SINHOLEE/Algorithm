def solution(enter, leave):
    queue = leave[:]
    stack = []
    visited = [0] *(len(leave)+1)
    answer = [0] * (len(leave)+1)
    while queue:
        while len(queue) and visited[queue[0]]: 
            a = queue.pop(0)
            idx = stack.index(a)
            # a는 퇴장할 새꾸 그니까 stack에 [1,2,3] 있고 a가 2면 idx = 1인 애까지 앞에서부터 1씩 더하면 됨
            for i in range(len(stack)):
                if(idx==i):
                    continue
                answer[a]+=1
                answer[stack[i]]+=1
            # a새꾸 빠질거니까 stack [1,2,3] -> [1,3]으로 바꿈
            stack = stack[:idx]+stack[idx+1:]
        if(len(enter)):
            temp = enter.pop(0)
            visited[temp] = 1
            stack.append(temp)

    return answer[1:]

print(solution(		[1, 3, 2],[1,2,3]))
print(solution(	[1, 4, 2, 3],[2, 1, 3, 4]))
print(solution(	[3,2,1],[2, 1, 3]))
print(solution(	[3,2,1],[ 1, 3,2]))
print(solution(	[1, 4, 2, 3],[2, 1, 4, 3]))

print(solution([1,2,3], [3,2,1]))

print(solution([i for i in range(1,1001)],[i for i in range(1000,0,-1)]))

for i in range(1000,0,-1):
  print(i)