# from pprint import pprint
T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    mat = [[0] * N for _ in range(N)]
    for m in range(M):
        i, j = map(int, input().split())
        mat[i-1][j-1] = 1
        mat[j-1][i-1] = 1


    visited = [False] * N
    count = 0
    for i in range(N):
        if visited[i] == False:
            count += 1

            my_queue = [i]
            while my_queue:
                for _ in range(len(my_queue)):
                    node = my_queue.pop(0)
                    if visited[node] == True:
                        continue
                    visited[node] = True
                    for i in range(len(mat[node])):
                        if visited[i] == False and mat[node][i] == 1:
                            if not my_queue:
                                my_queue.append(i)
                            else:
                                my_queue[-1:] = [my_queue[-1], i]


    print('#%s %s' % (tc,count))


