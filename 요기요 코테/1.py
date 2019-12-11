A,B,C,D = 4,4,3,2

def solution(A, B, C, D):
    numbers = [A,B,C,D]
    visited = [0,0,0,0]
    def perm(depth, time):
        if depth == 4:
            time = tuple(time)
            if time not in my_set:
                my_set.add(time)

            return
        for j in range(4):
            if visited[j] == 0:
                if depth == 0:
                    if numbers[j] in adic:
                        visited[j] = 1
                        perm(depth+1,time+[numbers[j]])
                        visited[j] = 0
                elif depth == 1:
                    if time[0] == 2:
                        if numbers[j] in bdic:
                            visited[j] = 1
                            perm(depth+1, time + [numbers[j]])
                            visited[j] = 0
                    else:
                        visited[j] = 1
                        perm(depth+1, time+[numbers[j]])
                        visited[j] = 0
                elif depth == 2:
                    if numbers[j] in cdic:
                        visited[j] = 1
                        perm(depth + 1, time + [numbers[j]])
                        visited[j] = 0
                else:
                    visited[j] = 1
                    perm(depth + 1, time + [numbers[j]])
                    visited[j] = 0

    my_set = set()
    time = [0, 0, 0, 0]
    adic = {0,1,2}
    bdic = {0,1,2,3} # if a가 2일때
    cdic = {0,1,2,3,4,5}


    perm(0,[])
    return len(my_set)

print(solution(A,B,C,D))